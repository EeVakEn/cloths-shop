<template>
  <div class="v-catalog">
    <div class="cart_favorites">
      <router-link class="cart_favorites__link" :to="{name:'favorites', params:{favorites_data: FAVORITES}}">
        <b-icon icon="heart"/>
        <span class="cart_favorites__count">{{ FAVORITES.length }}</span>
      </router-link>
      <router-link class="cart_favorites__link" :to="{name:'cart', params:{cart_data: CART}}">
        <b-icon icon="basket"/>
        <span class="cart_favorites__count">{{ getCartQuantity }}</span>
      </router-link>
    </div>


    <h1>Каталог</h1>
    <div class="v-catalog__list">
      <v-catalog-item
          v-for="product in PRODUCTS"
          :key="product.article"
          :product_data="product"
          :favorites_data="FAVORITES"
          @addToCart="addToCart"
          @addToFavorites="addToFavorites"
      />
    </div>
  </div>
</template>

<script>
import VCatalogItem from "./v-catalog-item";
import {mapActions, mapGetters} from 'vuex';

export default {
  name: "v-catalog",
  components: {VCatalogItem},
  data() {
    return {}
  },
  methods: {
    ...mapActions([
      'GET_PRODUCTS_FROM_API',
      'ADD_TO_CART',
      'ADD_TO_FAVORITES'
    ]),
    addToCart(data) {
      this.ADD_TO_CART(data);
    },
    addToFavorites(data) {
      this.ADD_TO_FAVORITES(data)
    }
  },
  mounted() {
    this.GET_PRODUCTS_FROM_API()
  },
  computed: {
    ...mapGetters([
      'PRODUCTS',
      'CART',
      'FAVORITES'
    ]),
    getCartQuantity: function () {
      let res = 0;
      for (let i = 0; i < this.CART.length; i++) {
        res += this.CART[i].quantity;
      }
      return res;
    }
  }
}
</script>

<style lang="scss">
.v-catalog {
  &__list {
    display: flex;
    flex-wrap: wrap;
    justify-content: start;
    align-items: center;
  }

}

.cart_favorites {
  position: fixed;
  display: flex;
  flex-wrap: wrap;
  top: 10px;
  right: 10px;

  &__link {
    font-size: 24px;
    text-decoration: none;
    color: $dark-color;
    padding: $padding;
  }

  &__link:hover {
    color: $dark-color;
  }

  &__count {
    display: inline-block;
    position: relative;
    top: -15px;
    right: 0;
    width: 15px;
    height: 15px;
    text-align: center;
    line-height: 15px;
    background: $dark-color;
    color: $second-color;
    border-radius: 50%;
    font-size: 11px;
  }


}
</style>