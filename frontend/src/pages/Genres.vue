<template>
  <q-page>
    <div
      class="container"
      v-if="getGenres"
    >
      <q-table
        grid
        title="Genres"
        :data="genres"
        :columns="columns"
        row-key="name"
        :filter="filter"
        hide-header
        class="table-container"
        :loading="loading"
        :pagination="pagination"
        :hide-pagination="(this.$q.platform.is.mobile) ? false : true"
      >
        <template v-slot:loading>
          <q-inner-loading showing color="primary" />
        </template>
        <template v-slot:top-right>
          <q-input borderless dense debounce="300" v-model="filter" placeholder="Search">
            <template v-slot:append>
              <q-icon name="search" color="white" />
            </template>
          </q-input>
        </template>
        <template v-slot:item="props">
          <q-badge outline rounded class="q-ma-sm q-pa-sm genre-link">
            <router-link :to="`genres/${props.row.slug}`">{{ props.row.name }}</router-link>
          </q-badge>
        </template>
      </q-table>
    </div>
  </q-page>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Genres',

  computed: {
    ...mapGetters([
      'getGenres'
    ]),
    genres () {
      return this.getGenres
    }
  },

  beforeMount () {
    this.loading = true

    const _this = this
    const params = {
      url: '/api/genres/',
      page: null,
      cb: () => {
        _this.loading = false
      }
    }
    this.$store.dispatch('loadItems', params)
  },

  data: function () {
    return {
      pagination: {
        rowsPerPage: (this.$q.platform.is.mobile) ? 15 : 1000
      },
      loading: false,
      filter: '',
      columns: [
        {
          name: 'name',
          required: true,
          field: row => row.name,
          format: val => `${val}`
        }
      ]
    }
  }
}
</script>

<style lang="scss">
.grid-style-transition {
  transition: transform .28s, background-color .28s
}

.table-container {
  background-color: #333;
  margin: 50px 1em 50px 1em;
  padding: 1em 1em 2em 1em;

  input {
    color: #fff;
  }
}

.q-table__title, .q-table__bottom--nodata {
  color: #fff;
}

.q-table__grid-item-value {
  text-align: center;
}

.q-table__bottom {
  color: white;

  span, i {
    color: white;
  }
}

.genre-link {
  background-color: darken($primary, 25);
  border-color: darken($primary, 5);
  a {
    color: #fff;
    font-size: 1.4em;
  }

  &:hover {
    background-color: darken($primary, 10);
    border-color: #ddd;
  }
}
</style>
