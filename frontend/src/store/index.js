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
      countGenres: 0,
      genres: [],
      genre: {},
      currentPage: 1
    },

    getters: {
      getCountVideos: state => state.countVideos,
      getVideos: state => state.videos,
      getVideo: state => state.video,
      getCountGenres: state => state.countGenres,
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
      updateCountGenres (state, count) {
        state.countGenres = count
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
      loadItems (context, { type, page, cb }) {
        type = type.toLowerCase()
        const url = `http://127.0.0.1:8080/api/${type}s/`
        axios.get(url, { params: { page: page } })
          .then(response => {
            if (response.status === 200) {
              const title = type.charAt(0).toUpperCase() + type.substr(1)
              context.commit(`updateCount${title}s`, response.data.count)
              context.commit(`update${title}s`, response.data.results)
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
