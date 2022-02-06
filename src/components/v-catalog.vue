<template>
  <div class="v-catalog">
    <h1>Catalog</h1>
    <div class="v-catalog__list">
      <v-catalog-item/>
    </div>
  </div>
</template>

<script>
import VCatalogItem from "./v-catalog-item";
export default {
  name: "v-catalog",
  components: {VCatalogItem}
}
</script>

<style lang="scss">
  .v-catalog{
    &__list{
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
     }
  }
</style>