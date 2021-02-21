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
          url: 'http://127.0.0.1:8080/api/videos/',
          page: 1,
          cb: () => {}
        }
        this.$store.dispatch('loadItems', params)
        this.$store.commit('updateCurrentPage', 1)
      } else if (e.target.textContent === 'Add genre') {
        window.location.href = 'http://127.0.0.1:8080/api/admin/media_server/genre/add/'
      } else if (e.target.textContent === 'Add video') {
        window.location.href = 'http://127.0.0.1:8080/api/admin/media_server/video/add/'
      }
    }
  }
}
</script>
