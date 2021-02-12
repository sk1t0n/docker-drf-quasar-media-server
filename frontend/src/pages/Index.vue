<template>
  <q-page class="flex flex-center">
    <img
      alt="Quasar logo"
      src="~assets/quasar-logo-full.svg"
      @click="onClick"
    >
  </q-page>
</template>

<script>
export default {
  name: 'PageIndex',

  data: () => ({
    videos: []
  }),

  methods: {
    async onClick () {
      const url = 'http://172.35.0.5/api/videos/'
      const res = await this.$axios.get(url)
      console.log(res.data)
    }
  }
}
</script>
