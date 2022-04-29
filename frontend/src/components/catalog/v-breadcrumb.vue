<template>
  <p>
    <span
        class="v-breadcrumb__link"
        @click = "$router.push('/').catch(()=>{})"
    >
      Главная
    </span>
    <span v-for="item in categories_array"
          :key="item.id"
    >
      <i class="bi bi-chevron-right"></i>
      <span
          class="v-breadcrumb__link"
          @click="$router.push(`/category/${item.slug}`)"
      >
        {{ item.name }}
      </span>
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