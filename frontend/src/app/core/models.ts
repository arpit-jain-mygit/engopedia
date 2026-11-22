// Shapes returned by the FastAPI backend.

export interface LevelInfo {
  root: string;
  meaning: string;
  word_count: number;
  unlocked: boolean;
  completed: boolean;
  stars: number;
}

export interface Profile {
  code: string;
  name: string;
  points: number;
  candies: number;
  streak: number;
  owned: string[];
  equipped: Record<string, string>;
  levels: LevelInfo[];
}

export interface ShopItem {
  id: string;
  slot: 'hat' | 'wand' | 'pet';
  name: string;
  emoji: string;
  price: number;
}

export interface Part {
  text: string;
  type: string;
  meaning: string;
}

export interface WordCard {
  word: string;
  parts: Part[];
  meaning: string;
  sentence: string;
}

// The nine quiz formats. Choice-style ones use "choices"; the others use the fields noted below.
export type QuizFormat = 'choice' | 'emoji' | 'hear' | 'odd' | 'tf' | 'scenario' | 'two' | 'build' | 'type' | 'match';

export interface QuizQuestion {
  id: string;
  format: QuizFormat;
  prompt: string;
  choices?: string[];        // choice-style formats, two-step (current step)
  scene?: string;            // emoji picture shown above the prompt
  speak?: string;            // hear: sentence read aloud
  stage?: number;            // two-step: which step (0-based)
  stage_total?: number;      // two-step: number of steps
  tiles?: string[];          // build: tiles to tap, already shuffled
  length?: number;           // type: letters in the word
  lefts?: string[];          // match: words in order
  rights?: string[];         // match: meanings, shuffled
}

export interface AnswerResult {
  correct: boolean;
  already_answered: boolean;
  points_awarded: number;
  candies_awarded: number;
  first_try?: boolean;
  stage_passed?: boolean;    // two-step: first step right, second step to come
  next?: QuizQuestion;       // two-step: the second step
  explanation: string;
  points: number;
  candies: number;
  streak: number;
}

export interface FinishResult {
  root: string;
  stars: number;
  first_try: number;
  total: number;
  points: number;
  candies: number;
}

export interface LeaderRow {
  name: string;
  points: number;
}
