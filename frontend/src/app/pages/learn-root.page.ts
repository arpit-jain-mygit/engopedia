import { Component, Input, OnInit, inject, signal, computed } from '@angular/core';
import { RouterLink } from '@angular/router';
import { ApiService } from '../core/api.service';
import { WordCard } from '../core/models';

@Component({
  selector: 'app-learn-root',
  standalone: true,
  imports: [RouterLink],
  template: `
    <a routerLink="/learn" class="back">← All roots</a>
    <h1>{{ root }} <span class="gloss">means "{{ meaning() }}"</span></h1>

    <label class="search">
      <span class="sr-only">Search words</span>
      <input type="search" placeholder="Search this root's words" [value]="query()" (input)="query.set($any($event.target).value)">
    </label>

    @if (loading()) {
      <p class="sub">Finding words...</p>
    } @else if (error()) {
      <p class="error" role="alert">{{ error() }}</p>
    } @else {
      <p class="sub">{{ filtered().length }} words. Tap a card to break the word apart.</p>
      <div class="cards">
        @for (card of filtered(); track card.word) {
          <article class="card" [class.open]="open() === card.word">
            <button class="card-head" (click)="toggle(card.word)" [attr.aria-expanded]="open() === card.word">
              <span class="word">{{ card.word }}</span>
              <span class="meaning">{{ card.meaning }}</span>
              <span class="chev" aria-hidden="true">{{ open() === card.word ? '▲' : '▼' }}</span>
            </button>

            @if (open() === card.word) {
              <div class="parts" [attr.aria-label]="'Parts of ' + card.word">
                @for (part of card.parts; track $index) {
                  <div class="part {{ part.type.toLowerCase() }}">
                    <span class="piece">{{ part.text }}</span>
                    <span class="kind">{{ part.type }}</span>
                    <span class="pmeaning">{{ part.meaning }}</span>
                  </div>
                }
              </div>
              <p class="sentence">💬 {{ card.sentence }}</p>
            }
          </article>
        }
      </div>
    }
  `,
  styles: [`
    .back { color: var(--accent); text-decoration: none; font-weight: 600; min-height: 44px; display: inline-flex; align-items: center; }
    h1 { font-family: var(--display); font-size: 30px; margin: 4px 0 12px; }
    .gloss { font-size: 18px; color: var(--muted); font-weight: 500; }
    .sub { color: var(--muted); }
    .search input { width: 100%; min-height: 48px; padding: 10px 14px; font: inherit; border-radius: 14px; border: 2px solid var(--line); background: var(--surface); color: var(--fg); margin-bottom: 8px; }
    .cards { display: flex; flex-direction: column; gap: 10px; }
    .card { padding: 0; overflow: hidden; }
    .card-head { display: grid; grid-template-columns: 1fr auto; gap: 2px 10px; width: 100%; padding: 14px 16px; background: none; border: 0; color: var(--fg); font: inherit; text-align: left; cursor: pointer; min-height: 56px; }
    .word { font-family: var(--display); font-weight: 800; font-size: 21px; }
    .meaning { grid-column: 1; color: var(--muted); font-size: 14px; }
    .chev { grid-row: 1 / span 2; grid-column: 2; align-self: center; color: var(--accent); }
    .parts { display: flex; flex-direction: column; gap: 6px; padding: 0 16px 8px; }
    .part { display: grid; grid-template-columns: auto auto 1fr; gap: 8px; align-items: center; padding: 8px 10px; border-radius: 12px; background: var(--tile); }
    .part.root { background: var(--correct-bg, #e3f5ec); }
    .part.prefix { background: #fdf1dc; }
    .part.suffix { background: #f1e8ff; }
    .piece { font-family: var(--display); font-weight: 800; font-size: 18px; }
    .kind { font-size: 12px; font-weight: 600; text-transform: uppercase; color: var(--muted); }
    .pmeaning { font-size: 14px; }
    .sentence { margin: 4px 16px 16px; padding: 10px 12px; border-radius: 12px; background: var(--bg); color: var(--fg); }
    .error { color: var(--retry); }
    .sr-only { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); }
  `],
})
export class LearnRootPage implements OnInit {
  @Input() root = '';
  private api = inject(ApiService);
  meaning = signal('');
  cards = signal<WordCard[]>([]);
  query = signal('');
  open = signal<string | null>(null);
  loading = signal(true);
  error = signal('');
  filtered = computed(() => {
    const q = this.query().trim().toLowerCase();
    return q ? this.cards().filter((c) => c.word.includes(q) || c.meaning.toLowerCase().includes(q)) : this.cards();
  });

  ngOnInit() {
    this.api.rootWords(this.root).subscribe({
      next: (r) => {
        this.meaning.set(r.meaning);
        this.cards.set(r.cards);
        this.loading.set(false);
      },
      error: () => {
        this.error.set('Could not open this root. Please try again.');
        this.loading.set(false);
      },
    });
  }

  toggle(word: string) {
    this.open.set(this.open() === word ? null : word);
  }
}
