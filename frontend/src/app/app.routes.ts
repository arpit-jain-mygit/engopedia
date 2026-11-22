import { Routes } from '@angular/router';
import { HubPage } from './pages/hub.page';
import { HomePage } from './pages/home.page';
import { LearnListPage } from './pages/learn-list.page';
import { LearnRootPage } from './pages/learn-root.page';
import { QuizMapPage } from './pages/quiz-map.page';
import { QuizPlayPage } from './pages/quiz-play.page';
import { LeaderboardPage } from './pages/leaderboard.page';
import { ShopPage } from './pages/shop.page';
import { WmHomePage } from './pages/wm-home.page';
import { WmLearnListPage } from './pages/wm-learn-list.page';
import { WmLearnChapterPage } from './pages/wm-learn-chapter.page';
import { WmQuizMapPage } from './pages/wm-quiz-map.page';
import { WmQuizPlayPage } from './pages/wm-quiz-play.page';

export const routes: Routes = [
  // Study hub: two tiles, Word Wizard and Wren & Martin.
  { path: '', component: HubPage, title: 'Study Hub' },

  // Word Wizard (existing app, unchanged paths except its start page moved to /word-wizard).
  { path: 'word-wizard', component: HomePage, title: 'Word Wizard' },
  { path: 'learn', component: LearnListPage, title: 'Learn | Word Wizard' },
  { path: 'learn/:root', component: LearnRootPage, title: 'Learn | Word Wizard' },
  { path: 'quiz', component: QuizMapPage, title: 'Quiz | Word Wizard' },
  { path: 'quiz/:root', component: QuizPlayPage, title: 'Quiz | Word Wizard' },
  { path: 'leaderboard', component: LeaderboardPage, title: 'Board | Word Wizard' },
  { path: 'shop', component: ShopPage, title: 'Candy shop | Word Wizard' },

  // Wren & Martin Grammar: Learn, Quiz, Shop and Board. Shop and Board share the wizard's wallet and board.
  { path: 'wren-martin', component: WmHomePage, title: 'Wren & Martin | Study Hub' },
  { path: 'wren-martin/learn', component: WmLearnListPage, title: 'Learn | Wren & Martin' },
  { path: 'wren-martin/learn/:chapter', component: WmLearnChapterPage, title: 'Learn | Wren & Martin' },
  { path: 'wren-martin/quiz', component: WmQuizMapPage, title: 'Quiz | Wren & Martin' },
  { path: 'wren-martin/quiz/:chapter', component: WmQuizPlayPage, title: 'Quiz | Wren & Martin' },
  { path: 'wren-martin/shop', component: ShopPage, title: 'Candy shop | Wren & Martin' },
  { path: 'wren-martin/board', component: LeaderboardPage, title: 'Board | Wren & Martin' },

  { path: '**', redirectTo: '' },
];
