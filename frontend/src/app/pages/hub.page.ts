import { Component, OnInit, inject } from '@angular/core';
import { RouterLink } from '@angular/router';
import { PlayerService } from '../core/player.service';

// Home page: two tiles, one for each study area. One wizard code works in both.
@Component({
  selector: 'app-hub',
  standalone: true,
  imports: [RouterLink],
  template: `
    <section class="hero">
      <div class="sparkle" aria-hidden="true">✨</div>
      <h1>Study Hub</h1>
      <p>Pick what you want to study today. Your wizard code works in both.</p>
    </section>

    <section class="choices">
      <a class="big ww" routerLink="/word-wizard">
        <span class="emoji" aria-hidden="true">🧙</span>
        <strong>Word Wizard</strong>
        <span>Learn root words, then cast them in a quiz to earn points and candies.</span>
      </a>
      <a class="big wm" routerLink="/wren-martin">
        <span class="emoji" aria-hidden="true">📖</span>
        <strong>Wren &amp; Martin Grammar</strong>
        <span>Simple notes for every chapter, and grammar quizzes from the book.</span>
      </a>
      <a class="big cm" routerLink="/cambridge">
        <span class="emoji" aria-hidden="true">📐</span>
        <strong>Cambridge Maths Stage 8</strong>
        <span>Notes for all 25 chapters, a quiz for each chapter, and tests you build yourself.</span>
      </a>
      <a class="big en" routerLink="/cambridge/english">
        <span class="emoji" aria-hidden="true">📝</span>
        <strong>Cambridge English Stage 8</strong>
        <span>Practice papers in the Cambridge style, each with a mark scheme and a student copy.</span>
      </a>
    </section>

    @if (!player.profile()) {
      <p class="center hint">Start your wizard on <a routerLink="/word-wizard">Word Wizard</a> to earn points and candies in both.</p>
    }
  `,
  styles: [`
    .hero { text-align: center; padding-top: 12px; }
    .sparkle { font-size: 64px; line-height: 1; }
    h1 { font-family: var(--display); font-size: 40px; margin: 8px 0 4px; }
    .hero p { color: var(--muted); margin: 0; }
    .choices { display: grid; grid-template-columns: 1fr; gap: 14px; margin: 24px 0; }
    @media (min-width: 640px) { .choices { grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); } }
    .big { display: flex; flex-direction: column; gap: 6px; padding: 26px 22px; border-radius: 22px; text-decoration: none; color: var(--fg); border: 2px solid var(--line); background: var(--surface); min-height: 180px; }
    .big strong { font-family: var(--display); font-size: 26px; }
    .big span:last-child { color: var(--muted); }
    .big.ww { border-color: var(--accent); }
    .big.wm { border-color: var(--correct); }
    .big.cm { border-color: var(--accent); }
    .big.en { border-color: var(--correct); }
    .big:hover { filter: brightness(0.98); }
    .emoji { font-size: 44px; }
    .center { text-align: center; }
    .hint { color: var(--muted); }
  `],
})
export class HubPage implements OnInit {
  player = inject(PlayerService);

  ngOnInit() {
    const saved = this.player.savedCode();
    if (saved && !this.player.profile()) {
      this.player.resume(saved).subscribe({ error: () => this.player.forget() });
    }
  }
}
