"""Storage layer. DynamoStore runs on AWS; MemoryStore runs in tests and local dev.

Single-table design:
  PLAYER#<code> / PROFILE       player name, points, candies, streak
  PLAYER#<code> / LEVEL#<root>  completed flag, correct count, first-try count
  PLAYER#<code> / Q#<root>#<id> per-question state (done, wrong attempts)
Leaderboard: player items also carry GSI1PK = "BOARD" and GSI1SK = points.
"""
import os
from decimal import Decimal


def _prepare(item):
    item = dict(item)
    if item.get("type") == "PLAYER":
        item["GSI1PK"] = "BOARD"
        item["GSI1SK"] = int(item.get("points", 0))
    return item


def _plain(value):
    if isinstance(value, Decimal):
        return int(value)
    if isinstance(value, dict):
        return {k: _plain(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_plain(v) for v in value]
    return value


class MemoryStore:
    def __init__(self):
        self.items = {}

    def get(self, pk, sk):
        item = self.items.get((pk, sk))
        return dict(item) if item else None

    def put(self, item):
        prepared = _prepare(item)
        self.items[(prepared["pk"], prepared["sk"])] = prepared

    def query_prefix(self, pk, prefix):
        return [dict(v) for (p, s), v in self.items.items() if p == pk and s.startswith(prefix)]

    def board(self, limit):
        players = [v for v in self.items.values() if v.get("type") == "PLAYER"]
        players.sort(key=lambda p: -p.get("points", 0))
        return [dict(p) for p in players[:limit]]

    def code_exists(self, code):
        return self.get(f"PLAYER#{code}", "PROFILE") is not None


class DynamoStore:
    def __init__(self, table_name):
        import boto3
        from boto3.dynamodb.conditions import Key

        self._Key = Key
        self.table = boto3.resource("dynamodb").Table(table_name)

    def get(self, pk, sk):
        resp = self.table.get_item(Key={"pk": pk, "sk": sk})
        item = resp.get("Item")
        return _plain(item) if item else None

    def put(self, item):
        self.table.put_item(Item=_prepare(item))

    def query_prefix(self, pk, prefix):
        resp = self.table.query(
            KeyConditionExpression=self._Key("pk").eq(pk) & self._Key("sk").begins_with(prefix)
        )
        return [_plain(i) for i in resp.get("Items", [])]

    def board(self, limit):
        resp = self.table.query(
            IndexName="GSI1",
            KeyConditionExpression=self._Key("GSI1PK").eq("BOARD"),
            ScanIndexForward=False,
            Limit=limit,
        )
        return [_plain(i) for i in resp.get("Items", [])]

    def code_exists(self, code):
        return self.get(f"PLAYER#{code}", "PROFILE") is not None


def make_store():
    table = os.environ.get("WORD_WIZARD_TABLE")
    if table:
        return DynamoStore(table)
    return MemoryStore()
