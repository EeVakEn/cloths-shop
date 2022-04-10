<template>
  <div class="v-catalog">
    <div class="cart_favorites">
      <router-link class="cart_favorites__link" :to="{name:'favorites', params:{favorites_data: FAVORITES}}">
        <i class="bi bi-heart"></i>
        <span class="cart_favorites__count">{{ FAVORITES.length }}</span>
      </router-link>
      <router-link class="cart_favorites__link" :to="{name:'cart', params:{cart_data: CART}}">
        <i class="bi bi-bag"></i>
        <span class="cart_favorites__count">{{ getCartQuantity }}</span>
      </router-link>
    </div>

    <h2>Каталог</h2>

    <v-breadcrumb v-if="isFetching" :categories_array='BREADCRUMB'/>

    <div v-if="isFetching" class="v-catalog__list">
      <v-catalog-item
          v-for="product in PRODUCTS"
          :key="product.article"
          :product_data="product"
          @addToFavorites="addToFavorites"
      />
    </div>
  </div>
</template>

<script>
import VCatalogItem from "./v-catalog-item";
import {mapActions, mapGetters} from 'vuex';
import VBreadcrumb from "@/components/catalog/v-breadcrumb";

export default {
  name: "v-catalog",
  components: {VBreadcrumb, VCatalogItem},
  data() {
    return {
      isFetching: false,
    }
  },
  methods: {
    ...mapActions([
      'GET_PRODUCTS_FROM_API',
      'GET_PRODUCTS_WITH_CATEGORY',
      'GET_BREADCRUMB',
      'GET_CATEGORY_BREADCRUMB',
      'ADD_TO_FAVORITES'
    ]),
    addToFavorites(data) {
      this.ADD_TO_FAVORITES(data)
    },
  },
  mounted() {
    if (this.$route.params.cat_slug) {
      this.GET_PRODUCTS_WITH_CATEGORY(this.$route.params.cat_slug)
      this.GET_CATEGORY_BREADCRUMB(this.$route.params.cat_slug)
    } else {
      this.GET_PRODUCTS_FROM_API()
      this.GET_BREADCRUMB()
    }
    this.isFetching = true
  },
  computed: {
    ...mapGetters([
      'PRODUCTS',
      'CART',
      'FAVORITES',
      'BREADCRUMB',
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
  margin: 30px;

  &__list {
    display: grid;
    grid-template-columns: repeat(auto-fill, 300px);
    justify-content: center;
    grid-gap: 10px;
  }

}

.cart_favorites {
  position: fixed;
  display: flex;
  flex-wrap: wrap;
  top: 10px;
  right: 20px;

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