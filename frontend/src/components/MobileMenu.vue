<template>
  <router-link :to="url" @click.native="linkClick">
    <q-item tag="a">
      <q-item-section>
        <q-item-label>{{ title }}</q-item-label>
      </q-item-section>
    </q-item>
  </router-link>
</template>

<script>
export default {
  name: 'MobileMenu',

  props: {
    title: {
      type: String,
      required: true
    },
    url: {
      type: String,
      default: '#'
    }
  },

  methods: {
    linkClick (e) {
      if (e.target.innerText.includes('Home')) {
        const params = {
          type: 'video',
          page: 1,
          cb: () => {}
        }
        this.$store.dispatch('loadItems', params)
        this.$store.commit('updateCurrentPage', 1)
      }
    }
  }
}
</script>
