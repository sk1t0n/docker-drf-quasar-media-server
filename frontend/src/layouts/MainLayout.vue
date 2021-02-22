<template>
  <q-layout
    view="hHh LpR fff"
    class="background-dark quattrocento-font-regular"
  >
    <q-header class="header-dark text-white">
      <div class="container">
        <q-toolbar>
          <q-toolbar-title class="quattrocento-font-bold header-logo">
            {{ logoText }}
          </q-toolbar-title>

          <div class="gt-md top-menu">
            <router-link to="/" @click.native="linkClick">Home</router-link>
            <router-link to="/genres" @click.native="linkClick">Genres</router-link>
            <a href="/api/admin/media_server/genre/add/">Add genre</a>
            <a href="/api/admin/media_server/video/add/">Add video</a>
          </div>

          <q-btn
            dense
            icon="menu"
            size="16px"
            aria-label="Menu"
            @click="leftDrawerOpen = !leftDrawerOpen"
            class="lt-lg btn-top-menu"
          />
        </q-toolbar>
      </div>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      side="left"
      content-class="drawer-dark flex items-center"
    >
      <q-list class="text-center">
        <q-item-label
          header
          class="text-white"
        >
          Menu
        </q-item-label>
        <MobileMenu />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer class="footer-dark text-center ">
      <a :href="gitlabUrl">
        <q-icon size="64px" name="fab fa-gitlab" class="social-btn" />
      </a>
      <q-toolbar>
        <q-toolbar-title class="footer-logo">{{ logoText }}</q-toolbar-title>
      </q-toolbar>
      <p>Copyright &copy; {{ (new Date()).getFullYear() }}</p>
    </q-footer>
  </q-layout>
</template>

<script>
import MobileMenu from 'components/MobileMenu.vue'

const logoText = 'Media Server'

export default {
  name: 'MainLayout',

  components: { MobileMenu },

  data: () => ({
    leftDrawerOpen: false,
    logoText: logoText,
    gitlabUrl: 'https://gitlab.com/woolster'
  }),

  methods: {
    linkClick (e) {
      if (e.target.innerText.includes('Home')) {
        const params = {
          url: '/api/videos/',
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

<style lang="scss">
@import url('./../css/container.scss');

.background-dark {
  background-color: $background-dark;
}

.header-dark {
  background-color: $header-dark;
  height: 58px;
  padding-top: 4px;
}

@media screen and (min-width: 440px) {
  .header-logo {
    font-size: 30px;
    margin-left: 2rem;
  }
}

@media screen and (max-width: 439px) {
  .header-logo {
    font-size: 25px;
    margin-left: 2rem;
  }
}

@media screen and (max-width: 380px) {
  .header-logo {
    font-size: 20px;
    margin-left: 2rem;
  }
}

.top-menu a {
  margin-left: 10px;
  margin-right: 2rem;
}

.btn-top-menu {
  border: 1px solid rgba(255,255,255,.3);
  margin-right: 2rem;
}

.drawer-dark {
  background-color: $drawer-dark;

  .q-list {
    width: 100%;
  }
}

.footer-dark {
  background-color: $footer-dark;
  height: 230px;
  padding-top: 45px;
  font-size: 1rem;
}

.footer-logo {
  font-size: 1.7rem;
}

.social-btn {
  &:hover {
    color: $footer-social-hover;
  }
}

a {
  text-decoration: none;
  color: $top-menu-color;

  &:hover {
    color: $top-menu-hover-color;
  }
}

main {
  min-height: calc(100% - 58px - 230px) !important;
}
</style>
