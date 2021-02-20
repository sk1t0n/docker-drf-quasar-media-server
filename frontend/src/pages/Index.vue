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
            <video width="100%" controls preload="metadata">
              <source :src="getVideoUrl(video.url)" :type="getVideoMIMEType(video.url)">
            </video>

            <q-card-section class="mycard-title">
              <router-link
                class="text-white"
                :to="{ name: 'videoDetail', params: { slug: video.slug }}"
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
              <router-link
                :to="{ name: 'videoDetail', params: { slug: video.slug }}"
              >
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

      <Pagination class="row" />
    </div>
  </q-page>
</template>

<script>
import { mapGetters } from 'vuex'
import Pagination from '../components/Pagination.vue'
import { getVideoUrl, getVideoMIMETypeFromUrl, filterDateFormat, filterTrim } from '../helpers'

export default {
  name: 'IndexPage',

  components: {
    Pagination
  },

  filters: {
    trim: filterTrim,
    realeaseDateFormat: filterDateFormat
  },

  computed: {
    ...mapGetters([
      'getVideos'
    ])
  },

  methods: {
    getGenreUrl: slug => `/genres/${slug}`,
    getVideoUrl: getVideoUrl,
    getVideoMIMEType: getVideoMIMETypeFromUrl
  }
}
</script>

<style lang="scss" scoped>
@import url('../css/video_list.scss');
</style>
