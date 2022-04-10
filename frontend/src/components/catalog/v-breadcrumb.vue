<template>
  <p>
    <router-link
        class="v-breadcrumb__link"
        :to="{ name: 'catalog'}"
    >
      Главная
    </router-link>
    <span v-for="item in categories_array"
          :key="item.id"
    >
      <i class="bi bi-chevron-right"></i>
      <router-link
          class="v-breadcrumb__link"
          :to="{ name: 'category', params: {cat_slug:item.slug}} "
      >
        {{ item.name }}
      </router-link>
    </span>
  </p>
</template>

<script>
export default {
  name: "v-breadcrumb",
  props: {
    categories_array: {
      type: Array,
      default() {
        return []
      },
    },
  },
}
</script>

<style scoped>
.v-breadcrumb__link {
  text-decoration: none !important;
  cursor: pointer;
}
</style>