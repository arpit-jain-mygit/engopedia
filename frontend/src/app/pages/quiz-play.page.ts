import { Component, Input, OnDestroy, OnInit, inject, signal, computed } from '@angular/core';
import { RouterLink, Router } from '@angular/router';
import { ApiService, AnswerBody } from '../core/api.service';
import { PlayerService } from '../core/player.service';
import { AvatarComponent } from '../core/avatar.component';
import { AnswerResult, FinishResult, QuizQuestion } from '../core/models';

@Component({
  selector: 'app-quiz-play',
  standalone: true,
  imports: [RouterLink, AvatarComponent],
  template: `
    <a routerLink="/quiz" class="back">← Quiz map</a>

    @if (loading()) {
      <p class="sub">Preparing your spell...</p>
    } @else if (error()) {
      <p class="error" role="alert">{{ error() }}</p>
    } @else if (finished()) {
      <section class="card result">
        <div class="medal" aria-hidden="true">{{ result()!.stars === 3 ? '🏆' : '🏅' }}</div>
        <h1>{{ result()!.stars === 3 ? 'Wizard master!' : 'Level complete!' }}</h1>
        <p class="stars" [attr.aria-label]="result()!.stars + ' stars'">{{ stars(result()!.stars) }}</p>
        <p class="sub">{{ result()!.first_try }} of {{ result()!.total }} right on the first try.</p>
        <div class="haul">
          <div><b>{{ player.profile()?.points ?? 0 }}</b><span>total points</span></div>
          <div><b>{{ player.profile()?.candies ?? 0 }}</b><span>candies</span></div>
        </div>
        <div class="actions">
          <a class="btn" routerLink="/quiz">Next level</a>
          <a class="btn ghost" routerLink="/leaderboard">See leaderboard</a>
        </div>
      </section>
    } @else {
      <div class="top">
        <span class="count">Question {{ index() + 1 }} of {{ total() }}</span>
        <span class="pill star">⭐ {{ player.profile()?.points ?? 0 }}</span>
        <span class="pill candy">🍬 {{ player.profile()?.candies ?? 0 }}</span>
        <span class="pill">🔥 {{ streak() }}</span>
      </div>
      <div class="bar" role="progressbar" [attr.aria-valuenow]="progress()" aria-valuemin="0" aria-valuemax="100">
        <i [style.width.%]="progress()"></i>
      </div>

      @if (celebrate()) {
        <div class="confetti" aria-hidden="true">
          @for (bit of confetti; track $index) {
            <span class="bit" [style.left.%]="bit.x" [style.background]="bit.color" [style.animation-delay.ms]="bit.delay" [style.transform]="'rotate(' + bit.spin + 'deg)'"></span>
          }
        </div>
      }

      <section class="card prompt">
        <div class="mascot" [class.happy]="solved()" [class.oops]="oops()">
          <app-avatar [equipped]="player.profile()?.equipped ?? {}" [catalog]="emojiById()" [size]="88"
                      [mood]="solved() ? '🎉' : oops() ? '🤔' : '🧙'"></app-avatar>
        </div>
        @if (current()!.scene) {
          <div class="scene" aria-hidden="true">{{ current()!.scene }}</div>
        }
        <h1>{{ current()!.prompt }}</h1>
        @if (current()!.speak) {
          <button class="listen" type="button" (click)="speak()">🔊 Listen again</button>
        }
        @if (stepNote()) {
          <p class="step">{{ stepNote() }}</p>
        }
      </section>

      @switch (current()!.format) {
        @case ('build') {
          <div class="tiles-slot" aria-label="Your word">
            @for (t of built(); track $index; let b = $index) {
              <button class="slot-chip" type="button" [disabled]="solved()" (click)="unbuild(b)" [attr.aria-label]="'Remove ' + t.text">{{ t.text }}</button>
            }
            @if (!built().length) {
              <span class="placeholder">Tap the tiles in order</span>
            }
          </div>
          <div class="tile-pool">
            @for (t of current()!.tiles ?? []; track $index; let k = $index) {
              <button class="tile" type="button" [disabled]="solved() || usedTiles().includes(k)" (click)="addTile(k)">{{ t }}</button>
            }
          </div>
          <div class="row">
            <button class="btn ghost" type="button" [disabled]="solved() || !built().length" (click)="undo()">Undo</button>
            <button class="btn" type="button" [disabled]="solved() || !built().length || busy()" (click)="checkText(builtText())">Check</button>
          </div>
        }
        @case ('type') {
          <input class="answer-field" type="text" autocomplete="off" autocapitalize="off" spellcheck="false"
                 placeholder="Type here" aria-label="Your answer" [disabled]="solved()"
                 [value]="typed()" (input)="typed.set($any($event.target).value)"
                 (keydown.enter)="checkText(typed())">
          <div class="row">
            <button class="btn" type="button" [disabled]="solved() || !typed().trim() || busy()" (click)="checkText(typed())">Check</button>
          </div>
        }
        @case ('match') {
          <div class="match">
            @for (l of current()!.lefts ?? []; track $index; let k = $index) {
              <b>{{ l }}</b>
              <select [attr.aria-label]="'Meaning for ' + l" [disabled]="solved()" (change)="setMatch(k, $any($event.target).value)">
                <option value="" [selected]="!matchPick()[k]">Choose meaning</option>
                @for (r of current()!.rights ?? []; track $index) {
                  <option [value]="r" [selected]="matchPick()[k] === r">{{ r }}</option>
                }
              </select>
            }
          </div>
          <div class="row">
            <button class="btn" type="button" [disabled]="solved() || !allMatched() || busy()" (click)="checkMatch()">Check pairs</button>
          </div>
        }
        @default {
          <div class="choices">
            @for (c of current()!.choices ?? []; track $index; let i = $index) {
              <button class="choice" [class.correct]="correctIndex() === i" [class.pop]="correctIndex() === i" [class.retry]="wrongIndexes().includes(i)" [class.shake]="shakeIndex() === i"
                      [disabled]="busy() || solved() || wrongIndexes().includes(i)"
                      (click)="pick(i)">
                <span class="key">{{ i + 1 }}</span> {{ c }}
              </button>
            }
          </div>
        }
      }

      @if (feedback(); as f) {
        <div class="feedback" [class.good]="f.correct" [class.try]="!f.correct" role="status" aria-live="polite">
          <h2>{{ f.stage_passed ? 'Step one done!' : f.correct ? 'Yes! Great spell.' : 'Almost. Try again!' }}</h2>
          <p>{{ f.explanation }}</p>
          @if (f.correct && !f.stage_passed) {
            <div class="earned">
              <span class="pill star">+{{ f.points_awarded }} pts</span>
              @if (f.candies_awarded) { <span class="pill candy">🍬 +{{ f.candies_awarded }}</span> }
              @if (f.first_try) { <span class="pill">first try!</span> }
            </div>
          }
        </div>
      }

      <div class="next">
        <button class="btn" [disabled]="!solved() || finishing()" (click)="next()">
          {{ index() + 1 === total() ? 'See results' : 'Next' }}
        </button>
      </div>
    }
  `,
  styles: [`
    .back { color: var(--accent); text-decoration: none; font-weight: 600; min-height: 44px; display: inline-flex; align-items: center; }
    .sub, .hint, .small { color: var(--muted); }
    .error { color: var(--retry); }
    .top { display: flex; gap: 8px; align-items: center; flex-wrap: wrap; margin: 8px 0; }
    .count { font-weight: 700; margin-right: auto; }
    .bar { height: 12px; background: var(--line); border-radius: 999px; overflow: hidden; margin-bottom: 14px; }
    .bar > i { display: block; height: 100%; background: var(--correct); transition: width 0.3s ease; }
    .prompt { text-align: center; }
    .prompt h1 { font-family: var(--display); font-size: 28px; margin: 6px 0; text-wrap: balance; }
    .scene { font-size: 56px; line-height: 1.1; margin-top: 4px; }
    .step { color: var(--accent); font-weight: 700; margin: 6px 0 0; }
    .listen { min-height: 44px; padding: 8px 16px; border-radius: 999px; border: 2px solid var(--line); background: var(--surface); color: var(--fg); font: inherit; font-weight: 600; cursor: pointer; }
    .choices { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin: 16px 0; }
    .choice { min-height: 76px; padding: 12px; border-radius: 16px; border: 2px solid var(--line); background: var(--surface); color: var(--fg); font: inherit; font-weight: 600; font-size: 16px; cursor: pointer; display: flex; align-items: center; justify-content: center; text-align: center; }
    .choice:hover:not(:disabled) { border-color: var(--accent); }
    .choice.correct { border-color: var(--correct); background: var(--correct-bg); }
    .choice.retry { border-color: var(--retry); background: var(--retry-bg); }
    .choice:disabled { cursor: default; }
    .key { font-family: var(--display); color: var(--muted); margin-right: 4px; }
    .tiles-slot { min-height: 64px; margin: 16px 0 10px; padding: 10px; border-radius: 16px; border: 2px dashed var(--line); display: flex; flex-wrap: wrap; gap: 8px; align-items: center; }
    .placeholder { color: var(--muted); }
    .slot-chip, .tile { min-height: 48px; padding: 8px 14px; border-radius: 12px; font: inherit; font-weight: 700; font-size: 18px; cursor: pointer; }
    .slot-chip { border: 2px solid var(--accent); background: var(--surface); color: var(--fg); }
    .tile-pool { display: flex; flex-wrap: wrap; gap: 10px; justify-content: center; margin-bottom: 12px; }
    .tile { border: 2px solid var(--line); background: var(--tile); color: var(--fg); }
    .tile:disabled, .slot-chip:disabled { opacity: 0.4; cursor: default; }
    .answer-field { width: 100%; min-height: 56px; box-sizing: border-box; padding: 12px 14px; font: inherit; font-size: 20px; border-radius: 14px; border: 2px solid var(--line); background: var(--surface); color: var(--fg); margin: 16px 0 10px; }
    .answer-field:focus { outline: none; border-color: var(--accent); }
    .row { display: flex; gap: 10px; justify-content: flex-end; flex-wrap: wrap; margin-bottom: 8px; }
    .match { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1.4fr); gap: 10px; align-items: center; margin: 16px 0 10px; }
    .match b { font-family: var(--display); }
    .match select { min-height: 44px; font: inherit; border-radius: 12px; border: 2px solid var(--line); background: var(--surface); color: var(--fg); padding: 6px; min-width: 0; }
    .feedback { padding: 16px; border-radius: 16px; margin-top: 4px; }
    .feedback.good { background: var(--correct-bg); border: 1px solid var(--correct); }
    .feedback.try { background: var(--retry-bg); border: 1px solid var(--retry); }
    .feedback h2 { font-family: var(--display); font-size: 22px; margin: 0 0 4px; }
    .feedback p { margin: 4px 0; }
    .earned { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 8px; }
    .next { display: flex; justify-content: flex-end; margin-top: 14px; }
    .result { text-align: center; padding: 24px; }
    .medal { font-size: 72px; }
    .result h1 { font-family: var(--display); font-size: 32px; margin: 8px 0; }
    .result .stars { color: var(--star); font-size: 34px; letter-spacing: 6px; margin: 4px 0; }
    .haul { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin: 16px 0; }
    .haul div { background: var(--tile); border-radius: 14px; padding: 12px; }
    .haul b { display: block; font-family: var(--display); font-size: 26px; }
    .haul span { font-size: 13px; color: var(--muted); }
    .actions { display: flex; flex-direction: column; gap: 10px; }
    @media (min-width: 640px) { .actions { flex-direction: row; justify-content: center; } }
    /* Animations. All of them turn off when the device asks for reduced motion (see the block at the end). */
    .mascot { font-size: 56px; line-height: 1; display: inline-block; animation: idle 2.4s ease-in-out infinite; }
    .mascot.happy { animation: bounce 0.6s ease-out 2; }
    .mascot.oops { animation: wobble 0.6s ease-in-out; }
    .choice.pop { animation: pop 0.45s cubic-bezier(.2,.9,.3,1.4); }
    .choice.shake { animation: shake 0.5s ease-in-out; }
    .confetti { position: fixed; inset: 0; pointer-events: none; overflow: hidden; z-index: 20; }
    .bit { position: absolute; top: -20px; width: 10px; height: 16px; border-radius: 3px; animation: fall 1.6s ease-in forwards; }
    .bit:nth-child(3n) { width: 8px; height: 8px; border-radius: 50%; }
    @keyframes idle { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-4px); } }
    @keyframes bounce { 0% { transform: scale(1); } 40% { transform: scale(1.25) translateY(-10px); } 100% { transform: scale(1); } }
    @keyframes wobble { 0%, 100% { transform: rotate(0); } 25% { transform: rotate(-12deg); } 75% { transform: rotate(12deg); } }
    @keyframes pop { 0% { transform: scale(1); } 40% { transform: scale(1.08); } 100% { transform: scale(1); } }
    @keyframes shake { 0%, 100% { transform: translateX(0); } 20% { transform: translateX(-8px); } 40% { transform: translateX(8px); } 60% { transform: translateX(-6px); } 80% { transform: translateX(6px); } }
    @keyframes fall { 0% { transform: translateY(0) rotate(0); opacity: 1; } 100% { transform: translateY(105vh) rotate(540deg); opacity: 0.2; } }
    @media (prefers-reduced-motion: reduce) {
      .mascot, .mascot.happy, .mascot.oops, .choice.pop, .choice.shake, .bit { animation: none !important; }
    }
    @media (max-width: 420px) { .match { grid-template-columns: 1fr; } }
  `],
})
export class QuizPlayPage implements OnInit, OnDestroy {
  @Input() root = '';
  private api = inject(ApiService);
  player = inject(PlayerService);
  private router = inject(Router);

  questions = signal<QuizQuestion[]>([]);
  meaning = signal('');
  index = signal(0);
  correctIndex = signal<number | null>(null);
  wrongIndexes = signal<number[]>([]);
  feedback = signal<AnswerResult | null>(null);
  streak = signal(0);
  busy = signal(false);
  finishing = signal(false);
  shakeIndex = signal<number | null>(null);
  celebrate = signal(false);
  solved = signal(false);       // the question is answered correctly (any format)
  oops = signal(false);         // the last try was wrong
  stepNote = signal('');        // "Now step 2" line for two-step questions
  built = signal<{ text: string; k: number }[]>([]);
  typed = signal('');
  matchPick = signal<Record<number, string>>({});
  confetti: { x: number; color: string; delay: number; spin: number }[] = [];
  private timers: ReturnType<typeof setTimeout>[] = [];
  finished = signal(false);
  result = signal<FinishResult | null>(null);
  loading = signal(true);
  error = signal('');

  emojiById = signal<Record<string, string>>({});
  total = computed(() => this.questions().length);
  current = computed(() => this.questions()[this.index()] ?? null);
  progress = computed(() => (this.total() ? (this.index() / this.total()) * 100 : 0));
  usedTiles = computed(() => this.built().map((b) => b.k));
  builtText = computed(() => this.built().map((b) => b.text).join(''));
  allMatched = computed(() => {
    const n = this.current()?.lefts?.length ?? 0;
    const picks = this.matchPick();
    return n > 0 && Array.from({ length: n }, (_, k) => picks[k]).every((v) => !!v);
  });

  ngOnInit() {
    const code = this.player.profile()?.code ?? this.player.savedCode();
    if (!code) {
      this.router.navigateByUrl('/');
      return;
    }
    this.api.shop().subscribe({
      next: (r) => this.emojiById.set(Object.fromEntries(r.items.map((i) => [i.id, i.emoji]))),
    });
    this.api.questions(code, this.root).subscribe({
      next: (r) => {
        this.meaning.set(r.meaning);
        this.questions.set(r.questions);
        this.loading.set(false);
        this.enterQuestion();
      },
      error: (err) => {
        this.error.set(err.status === 403 ? 'Finish the previous level first.' : 'Could not load this level.');
        this.loading.set(false);
      },
    });
  }

  // Tap a choice button (choice-style formats, including two-step).
  pick(i: number) {
    this.submit({ choice: i }, i);
  }

  addTile(k: number) {
    const t = this.current()?.tiles?.[k];
    if (t === undefined || this.solved() || this.usedTiles().includes(k)) return;
    this.built.set([...this.built(), { text: t, k }]);
  }

  unbuild(pos: number) {
    if (this.solved()) return;
    this.built.set(this.built().filter((_, i) => i !== pos));
  }

  undo() {
    if (this.solved() || !this.built().length) return;
    this.built.set(this.built().slice(0, -1));
  }

  checkText(text: string) {
    const v = text.trim();
    if (!v) return;
    this.submit({ text: v });
  }

  setMatch(k: number, value: string) {
    this.matchPick.set({ ...this.matchPick(), [k]: value });
  }

  checkMatch() {
    const lefts = this.current()?.lefts ?? [];
    const picks = this.matchPick();
    this.submit({ pairs: lefts.map((_, k) => picks[k] ?? '') });
  }

  speak() {
    const text = this.current()?.speak;
    if (!text || typeof window === 'undefined' || !('speechSynthesis' in window)) return;
    try {
      const u = new SpeechSynthesisUtterance(text);
      u.lang = 'en-GB';
      u.rate = 0.9;
      window.speechSynthesis.cancel();
      window.speechSynthesis.speak(u);
    } catch {
      /* speech blocked: the question still works without it */
    }
  }

  private submit(body: AnswerBody, choiceIndex: number | null = null) {
    const code = this.player.profile()?.code;
    const q = this.current();
    if (!code || !q || this.busy() || this.solved()) return;
    this.busy.set(true);
    this.api.answer(code, this.root, q.id, body).subscribe({
      next: (res) => {
        this.busy.set(false);
        this.feedback.set(res);
        this.streak.set(res.streak);
        if (res.stage_passed && res.next) {
          // Two-step: step one is right, so show step two on the same question. No points yet.
          this.questions.set(this.questions().map((x, i) => (i === this.index() ? res.next! : x)));
          this.clearAnswerState();
          this.stepNote.set('Now the second step.');
        } else if (res.correct) {
          this.solved.set(true);
          this.oops.set(false);
          if (choiceIndex !== null) this.correctIndex.set(choiceIndex);
          this.burstConfetti();
        } else {
          this.oops.set(true);
          if (choiceIndex !== null) {
            this.wrongIndexes.set([...this.wrongIndexes(), choiceIndex]);
            this.shake(choiceIndex);
          }
          this.later(() => this.oops.set(false), 600);
        }
        const p = this.player.profile();
        if (p) this.player.update({ ...p, points: res.points, candies: res.candies, streak: res.streak });
      },
      error: () => {
        this.busy.set(false);
        this.feedback.set({ correct: false, already_answered: false, points_awarded: 0, candies_awarded: 0,
          explanation: 'Something went wrong. Please try that again.', points: 0, candies: 0, streak: 0 });
      },
    });
  }

  next() {
    if (this.index() + 1 < this.total()) {
      this.index.set(this.index() + 1);
      this.resetQuestion();
      this.enterQuestion();
      return;
    }
    const code = this.player.profile()?.code;
    if (!code) return;
    this.finishing.set(true);
    this.api.finishLevel(code, this.root).subscribe({
      next: (r) => {
        this.result.set(r);
        this.finished.set(true);
        this.finishing.set(false);
        this.player.refresh().subscribe();
      },
      error: () => {
        this.finishing.set(false);
        this.error.set('Could not save your level. Please try again.');
      },
    });
  }

  // Read the sentence aloud when a listening question opens.
  private enterQuestion() {
    if (this.current()?.format === 'hear') this.later(() => this.speak(), 300);
  }

  // Right answer: a short confetti burst. Random pieces, cleared after the animation.
  private burstConfetti() {
    const colors = ['#f2b531', '#2f6fdd', '#1f8a5b', '#e0457b', '#8e5cf0'];
    this.confetti = Array.from({ length: 36 }, () => ({
      x: Math.random() * 100,
      color: colors[Math.floor(Math.random() * colors.length)],
      delay: Math.floor(Math.random() * 300),
      spin: Math.floor(Math.random() * 360),
    }));
    this.celebrate.set(true);
    this.later(() => this.celebrate.set(false), 1800);
  }

  // Wrong answer: the button shakes once, then the kid can try again.
  private shake(i: number) {
    this.shakeIndex.set(i);
    this.later(() => this.shakeIndex.set(null), 500);
  }

  private later(fn: () => void, ms: number) {
    this.timers.push(setTimeout(fn, ms));
  }

  ngOnDestroy() {
    this.timers.forEach((t) => clearTimeout(t));
    try { window.speechSynthesis?.cancel(); } catch { /* ignore */ }
  }

  // Clears only what the kid entered, so a two-step question can move on to its second step.
  private clearAnswerState() {
    this.correctIndex.set(null);
    this.wrongIndexes.set([]);
    this.built.set([]);
    this.typed.set('');
    this.matchPick.set({});
  }

  private resetQuestion() {
    this.clearAnswerState();
    this.solved.set(false);
    this.oops.set(false);
    this.stepNote.set('');
    this.feedback.set(null);
  }

  stars(n: number): string {
    return '★'.repeat(n) + '☆'.repeat(3 - n);
  }
}
