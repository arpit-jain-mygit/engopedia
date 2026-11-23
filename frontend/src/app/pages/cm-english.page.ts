import { Component } from '@angular/core';

// Cambridge Stage 8 English: six unofficial practice papers. Each paper has an exam paper, a mark scheme
// and a student copy, all hosted as PDFs (no login).
interface EnglishPaper {
  number: number;
  title: string;
  kind: string;
  file: string; // the exam paper file name, without the document type
}

const BASE = '/papers/cambridge-stage8-english/';
const DATE = '2026-10-14_1340_v2_Stage8';

const PAPERS: EnglishPaper[] = [
  { number: 1, title: 'Non-fiction: memoir', kind: 'Nonfiction', file: 'Paper_1_Nonfiction' },
  { number: 2, title: 'Fiction: comic-gothic story', kind: 'Fiction', file: 'Paper_2_Fiction' },
  { number: 3, title: 'Explanatory: two texts', kind: 'Explanatory', file: 'Paper_3_Explanatory' },
  { number: 4, title: 'Persuasive: opinion writing', kind: 'Persuasive', file: 'Paper_4_Persuasive' },
  { number: 5, title: 'Drama: playscript about conflict', kind: 'Drama', file: 'Paper_5_Drama' },
  { number: 6, title: 'Poetry: two poems on growing up', kind: 'Poetry', file: 'Paper_6_Poetry' },
];

@Component({
  selector: 'app-cm-english',
  standalone: true,
  template: `
    <h1>📝 English Stage 8</h1>
    <p class="sub">Unofficial practice papers in the Cambridge style. Open the paper, the mark scheme or the student copy.</p>

    @for (p of papers; track p.number) {
      <section class="paper">
        <h2>Paper {{ p.number }}: {{ p.title }}</h2>
        <div class="links">
          <a [href]="url(p.file)" target="_blank" rel="noopener">📄 Exam paper</a>
          <a [href]="url(p.number, 'Mark_Scheme')" target="_blank" rel="noopener">✅ Mark scheme</a>
          <a [href]="url(p.number, 'Student_Copy')" target="_blank" rel="noopener">✏️ Student copy</a>
        </div>
      </section>
    }
  `,
  styles: [`
    h1 { font-family: var(--display); font-size: 30px; margin: 8px 0 4px; }
    .sub { color: var(--muted); margin: 0 0 16px; }
    .paper { background: var(--surface); border: 1px solid var(--line); border-radius: 16px; padding: 14px 16px; margin-bottom: 12px; }
    h2 { font-size: 17px; margin: 0 0 10px; overflow-wrap: anywhere; }
    .links { display: flex; gap: 8px; flex-wrap: wrap; }
    .links a { padding: 10px 14px; border-radius: 12px; border: 1px solid var(--line); color: var(--fg); text-decoration: none; min-height: 44px; display: inline-flex; align-items: center; }
    .links a:hover { border-color: var(--accent); }
  `],
})
export class CmEnglishPage {
  readonly papers = PAPERS;

  // Exam paper: "Paper_1_Nonfiction_<date>.pdf". Mark scheme and student copy use the same pattern with a different type word.
  url(p: string | number, type?: string): string {
    if (typeof p === 'string') return `${BASE}${p}_${DATE}.pdf`;
    return `${BASE}Paper_${p}_${type}_${DATE}.pdf`;
  }
}
