<template>
  <div class="v-catalog-item">
    <div class="v-catalog-item__image-wrapper">
      <img class="v-catalog-item__image" :src=" require('../../assets/images/products/' + favorite_item_data.image)"
           :alt="favorite_item_data.image">
    </div>

    <p class="v-catalog-item__name">{{ favorite_item_data.name }}</p>
    <p class="v-catalog-item__description">{{ favorite_item_data.description }}</p>
    <div class="v-catalog-item__bottom">
      <span class="v-catalog-item__price">{{ getFormattedPrice }} ₽</span>
      <b-button-group class="v-catalog-item__btn-grp">
        <b-button class="v-catalog-item__btn-grp__btn" @click="addToCart">
          В корзину
          <b-icon icon="basket" scale="1"/>
        </b-button>
        <b-button class="v-catalog-item__btn-grp__btn" @click="addToFavorites">
          <b-icon v-if="favorite_item_data.isFavorite" icon="heart-fill" scale="1"/>
          <b-icon v-else icon="heart" scale="1"/>
        </b-button>
      </b-button-group>
    </div>
  </div>
</template>

<script>
export default {
  name: "v-favorite-item",
  props: {
    favorite_item_data: {
      type: Object,
      default() {
        return {}
      }
    }
  },
  methods: {
    addToCart() {
      this.$emit('addToCart', this.favorite_item_data)
    },
    addToFavorites() {
      this.$emit('addToFavorites', this.favorite_item_data);
      this.favorite_item_data.isFavorite = !this.favorite_item_data.isFavorite;
    }
  },
  computed: {
    getFormattedPrice: function () {
      return this.favorite_item_data.price.toLocaleString()
    }
  }
}
</script>

<style>

</style>