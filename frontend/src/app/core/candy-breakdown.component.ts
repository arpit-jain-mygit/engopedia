import { Component, computed, input } from '@angular/core';
import { CandiesByCategory } from './models';

// Shows the candies for each category as small pills: Word Wizard, Grammar, and the two Cambridge categories.
@Component({
  selector: 'app-candy-breakdown',
  standalone: true,
  template: `
    <div class="breakdown" aria-label="Candies by category">
      @for (c of cats(); track c.label) {
        <span class="cat"><span aria-hidden="true">{{ c.icon }}</span> {{ c.label }} <b>{{ c.value }}</b></span>
      }
    </div>
  `,
  styles: [`
    .breakdown { display: flex; flex-wrap: wrap; gap: 8px; justify-content: center; }
    .cat { display: inline-flex; align-items: center; gap: 4px; padding: 6px 12px; border-radius: 999px; border: 1px solid var(--line); background: var(--bg); font-size: 14px; }
    .cat b { font-variant-numeric: tabular-nums; }
  `],
})
export class CandyBreakdownComponent {
  breakdown = input<CandiesByCategory | undefined>();

  cats = computed(() => {
    const b = this.breakdown();
    return [
      { icon: '🧙', label: 'Word Wizard', value: b?.word_wizard ?? 0 },
      { icon: '📖', label: 'Grammar', value: b?.grammar ?? 0 },
      { icon: '📐', label: 'Cambridge Maths', value: b?.cambridge_maths ?? 0 },
      { icon: '📝', label: 'Cambridge English', value: b?.cambridge_english ?? 0 },
    ];
  });
}
