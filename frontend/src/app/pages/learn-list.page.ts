import { Component, OnInit, inject, signal } from '@angular/core';
import { RouterLink } from '@angular/router';
import { ApiService } from '../core/api.service';
import { LevelInfo } from '../core/models';

@Component({
  selector: 'app-learn-list',
  standalone: true,
  imports: [RouterLink],
  template: `
    <h1>📚 Pick a root word</h1>
    <p class="sub">A root is the core of a word. Tap one to see every word built from it.</p>

    @if (loading()) {
      <p class="sub">Opening the spellbook...</p>
    } @else if (error()) {
      <p class="error" role="alert">{{ error() }}</p>
    } @else {
      <div class="grid">
        @for (lv of levels(); track lv.root) {
          <a class="tile" [routerLink]="['/learn', lv.root]">
            <span class="root">{{ lv.root }}</span>
            <span class="gloss">{{ lv.meaning }}</span>
            <span class="count">{{ lv.word_count }} words</span>
          </a>
        }
      </div>
    }
  `,
  styles: [`
    h1 { font-family: var(--display); font-size: 30px; margin: 8px 0 4px; }
    .sub { color: var(--muted); margin: 0 0 16px; }
    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 10px; }
    .tile { display: flex; flex-direction: column; gap: 4px; padding: 14px; border-radius: 16px; background: var(--surface); border: 1px solid var(--line); color: var(--fg); text-decoration: none; min-height: 110px; }
    .tile:hover { border-color: var(--accent); }
    .root { font-family: var(--display); font-weight: 800; font-size: 22px; }
    .gloss { color: var(--muted); font-size: 14px; flex: 1; }
    .count { font-size: 12px; color: var(--accent); font-weight: 600; }
    .error { color: var(--retry); }
  `],
})
export class LearnListPage implements OnInit {
  private api = inject(ApiService);
  levels = signal<LevelInfo[]>([]);
  loading = signal(true);
  error = signal('');

  ngOnInit() {
    this.api.rootLevels().subscribe({
      next: (r) => {
        this.levels.set(r.levels);
        this.loading.set(false);
      },
      error: () => {
        this.error.set('Could not load the root words. Please try again.');
        this.loading.set(false);
      },
    });
  }
}
