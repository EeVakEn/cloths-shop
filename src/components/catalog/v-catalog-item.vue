<template>
  <div class="v-catalog-item">
    <div class="v-catalog-item__image-wrapper">
      <img class="v-catalog-item__image" :src=" require('../../assets/images/products/' + product_data.image)"
           :alt="product_data.image">
    </div>

    <p class="v-catalog-item__name">{{ product_data.name }}</p>
    <p class="v-catalog-item__description">{{ product_data.description }}</p>
    <div class="v-catalog-item__bottom">
      <span class="v-catalog-item__price">{{ getFormattedPrice }} ₽</span>
      <b-button-group class="v-catalog-item__btn-grp">
        <b-button class="v-catalog-item__btn-grp__btn" @click="addToCart">
          В корзину
          <b-icon icon="basket" scale="1"/>
        </b-button>
        <b-button class="v-catalog-item__btn-grp__btn" @click="addToFavorites">
          <b-icon v-if="product_data.isFavorite" icon="heart-fill" scale="1"/>
          <b-icon v-else icon="heart" scale="1"/>
        </b-button>
      </b-button-group>
    </div>

  </div>
</template>

<script>
export default {
  name: "v-catalog-item",
  props: {
    product_data: {
      type: Object,
      default() {
        return {}
      },
    },
    favorites_data: {
      type: Array,
      default() {
        return [];
      }
    }
  },
  methods: {
    addToCart() {
      this.$emit('addToCart', this.product_data)
    },
    addToFavorites() {
      this.$emit('addToFavorites', this.product_data)
    },

  },
  mounted() {
    this.$set(this.product_data, 'quantity', 1)
    this.$set(this.product_data, 'isFavorite', false)
  },
  computed: {
    getFormattedPrice: function () {
      return this.product_data.price.toLocaleString()
    },
  }
}
</script>

<style lang="scss">
.v-catalog-item {
  display: flex;
  flex-direction: column;
  margin: $margin*0.5;
  background-color: $second-color;
  width: 300px;
  height: 500px;
  &__image-wrapper{
    width: 100%;
    height: 350px;
  }
  &__name {
    padding: $padding;
    text-align: left;
    font-weight: bold;
    margin-bottom: 0;
  }

  &__description {
    padding: 0 $padding;
    text-align: left;
    height: 50px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  &__bottom{
    position: relative;
    display: block;
    bottom: $padding;
  }
  &__price {
    line-height: 20px;
    font-size: 20px;
    font-weight: bold;
    padding-right: $padding*2;
  }

  &__btn-grp {
    width: 180px;

    &__btn {
      background-color: $dark-color !important;
      border-radius: 0 !important;
    }
  }

  &__image {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
}
</style>