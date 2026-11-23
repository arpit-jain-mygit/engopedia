import { Component, inject, signal } from '@angular/core';
import { NavigationEnd, Router, RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';
import { filter } from 'rxjs';
import { PlayerService } from './core/player.service';

type Section = 'hub' | 'word-wizard' | 'wren-martin';

interface NavItem {
  label: string;
  link: string;
}

const NAV: Record<Exclude<Section, 'hub'>, NavItem[]> = {
  'word-wizard': [
    { label: '📚 Learn', link: '/learn' },
    { label: '🎯 Quiz', link: '/quiz' },
    { label: '🛍️ Shop', link: '/shop' },
    { label: '🏆 Board', link: '/leaderboard' },
  ],
  'wren-martin': [
    { label: '📚 Learn', link: '/wren-martin/learn' },
    { label: '🎯 Quiz', link: '/wren-martin/quiz' },
    { label: '✍️ Tests', link: '/wren-martin/tests' },
    { label: '🛍️ Shop', link: '/wren-martin/shop' },
    { label: '🏆 Board', link: '/wren-martin/board' },
  ],
};

const BRAND: Record<Section, string> = {
  hub: '✨ Study Hub',
  'word-wizard': '🧙 Word Wizard',
  'wren-martin': '📖 Wren & Martin',
};

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, RouterLink, RouterLinkActive],
  template: `
    <header class="top">
      <a routerLink="/" class="brand">{{ brand() }}</a>
      @if (section() !== 'hub') {
        <nav [attr.aria-label]="brand() + ' menu'">
          @for (item of nav(); track item.link) {
            <a [routerLink]="item.link" routerLinkActive="on">{{ item.label }}</a>
          }
        </nav>
      }
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
  private router = inject(Router);
  section = signal<Section>(this.sectionFor(this.router.url));

  constructor() {
    this.router.events
      .pipe(filter((e): e is NavigationEnd => e instanceof NavigationEnd))
      .subscribe((e) => this.section.set(this.sectionFor(e.urlAfterRedirects)));
  }

  brand() {
    return BRAND[this.section()];
  }

  nav() {
    const s = this.section();
    return s === 'hub' ? [] : NAV[s];
  }

  private sectionFor(url: string): Section {
    const path = url.split(/[?#]/)[0];
    if (path === '/' || path === '') return 'hub';
    return path.startsWith('/wren-martin') ? 'wren-martin' : 'word-wizard';
  }
}
