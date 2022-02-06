<template>
  <div class="v-catalog-item">
    <img src="" alt="img">
    <p>Item 1</p>
    <p>Price:100</p>
    <button>Add to cart</button>
  </div>
</template>

<script>
export default {
  name: "v-catalog-item"
}
</script>

<style lang="scss">
  .v-catalog-item{
    flex-basis: 25%;
    box-shadow: 0 0 8px 0 $main-color;
    padding: $padding*2;
    margin-bottom: $margin*2;
  }
</style>