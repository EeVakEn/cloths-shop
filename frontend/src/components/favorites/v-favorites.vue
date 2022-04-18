<template>

  <div class="v-favorites container-fluid">
    <h1>Избранное</h1>
    <div v-if="FAVORITES.length" class="container-fluid">
      <div class="row g-2" >
        <v-catalog-item
            class=" col-xl-3 col-lg-4 col-md-6 col-sm-12"
            v-for="product in FAVORITES"
            :key="product.article"
            :product_data="product"
            @addToCart="addToCart"
            @addToFavorites="addToFavorites"
        />
      </div>
    </div>
    <div v-else style="text-align: center">
      <p>Вы пока что ничего не выбрали<br/>Но всегда это можно исправить<br/> Кликай на кнопочку снизу </p>
      <router-link :to="{name: 'catalog'}">
        <button class="dark-button">Перейти в каталог</button>
      </router-link>
    </div>

  </div>

</template>

<script>
import {mapGetters, mapActions} from "vuex";
import VCatalogItem from "@/components/catalog/v-catalog-item";

export default {
  name: "v-favorites",
  components: {VCatalogItem},
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
  computed: {
    ...mapGetters([
      'FAVORITES'
    ])
  }

}
</script>

<style lang="scss">
</style>