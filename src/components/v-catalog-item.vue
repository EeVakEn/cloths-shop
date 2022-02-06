<template>
  <div class="v-catalog-item">
    <img class="v-catalog-item__image" :src=" require('../assets/images/' + product_data.image)" :alt="product_data.image">
    <p class="v-catalog-item__name">{{product_data.name}}</p>
    <p class="v-catalog-item__price">{{product_data.price}} ₽</p>
    <b-button
        variant="success"
        class="v-catalog-item__add-cart-btn btn"
        @click="addToCart"
    >
      Add to cart
    </b-button>
  </div>
</template>

<script>
export default {
  name: "v-catalog-item",
  props:{
    product_data:{
      type: Object,
      default() {
        return{}
      },
    }
  },
  methods:{
    addToCart(){
      this.$emit('sendArticle', this.product_data.article)
    }
  }
}
</script>

<style lang="scss">
  .v-catalog-item{
    flex-basis: 25%;
    box-shadow: 0 0 10px 0 $main-color;
    padding: $padding*2;
    margin-bottom: $margin*2;
    background-color: $second-color;
    border-radius: $radius*4;
    &__image{
      width: 300px;
    }
  }
</style>