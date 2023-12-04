import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/searchbyid',
    name: 'SingleAccountById',
    component: () => import(/* webpackChunkName: "about" */ '../components/SingleAccountById.vue')
  },
  {
    path: '/',
    name: 'SearchResults',
    component: () => import(/* webpackChunkName: "about" */ '../components/TimelineStatuses.vue')
  }
]

const router = createRouter({
  history: createWebHistory('/tools/mastodon'),
  routes: routes,
});

export default router
