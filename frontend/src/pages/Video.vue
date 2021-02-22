<template>
  <q-page>
    <div class="container">
      <div class="row">
        <div class="col-lg-8 offset-lg-2 q-pa-md">
          <div v-if="video">
            <h4 id="videoTitle" class="title">{{ video.title }}</h4>

            <video width="100%" controls class="q-my-lg" preload="none">
              <source id="srcVideo" src="1.mp4" type="video/mp4">
            </video>

            <div class="field field-text-size">
              <span>Release date: </span>
              <span>{{ video.release_date | realeaseDateFormat }}</span>
            </div>

            <div class="field field-text-size"><span>Runtime: </span><span>{{ video.runtime }}</span></div>

            <p class="field">{{ video.description }}</p>

            <div class="text-center">
              <q-chip
                v-for="genre in video.genres"
                :key="genre.id"
                :ref="genre.id"
              >
                <a
                  :href="getGenreUrl(genre.slug)"
                  @mouseover="btnGenreOver(genre.id)"
                  @mouseleave="btnGenreLeave(genre.id)"
                >
                  {{ genre.name }}
                </a>
              </q-chip>
            </div>
          </div>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
import { mapState } from 'vuex'
import { getVideoMIMETypeFromUrl, filterDateFormat } from '../helpers'

export default {
  name: 'Video',

  data: function () {
    return {
      show: false,
      slug: this.$route.path.split('/')[2]
    }
  },

  beforeMount () {
    this.$q.loading.show()

    const _this = this
    const cb = () => {
      const interval = setInterval(changeVideo, 100)

      function changeVideo () {
        if (document.getElementById('srcVideo')) {
          const srcVideo = document.getElementById('srcVideo')
          srcVideo.src = `media/${_this.video.url}`
          srcVideo.type = _this.getVideoMIMEType(_this.video.url)
          srcVideo.parentElement.load()
          _this.$q.loading.hide()
          _this.show = true
          clearInterval(interval)
        }
      }
    }

    const params = {
      url: `/api/videos/${this.slug}`,
      cb: cb
    }
    this.$store.dispatch('loadItem', params)
  },

  filters: {
    realeaseDateFormat: filterDateFormat
  },

  methods: {
    getGenreUrl: slug => `genres/${slug}`,
    btnGenreOver (id) {
      this.$refs[id][0].$el.classList.add('animated')
      this.$refs[id][0].$el.classList.add('pulse')
    },
    btnGenreLeave (id) {
      this.$refs[id][0].$el.classList.remove('animated')
      this.$refs[id][0].$el.classList.remove('pulse')
    },
    getVideoMIMEType: getVideoMIMETypeFromUrl
  },

  computed: {
    ...mapState({
      video: state => state.video
    })
  }
}
</script>

<style lang="scss" scoped>
.title {
  color: $video-page-title;
  font-size: 2rem;
  margin-bottom: 0px;
  text-align: center;
}

.q-chip {
  background-color: $video-page-bg-genre;
  margin: 30px 10px 0px 10px;
}

a {
  color: white;
  margin-top: -2px;

  &:hover {
    color: black;
    cursor: pointer;
  }
}

.field {
  color: $video-page-text;
  font-size: 1rem;
  margin-bottom: 5px;

  span:first-child {
    color: $video-page-title;
  }
  span:last-child {
    color: $video-page-bg-genre;
  }
}

.field-text-size {
  font-size: 1.2rem;
}

p {
  text-align: justify;
}

@media screen and (max-width: 991px) {
  #videoTitle {
    margin-top: 0.5em;
    font-size: 1.8em;
  }
}
</style>
