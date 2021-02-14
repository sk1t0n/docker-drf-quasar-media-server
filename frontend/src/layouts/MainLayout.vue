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
            <router-link
              v-for="item in topMenu"
              :key="item.title"
              :to="item.url"
            >
              {{ item.title }}
            </router-link>
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
        <MobileMenu
          v-for="item in topMenu"
          :key="item.title"
          :title="item.title"
          :url="item.url"
          class="text-white"
        />
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
const topMenu = [
  {
    title: 'Home',
    url: '/'
  },
  {
    title: 'Add genre',
    url: '/genre/add'
  },
  {
    title: 'Add video',
    url: '/video/add'
  }
]

export default {
  name: 'MainLayout',
  components: { MobileMenu },
  data () {
    return {
      leftDrawerOpen: false,
      topMenu: topMenu,
      logoText: logoText,
      gitlabUrl: 'https://gitlab.com/woolster'
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
</style>
