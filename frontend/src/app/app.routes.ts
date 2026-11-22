import { Routes } from '@angular/router';
import { HomePage } from './pages/home.page';
import { LearnListPage } from './pages/learn-list.page';
import { LearnRootPage } from './pages/learn-root.page';
import { QuizMapPage } from './pages/quiz-map.page';
import { QuizPlayPage } from './pages/quiz-play.page';
import { LeaderboardPage } from './pages/leaderboard.page';
import { ShopPage } from './pages/shop.page';

export const routes: Routes = [
  { path: '', component: HomePage, title: 'Word Wizard' },
  { path: 'learn', component: LearnListPage, title: 'Learn | Word Wizard' },
  { path: 'learn/:root', component: LearnRootPage, title: 'Learn | Word Wizard' },
  { path: 'quiz', component: QuizMapPage, title: 'Quiz | Word Wizard' },
  { path: 'quiz/:root', component: QuizPlayPage, title: 'Quiz | Word Wizard' },
  { path: 'leaderboard', component: LeaderboardPage, title: 'Leaderboard | Word Wizard' },
  { path: 'shop', component: ShopPage, title: 'Candy shop | Word Wizard' },
  { path: '**', redirectTo: '' },
];
