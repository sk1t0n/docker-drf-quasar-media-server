
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') },
      {
        path: '/videos/:slug',
        name: 'videoDetail',
        component: () => import('pages/Video.vue'),
        props: true
      },
      {
        path: '/genres',
        component: () => import('pages/Genres.vue')
      },
      {
        path: '/genres/:slug',
        name: 'genreDetail',
        component: () => import('pages/Genre.vue'),
        props: true
      }
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
