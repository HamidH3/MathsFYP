import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../src/components/HomePage.vue' 
// import GamePage from '../src/components/GamePage.vue' 
import LeaderboardPage from '../src/components/LeaderboardPage.vue'

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage
  },
//   {
//     path: '/game',
//     name: 'GamePage',
//     component: GamePage
//   },
  {
    path:'/leaderboard',
    name:'LeaderboardPage',
    component:LeaderboardPage
  }
]

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL || '/'),
    routes,
  });
  

export default router