# Word Wizard

A kids' app for learning root words, built from *Word Power Made Easy*.

- **Learn root words:** pick a root, see every word built from it, and tap a word to break it into its parts.
- **Quiz:** levels by root. Right answers earn points and candies, streaks give bonus points, and there's a global leaderboard.

## Stack

| Part | Tech |
|---|---|
| Web app | Angular 19 (standalone components, signals) |
| API | FastAPI, run on AWS Lambda through Mangum |
| Data | DynamoDB (one table, on-demand, with a GSI for the leaderboard) |
| Hosting | S3 (private) behind CloudFront, with `/api/*` routed to API Gateway |
| Infrastructure | Terraform, region `ap-south-1`, one environment (`dev`) |

## Layout

```
backend/        FastAPI app, tests, seed data (words.json, morphemes.json)
frontend/       Angular app
infra/          Terraform (DynamoDB, Lambda, API Gateway, S3, CloudFront)
scripts/        export_workbook.py (workbook -> JSON), build_lambda.sh (zip for Lambda)
```

## Run locally

```bash
# API on http://127.0.0.1:8000
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt -r requirements-dev.txt
.venv/bin/uvicorn app.main:app --port 8000

# Web app on http://localhost:4200 (proxies /api to the API)
cd frontend
npm install
npx ng serve --proxy-config proxy.conf.json
```

Without `WORD_WIZARD_TABLE` set, the API uses an in-memory store, so progress resets on restart.

Run the tests:

```bash
cd backend && .venv/bin/python -m pytest -q tests
```

## Build and deploy

```bash
./scripts/build_lambda.sh                 # backend/build/lambda.zip
cd frontend && npx ng build && cd ..      # frontend/dist/word-wizard-web

cd infra
terraform init
terraform plan -out=tfplan                # review first
terraform apply tfplan                    # creates billable resources
terraform output app_url                  # open this URL
```

The first `apply` uploads the web build to S3 and creates the CloudFront distribution, which can take 10 to 15 minutes. After that, rebuild the frontend and run `terraform apply` again to upload changes.

## Game rules (backend/app/game.py)

- 10 points per correct answer.
- +5 for a correct answer on the first try.
- Every 3 first-try answers in a row gives +10.
- 1 candy per question, earned once only.
- A level needs all 5 questions right. Stars come from first-try answers: 4 or 5 = 3 stars, 2 or 3 = 2 stars, otherwise 1 star.

## Player codes and privacy

- A player picks a name and gets a 6-letter code. The code is the only way back in, so progress follows the code on any device.
- No email, password or other personal data is collected. Children can play without an adult account.
- Names are not checked for uniqueness. The leaderboard shows names, so tell kids not to use their real surname.

## Known limits (v1)

- Points are updated with a read-then-write, so two answers sent at the exact same moment can race. This is fine for one child at a time, but it should be fixed with conditional writes before a classroom rollout.
- Only one environment (`dev`) and local Terraform state. Move state to an S3 backend with locking before adding `prod`.
- A lost code cannot be recovered. Add a parent or teacher recovery option later if needed.
- Quiz questions are generated from the workbook data. Some distractors are sensible but not perfect; review the question bank before a wider release.
