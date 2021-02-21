<template>
  <q-page>
    <div class="container">
      <h3 class="flex flex-center q-my-sm text-blue-grey-4">{{ genreName }}</h3>
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
                @click.native="clickGenre"
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

      <Pagination class="row" :slug="slug" :key="paginationKey" />
    </div>
  </q-page>
</template>

<script>
import { mapGetters } from 'vuex'
import Pagination from '../components/Pagination.vue'
import { getVideoUrl, getVideoMIMETypeFromUrl, filterDateFormat, filterTrim } from '../helpers'

export default {
  name: 'GenrePage',

  components: {
    Pagination
  },

  computed: {
    ...mapGetters([
      'getGenre',
      'getVideos'
    ])
  },

  data: function () {
    return {
      slug: this.$route.path.split('/')[2],
      paginationKey: 1,
      genreName: (this.getGenre) ? this.getGenre.name : ''
    }
  },

  beforeMount () {
    const _this = this
    const params = {
      url: `http://127.0.0.1:8080/api/genres/${this.slug}`,
      page: null,
      cb: () => {
        _this.genreName = _this.getGenre.name
      }
    }
    this.$store.dispatch('loadItem', params)
  },

  filters: {
    trim: filterTrim,
    realeaseDateFormat: filterDateFormat
  },

  methods: {
    getGenreUrl: slug => `/genres/${slug}`,
    getVideoUrl: getVideoUrl,
    getVideoMIMEType: getVideoMIMETypeFromUrl,
    clickGenre (e) {
      const linkSlug = e.target.pathname.split('/')[2]
      if (this.slug !== linkSlug) {
        this.slug = linkSlug
        this.genreName = e.target.innerText
        this.paginationKey++
      }
    }
  }
}
</script>

<style lang="scss" scoped>
@import url('../css/video_list.scss');
</style>
