import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';
import { AnswerResult, CmChapter, CmNote, CmQuiz, CmQuizResult, FinishResult, LeaderRow, LevelInfo, Profile, QuizQuestion, ShopItem, WmAnswerResult, WmChapter, WmQuestionList, WmTestItem, WmTestResult, WordCard } from './models';

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

  wmChapters(): Observable<{ chapters: WmChapter[] }> {
    return this.http.get<{ chapters: WmChapter[] }>('/api/wm/chapters');
  }

  wmQuestions(code: string, chapter: number): Observable<WmQuestionList> {
    return this.http.get<WmQuestionList>(`/api/players/${encodeURIComponent(code)}/wm/chapters/${chapter}/questions`);
  }

  wmProgress(code: string): Observable<{ done: Record<string, number> }> {
    return this.http.get<{ done: Record<string, number> }>(`/api/players/${encodeURIComponent(code)}/wm/progress`);
  }

  wmAnswer(code: string, chapter: number, questionId: string, choice: number): Observable<WmAnswerResult> {
    return this.http.post<WmAnswerResult>(`/api/players/${encodeURIComponent(code)}/wm/answers`, {
      chapter,
      question_id: questionId,
      choice,
    });
  }

  // Student-made test: chapters and formats are chosen by the student; no login needed.
  wmBuildTest(chapters: number[], formats: string[], count: number): Observable<{ items: WmTestItem[] }> {
    const params = `chapters=${chapters.join(',')}&formats=${formats.join('')}&count=${count}`;
    return this.http.get<{ items: WmTestItem[] }>(`/api/wm/tests/build?${params}`);
  }

  wmGradeTest(items: { id: string; answer: string }[]): Observable<WmTestResult> {
    return this.http.post<WmTestResult>('/api/wm/tests/grade', { items });
  }

  // Cambridge Stage 8: chapter notes, chapter quizzes and student-made tests. No login needed.
  cmChapters(): Observable<{ chapters: CmChapter[] }> {
    return this.http.get<{ chapters: CmChapter[] }>('/api/cm/chapters');
  }

  cmChapter(chapter: number): Observable<CmNote> {
    return this.http.get<CmNote>(`/api/cm/chapters/${chapter}`);
  }

  cmQuiz(chapter: number): Observable<CmQuiz> {
    return this.http.get<CmQuiz>(`/api/cm/chapters/${chapter}/quiz`);
  }

  cmBuildTest(chapters: number[], formats: string[], count: number): Observable<{ items: WmTestItem[] }> {
    const params = `chapters=${chapters.join(',')}&formats=${formats.join('')}&count=${count}`;
    return this.http.get<{ items: WmTestItem[] }>(`/api/cm/tests/build?${params}`);
  }

  cmGradeTest(items: { id: string; answer: string }[]): Observable<WmTestResult> {
    return this.http.post<WmTestResult>('/api/cm/tests/grade', { items });
  }

  cmGradeForPlayer(code: string, items: { id: string; answer: string }[]): Observable<CmQuizResult> {
    return this.http.post<CmQuizResult>(`/api/players/${code}/cm/grade`, { items });
  }

  leaderboard(limit = 10): Observable<{ rows: LeaderRow[] }> {
    return this.http.get<{ rows: LeaderRow[] }>(`/api/leaderboard?limit=${limit}`);
  }
}
