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
      urlNextVideos: 'http://127.0.0.1:8080/api/videos/?page=1',
      urlPrevVideos: null,
      videos: [],
      video: {}
    },

    getters: {
      getCountVideos: state => state.countVideos,
      getUrlNextVideos: state => state.urlNextVideos,
      getUrlPrevVideos: state => state.urlPrevVideos,
      getVideos: state => state.videos,
      getVideo: state => state.video
    },

    mutations: {
      updateCountVideos (state, countVideos) {
        state.countVideos = countVideos
      },
      updateUrlNextVideos (state, url) {
        state.urlNextVideos = url
      },
      updateUrlPrevVideos (state, url) {
        state.urlPrevVideos = url
      },
      updateVideos (state, videos) {
        state.videos = videos
      },
      updateVideo (state, video) {
        state.video = video
      }
    },

    actions: {
      loadVideos (context, url) {
        if (!url) return
        const arr = url.split('?')
        url = arr[0]
        let page
        if (arr.length === 2 && arr[1].startsWith('page')) {
          page = arr[1].split('=')[1]
        } else {
          page = 1
        }
        axios.get(url, { params: { page: page } })
          .then(response => {
            if (response.status === 200) {
              context.commit('updateCountVideos', response.data.count)
              context.commit('updateUrlNextVideos', response.data.next)
              if (!response.data.previous || response.data.previous.includes('?page=')) {
                context.commit('updateUrlPrevVideos', response.data.previous)
              } else {
                context.commit('updateUrlPrevVideos', `${response.data.previous}?page=${page - 1}`)
              }
              context.commit('updateVideos', response.data.results)
            }
          })
          .catch(error => {
            console.log(error)
          })
      }
    },

    // enable strict mode (adds overhead!)
    // for dev mode only
    strict: process.env.DEV
  })

  return Store
}
