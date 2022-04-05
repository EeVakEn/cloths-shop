<template>
  <div>

    <span
        v-if="categories_array.length > 0"
        class="v-breadcrumb__link"
        @click="$router.push({name: 'catalog'})"
    >
      Главная
    </span>
    <span v-for="item in this.categories_array.slice(0, -1)"
          :key="item.id"
    >
      >
      <span
          class="v-breadcrumb__link"
          @click="$router.push({name:'category', params: {cat_slug:item.slug}}, $router.go())"
      >
        {{ item.name }}
      </span>
    </span>
    >
    <span class="v-breadcrumb__link">{{ this.categories_array[this.categories_array.length - 1].name }}</span>

  </div>
</template>

<script>
export default {
  name: "v-breadcrumb",
  props: {
    categories_array: {
      type: Array,
      default() {
        return {}
      },
    },
  },
  created() {
    console.log(this.categories_array)
  }
}
</script>

<style scoped>
.v-breadcrumb__link {
  text-decoration: none !important;
  cursor: pointer;
}
</style>