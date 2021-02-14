<template>
  <q-page>
    <div class="container">
      <div class="row">
        <div
          class="col-lg-4 col-md-6 col-sm-12 col-xs-12 q-pa-md"
          v-for="video in getVideos"
          :key="video.id"
        >
          <q-card
            flat
            bordered
            square
            class="mycard"
          >
            <video width="100%" controls>
              <source :src="video.url | videoUrlByExtension('webm')" type="video/webm">
              <source :src="video.url | videoUrlByExtension('mp4')" type="video/mp4">
            </video>

            <q-card-section class="mycard-title">
              <router-link
                class="text-white"
                :to="getVideoPageUrl(video.slug)"
              >
                {{ video.title }}
              </router-link>
            </q-card-section>

            <q-card-section class="mycard-field">
              Genres:
              <router-link
                v-for="genre in video.genres"
                :key="genre.id"
                :to="getGenreUrl(genre.slug)"
              >
                {{ genre.name }}
              </router-link>
              <span v-if="video.genres.length === 0">no</span>
            </q-card-section>

            <q-card-section class="mycard-field">
              Release date: {{ video.release_date | realeaseDateFormat }}
            </q-card-section>

            <q-card-section class="mycard-field">
              Runtime: {{ video.runtime }} min
              <div class="hr" />
            </q-card-section>

            <q-card-section class="mycard-summary">
              {{ video.description | trim }}
            </q-card-section>

            <q-card-section>
              <router-link :to="getVideoPageUrl(video.slug)">
                <q-btn
                  label="Read more"
                  size="16px"
                  class="btn-read-more text-white"
                  no-caps
                  unelevated
                  padding="8px 20px"
                />
              </router-link>
            </q-card-section>
          </q-card>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
import { mapGetters } from 'vuex'

import filterVideoUrlByExtension from '../helpers'

export default {
  name: 'PageIndex',

  components: {
    //
  },

  filters: {
    videoUrlByExtension: filterVideoUrlByExtension,

    trim (value) {
      if (value.length > 200) {
        return value.slice(0, 200) + ' ...'
      }
      return value
    },

    realeaseDateFormat (value) {
      const language = window.navigator.language
      const arr = value.split('-')
      if (language === 'ru-RU') {
        return `${arr[2]}.${arr[1]}.${arr[0]}`
      } else if (language === 'en-US') {
        return `${arr[1]}/${arr[2]}/${arr[0]}`
      } else {
        return `${arr[2]}/${arr[1]}/${arr[0]}`
      }
    }
  },

  computed: {
    ...mapGetters([
      'getVideos',
      'getUrlNextVideos'
    ])
  },

  beforeMount () {
    this.$store.dispatch('loadVideos', this.getUrlNextVideos)
  },

  methods: {
    getVideoPageUrl: slug => `/videos/${slug}`,
    getGenreUrl: slug => `/genres/${slug}`
  }
}
</script>

<style lang="scss" scoped>
.mycard {
  background-color: $card-background;
  color: $card-text-color;

  a:hover {
    color: $card-header-hover-text-color !important;
    cursor: pointer;
  }

  .mycard-title {
    font-size: 1.3rem;
  }

  .mycard-field {
    margin-top: -25px;
    margin-bottom: -30px;
    font-size: 1rem;
  }

  .hr {
    border-top: 1px solid $grey-8;
    margin-top: 10px;
    margin-bottom: 10px;
  }

  .mycard-summary {
    font-size: 0.9rem;
    margin-bottom: -15px;
  }

  .btn-read-more {
    border: 1px solid $card-btn-border-color;
    border-radius: 0px;
    font-size: 14px !important;

    &:hover {
      background-color: $card-btn-hover-bg !important;
      border-color: $card-btn-hover-bg;
    }
  }
}
</style>
