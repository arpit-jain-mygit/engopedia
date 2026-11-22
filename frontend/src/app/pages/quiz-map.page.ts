import { Component, OnInit, inject, signal } from '@angular/core';
import { RouterLink } from '@angular/router';
import { ApiService } from '../core/api.service';
import { PlayerService } from '../core/player.service';
import { LevelInfo } from '../core/models';

@Component({
  selector: 'app-quiz-map',
  standalone: true,
  imports: [RouterLink],
  template: `
    <h1>🎯 Quiz map</h1>
    <p class="sub">Finish a level to unlock the next one. Earn stars for first-try answers.</p>

    @if (loading()) {
      <p class="sub">Loading your spells...</p>
    } @else if (error()) {
      <p class="error" role="alert">{{ error() }}</p>
    } @else {
      <ol class="map">
        @for (lv of levels(); track lv.root; let i = $index) {
          <li>
            @if (lv.unlocked) {
              <a class="level" [class.done]="lv.completed" [routerLink]="['/quiz', lv.root]">
                <span class="num">{{ i + 1 }}</span>
                <span class="root">{{ lv.root }}</span>
                <span class="gloss">{{ lv.meaning }}</span>
                <span class="stars" [attr.aria-label]="lv.stars + ' stars'">{{ stars(lv.stars) }}</span>
              </a>
            } @else {
              <div class="level locked" aria-disabled="true">
                <span class="num">{{ i + 1 }}</span>
                <span class="root">{{ lv.root }}</span>
                <span class="gloss">Locked</span>
                <span class="stars">🔒</span>
              </div>
            }
          </li>
        }
      </ol>
    }
  `,
  styles: [`
    h1 { font-family: var(--display); font-size: 30px; margin: 8px 0 4px; }
    .sub { color: var(--muted); margin: 0 0 16px; }
    .error { color: var(--retry); }
    .map { list-style: none; padding: 0; margin: 0; display: grid; gap: 10px; grid-template-columns: 1fr; }
    @media (min-width: 640px) { .map { grid-template-columns: 1fr 1fr; } }
    .level { display: grid; grid-template-columns: 40px 1fr auto; grid-template-areas: "num root stars" "num gloss stars"; align-items: center; gap: 0 12px; padding: 12px 14px; border-radius: 16px; background: var(--surface); border: 2px solid var(--line); color: var(--fg); text-decoration: none; min-height: 64px; }
    a.level:hover { border-color: var(--accent); }
    a.level.done { border-color: var(--correct); }
    .level.locked { opacity: 0.55; }
    .num { grid-area: num; font-family: var(--display); font-weight: 800; font-size: 20px; color: var(--muted); }
    .root { grid-area: root; font-family: var(--display); font-weight: 800; font-size: 20px; }
    .gloss { grid-area: gloss; color: var(--muted); font-size: 14px; }
    .stars { grid-area: stars; color: var(--star); letter-spacing: 2px; font-size: 16px; }
  `],
})
export class QuizMapPage implements OnInit {
  private api = inject(ApiService);
  private player = inject(PlayerService);
  levels = signal<LevelInfo[]>([]);
  loading = signal(true);
  error = signal('');

  ngOnInit() {
    const code = this.player.profile()?.code ?? this.player.savedCode();
    if (!code) {
      this.error.set('Start your spellbook on the home page first.');
      this.loading.set(false);
      return;
    }
    this.player.refresh().subscribe({
      next: (p) => {
        this.levels.set(p.levels);
        this.loading.set(false);
      },
      error: () => {
        this.error.set('Could not load your quiz map. Please try again.');
        this.loading.set(false);
      },
    });
  }

  stars(n: number): string {
    return '★'.repeat(n) + '☆'.repeat(3 - n);
  }
}
