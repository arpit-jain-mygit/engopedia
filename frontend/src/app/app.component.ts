import { Component, inject } from '@angular/core';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';
import { PlayerService } from './core/player.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, RouterLink, RouterLinkActive],
  template: `
    <header class="top">
      <a routerLink="/" class="brand"><span aria-hidden="true">🧙</span> Word Wizard</a>
      <nav aria-label="Main">
        <a routerLink="/learn" routerLinkActive="on">📚 Learn</a>
        <a routerLink="/quiz" routerLinkActive="on">🎯 Quiz</a>
        <a routerLink="/shop" routerLinkActive="on">🛍️ Shop</a>
        <a routerLink="/leaderboard" routerLinkActive="on">🏆 Board</a>
      </nav>
      @if (player.profile(); as p) {
        <div class="wallet" aria-label="Your points and candies">
          <span class="pill star">⭐ {{ p.points }}</span>
          <span class="pill candy">🍬 {{ p.candies }}</span>
        </div>
      }
    </header>
    <main class="page">
      <router-outlet />
    </main>
  `,
  styles: [`
    .top { display: flex; align-items: center; gap: 12px; flex-wrap: wrap; padding: 12px 16px; max-width: 960px; margin: 0 auto; }
    .brand { font-family: var(--display); font-weight: 800; font-size: 20px; color: var(--fg); text-decoration: none; margin-right: auto; }
    nav { display: flex; gap: 6px; flex-wrap: wrap; }
    nav a { padding: 8px 12px; border-radius: 999px; color: var(--fg); text-decoration: none; font-weight: 600; min-height: 44px; display: inline-flex; align-items: center; }
    nav a.on, nav a:hover { background: var(--tile); }
    .wallet { display: flex; gap: 6px; }
    .page { max-width: 960px; margin: 0 auto; padding: 8px 16px 48px; }
  `],
})
export class AppComponent {
  player = inject(PlayerService);
}
