<template>
  <div>
    <router-link to="/" @click.native="linkClick">
      <q-item tag="a">
        <q-item-section>
          <q-item-label class="text-white">Home</q-item-label>
        </q-item-section>
      </q-item>
    </router-link>
    <router-link to="/genres">
      <q-item tag="a">
        <q-item-section>
          <q-item-label class="text-white">Genres</q-item-label>
        </q-item-section>
      </q-item>
    </router-link>
    <q-item tag="a" @click.native="linkClick">
      <q-item-section>
        <q-item-label class="text-white">Add genre</q-item-label>
      </q-item-section>
    </q-item>
    <q-item tag="a" @click.native="linkClick">
      <q-item-section>
        <q-item-label class="text-white">Add video</q-item-label>
      </q-item-section>
    </q-item>
  </div>
</template>

<script>
export default {
  name: 'MobileMenu',

  methods: {
    linkClick (e) {
      if (e.target.textContent === 'Home') {
        const params = {
          url: '/api/videos/',
          page: 1,
          cb: () => {}
        }
        this.$store.dispatch('loadItems', params)
        this.$store.commit('updateCurrentPage', 1)
      } else if (e.target.textContent === 'Add genre') {
        const url = '/api/admin/media_server/genre/add/'
        window.location.href = url
      } else if (e.target.textContent === 'Add video') {
        const url = '/api/admin/media_server/video/add/'
        window.location.href = url
      }
    }
  }
}
</script>
