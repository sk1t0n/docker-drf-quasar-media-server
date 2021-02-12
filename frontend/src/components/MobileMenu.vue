<template>
  <router-link :to="url">
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
  }
}
</script>
