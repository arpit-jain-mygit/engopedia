import { Component, OnInit, inject, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';
import { PlayerService } from '../core/player.service';
import { ApiService } from '../core/api.service';
import { AvatarComponent } from '../core/avatar.component';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [FormsModule, RouterLink, AvatarComponent],
  template: `
    @if (player.profile(); as p) {
      <section class="hero">
        <app-avatar [equipped]="p.equipped" [catalog]="emojiById()" [size]="120"></app-avatar>
        <h1>Hi, {{ p.name }}!</h1>
        <p>Your wizard code: <strong class="code">{{ p.code }}</strong></p>
        <p class="hint">Write this code down. Use it to come back to your spells on any device.</p>
      </section>

      <section class="choices">
        <a class="big learn" routerLink="/learn">
          <span class="emoji" aria-hidden="true">📚</span>
          <strong>Learn root words</strong>
          <span>Break words into parts and see what they mean.</span>
        </a>
        <a class="big quiz" routerLink="/quiz">
          <span class="emoji" aria-hidden="true">🎯</span>
          <strong>Quiz time</strong>
          <span>Answer questions, earn points and candies.</span>
        </a>
      </section>

      <p class="center"><a routerLink="/leaderboard">🏆 See the leaderboard</a></p>
      <p class="center small"><button class="link" (click)="switchPlayer()">Play as someone else</button></p>
    } @else {
      <section class="hero">
        <div class="wizard" aria-hidden="true">🧙</div>
        <h1>Word Wizard</h1>
        <p>Learn root words, then cast them in a quiz to earn points and candies.</p>
      </section>

      <section class="card form">
        <label for="name">Choose a wizard name</label>
        <input id="name" maxlength="16" [(ngModel)]="name" placeholder="e.g. Maya" autocomplete="off">
        <button class="btn block" (click)="start()" [disabled]="busy() || !name.trim()">
          {{ busy() ? 'Starting...' : 'Start my spellbook' }}
        </button>

        <hr>

        <label for="code">Already have a wizard code?</label>
        <div class="row">
          <input id="code" maxlength="6" [(ngModel)]="code" placeholder="6 letters" autocomplete="off" style="text-transform:uppercase">
          <button class="btn ghost" (click)="resume()" [disabled]="busy() || code.trim().length < 6">Open</button>
        </div>
        @if (error()) {
          <p class="error" role="alert">{{ error() }}</p>
        }
      </section>
    }
  `,
  styles: [`
    .hero { text-align: center; padding-top: 12px; }
    .wizard { font-size: 72px; line-height: 1; }
    h1 { font-family: var(--display); font-size: 40px; margin: 8px 0 4px; }
    .code { font-family: var(--display); letter-spacing: 0.15em; font-size: 22px; color: var(--accent); }
    .hint, .small { color: var(--muted); font-size: 15px; }
    .choices { display: grid; grid-template-columns: 1fr; gap: 14px; margin: 24px 0; }
    @media (min-width: 640px) { .choices { grid-template-columns: 1fr 1fr; } }
    .big { display: flex; flex-direction: column; gap: 6px; padding: 26px 22px; border-radius: 22px; text-decoration: none; color: var(--fg); border: 2px solid var(--line); background: var(--surface); min-height: 150px; }
    .big strong { font-family: var(--display); font-size: 26px; }
    .big span:last-child { color: var(--muted); }
    .big.learn { border-color: var(--accent); }
    .big.quiz { border-color: var(--correct); }
    .emoji { font-size: 44px; }
    .center { text-align: center; }
    .form { max-width: 420px; margin: 24px auto 0; display: flex; flex-direction: column; gap: 10px; }
    .form label { font-weight: 600; }
    .form input { min-height: 52px; padding: 12px 14px; font: inherit; font-size: 17px; border-radius: 14px; border: 2px solid var(--line); background: var(--bg); color: var(--fg); }
    .row { display: flex; gap: 8px; }
    .row input { flex: 1; min-width: 0; }
    hr { border: 0; border-top: 1px solid var(--line); margin: 8px 0; }
    .error { color: var(--retry); margin: 0; }
    .link { background: none; border: 0; color: var(--accent); font: inherit; cursor: pointer; text-decoration: underline; min-height: 44px; }
  `],
})
export class HomePage implements OnInit {
  player = inject(PlayerService);
  private api = inject(ApiService);
  emojiById = signal<Record<string, string>>({});
  name = '';
  code = '';
  busy = signal(false);
  error = signal('');

  ngOnInit() {
    this.api.shop().subscribe({
      next: (r) => this.emojiById.set(Object.fromEntries(r.items.map((i) => [i.id, i.emoji]))),
    });
    const saved = this.player.savedCode();
    if (saved && !this.player.profile()) {
      this.busy.set(true);
      this.player.resume(saved).subscribe({
        next: () => this.busy.set(false),
        error: () => {
          this.player.forget();
          this.busy.set(false);
        },
      });
    }
  }

  start() {
    this.busy.set(true);
    this.error.set('');
    this.player.create(this.name.trim()).subscribe({
      next: () => this.busy.set(false),
      error: () => {
        this.busy.set(false);
        this.error.set('Could not start. Please try again.');
      },
    });
  }

  resume() {
    this.busy.set(true);
    this.error.set('');
    this.player.resume(this.code).subscribe({
      next: () => this.busy.set(false),
      error: () => {
        this.busy.set(false);
        this.error.set('No wizard has that code. Check the letters and try again.');
      },
    });
  }

  switchPlayer() {
    this.player.forget();
    this.name = '';
    this.code = '';
  }
}
