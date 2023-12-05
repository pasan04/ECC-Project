import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'SearchResults',
    component: () => import(/* webpackChunkName: "about" */ '../components/SearchResults.vue')
  }
]

const router = createRouter({
  history: createWebHistory('/tools/prediction'),
  routes: routes,
});

export default router
