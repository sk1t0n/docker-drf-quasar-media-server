import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'

Vue.use(Vuex)

/*
 * If not building with SSR mode, you can
 * directly export the Store instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Store instance.
 */

export default function (/* { ssrContext } */) {
  const Store = new Vuex.Store({
    state: {
      countVideos: 0,
      videos: [],
      video: {},
      genres: [],
      genre: {},
      currentPage: 1
    },

    getters: {
      getCountVideos: state => state.countVideos,
      getVideos: state => state.videos,
      getVideo: state => state.video,
      getGenres: state => state.genres,
      getGenre: state => state.genre
    },

    mutations: {
      updateCountVideos (state, count) {
        state.countVideos = count
      },
      updateVideos (state, videos) {
        state.videos = videos
      },
      updateVideo (state, video) {
        state.video = video
      },
      updateGenres (state, genres) {
        state.genres = genres
      },
      updateGenre (state, genre) {
        state.genre = genre
      },
      updateCurrentPage (state, currentPage) {
        state.currentPage = currentPage
      }
    },

    actions: {
      loadItems (context, { url, page, cb }) {
        const params = (page > 1) ? { params: { page: page } } : {}
        axios.get(url, params)
          .then(response => {
            if (response.status === 200) {
              if (url.includes('/videos/')) {
                context.commit('updateCountVideos', response.data.count)
                context.commit('updateVideos', response.data.results)
              } else {
                context.commit('updateGenres', response.data)
              }
            }
            cb()
          })
          .catch(error => {
            if (error.response.status === 404) {
              this.$router.push({ path: '/404' })
            }
            cb()
          })
      },

      loadItem (context, { url, cb }) {
        axios.get(url)
          .then(response => {
            if (response.status === 200) {
              if (url.includes('/videos/')) {
                context.commit('updateVideo', response.data)
              } else {
                context.commit('updateGenre', response.data)
              }
            }
            cb()
          })
          .catch(error => {
            if (error.response.status === 404) {
              this.$router.push({ path: '/404' })
            }
            cb()
          })
      }
    },

    // enable strict mode (adds overhead!)
    // for dev mode only
    strict: process.env.DEV
  })

  return Store
}
