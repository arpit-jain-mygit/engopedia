import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';
import { AnswerResult, FinishResult, LeaderRow, LevelInfo, Profile, QuizQuestion, ShopItem, WordCard } from './models';

export interface AnswerBody {
  choice?: number;
  text?: string;
  pairs?: string[];
}

// All calls use the relative /api path. CloudFront sends /api to the Lambda,
// and the Angular dev server proxies it to uvicorn locally (proxy.conf.json).
@Injectable({ providedIn: 'root' })
export class ApiService {
  private http = inject(HttpClient);

  rootLevels(): Observable<{ levels: LevelInfo[] }> {
    return this.http.get<{ levels: LevelInfo[] }>('/api/roots');
  }

  rootWords(root: string): Observable<{ root: string; meaning: string; cards: WordCard[] }> {
    return this.http.get<{ root: string; meaning: string; cards: WordCard[] }>(`/api/roots/${encodeURIComponent(root)}/words`);
  }

  createPlayer(name: string): Observable<Profile> {
    return this.http.post<Profile>('/api/players', { name });
  }

  getPlayer(code: string): Observable<Profile> {
    return this.http.get<Profile>(`/api/players/${encodeURIComponent(code)}`);
  }

  questions(code: string, root: string): Observable<{ root: string; meaning: string; questions: QuizQuestion[] }> {
    return this.http.get<{ root: string; meaning: string; questions: QuizQuestion[] }>(
      `/api/players/${encodeURIComponent(code)}/levels/${encodeURIComponent(root)}/questions`
    );
  }

  // One body per format: choice (index), text (build, type) or pairs (match).
  answer(code: string, root: string, questionId: string, body: AnswerBody): Observable<AnswerResult> {
    return this.http.post<AnswerResult>(`/api/players/${encodeURIComponent(code)}/answers`, {
      root,
      question_id: questionId,
      ...body,
    });
  }

  finishLevel(code: string, root: string): Observable<FinishResult> {
    return this.http.post<FinishResult>(`/api/players/${encodeURIComponent(code)}/levels/${encodeURIComponent(root)}/finish`, {});
  }

  shop(): Observable<{ items: ShopItem[] }> {
    return this.http.get<{ items: ShopItem[] }>('/api/shop');
  }

  buyItem(code: string, itemId: string): Observable<Profile> {
    return this.http.post<Profile>(`/api/players/${encodeURIComponent(code)}/shop/buy`, { item_id: itemId });
  }

  equipItem(code: string, itemId: string): Observable<Profile> {
    return this.http.post<Profile>(`/api/players/${encodeURIComponent(code)}/shop/equip`, { item_id: itemId });
  }

  leaderboard(limit = 10): Observable<{ rows: LeaderRow[] }> {
    return this.http.get<{ rows: LeaderRow[] }>(`/api/leaderboard?limit=${limit}`);
  }
}
