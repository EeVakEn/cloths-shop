<template>
  <p>
    <span v-for="item in this.categories.slice(0, -1)"
          :key="item.id"
    >
        <router-link
            class="v-breadcrumb__link"
            :to="item.id?{ name: 'category', params: {cat_slug:item.slug}}:{name: 'catalog'} "
        >
          {{ item.name }}
        </router-link>
    >
    </span>
    <b>{{ this.categories[this.categories.length - 1].name }}</b>
  </p>
</template>

<script>
export default {
  name: "v-breadcrumb",
  data() {
    return {
      categories: [
        {
          id: 0,
          name: 'Главная',
          slug: '',
          get_full_url: '/',
        },
      ]
    }
  },
  props: {
    categories_array: {
      type: Array,
      default() {
        return {}
      },
    },
  },
  mounted() {
    this.categories_array.forEach(category => this.categories.push(category))
  }
}
</script>

<style scoped>
.v-breadcrumb__link {
  text-decoration: none !important;
  cursor: pointer;
}
</style>