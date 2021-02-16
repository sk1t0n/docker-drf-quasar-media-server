<template>
  <transition name="fade">
    <div v-if="show" class="flex flex-center">
      <q-pagination
        :value="currentPage"
        @input="loadData"
        :max="pages"
        :max-pages="5"
        :direction-links="true"
        :boundary-links="true"
      />
    </div>
  </transition>
</template>

<script>
import { mapGetters, mapState } from 'vuex'

export default {
  name: 'Pagination',

  props: {
    itemType: {
      type: String,
      required: true
    }
  },

  data: () => ({
    pages: 1,
    limitVideos: 6,
    limitGenres: 20,
    show: false
  }),

  computed: {
    ...mapGetters([
      'getCountVideos',
      'getCountGenres'
    ]),
    ...mapState({
      currentPage: state => state.currentPage
    })
  },

  beforeMount () {
    this.$q.loading.show()

    const _this = this
    const cb = () => {
      if (_this.itemType.toLowerCase() === 'video') {
        _this.pages = Math.ceil(_this.getCountVideos / _this.limitVideos)
      } else {
        _this.pages = Math.ceil(_this.getCountGenres / _this.limitGenres)
      }
      _this.$q.loading.hide()
      _this.show = true
    }

    if (this.$route.fullPath.includes('?page=')) {
      const paramPage = Number(this.$route.query.page)
      this.$store.commit('updateCurrentPage', paramPage)
    }
    const params = {
      type: this.itemType,
      page: this.currentPage,
      cb: cb
    }
    this.$store.dispatch('loadItems', params)
  },

  methods: {
    loadData (currPage) {
      this.$store.commit('updateCurrentPage', currPage)

      if (this.$route.fullPath.includes('?page=') &&
          currPage === Number(this.$route.query.page)) {
        return
      }

      const params = {
        type: this.itemType,
        page: currPage,
        cb: () => {}
      }
      this.$store.dispatch('loadItems', params)
      this.$router.push({ path: `/?page=${currPage}` })
    }
  }
}
</script>

<style lang="scss">
@media screen and (max-width: 767px) {
  .q-pagination {
    padding-top: 12px;
    padding-bottom: 24px;
  }
}

@media screen and (min-width: 768px) {
  .q-pagination {
    padding-top: 24px;
    padding-bottom: 24px;
  }
}

.no-wrap {
  flex-wrap: wrap;
  justify-content: center;
}

.q-pagination {
  .bg-primary {
    background-color: $pagination-btn-active !important;
  }

  .text-primary {
    color: $pagination-btn-text-color !important;
  }

  .q-btn {
    border-radius: 0px;
    width: 35px;
    height: 35px;
    margin: 5px;
    background-color: $pagination-btn;
    color: white;

    &:hover {
      background-color: $pagination-btn-hover;
    }
  }
}

.fade-enter-active {
  transition: opacity 1s;
}

.fade-enter {
  opacity: 0;
}
</style>
