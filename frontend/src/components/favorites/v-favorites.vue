<template>

  <div class="container-fluid ">
    <div class="v-favorites">
      <div v-if="FAVORITES.length">
        <h2>Избранное</h2>
        <div class="row g-2">
            <v-catalog-item
                class="col-xl-3 col-lg-4 col-md-6 col-sm-12"
                v-for="product in FAVORITES"
                :key="product.article"
                :product_data="product"
                @addToCart="addToCart"
                @addToFavorites="addToFavorites"
            />

        </div>
      </div>
      <div v-else style="text-align: center">
        <h2>Избранное</h2>
        <i style="font-size: 25vw; padding: 30px 0" class="fa fa-heart-crack"></i>
<!--        <img class="link-img" src="@/assets/images/broken-heart-svgrepo-com.svg" alt="" style="max-width: 400px"/>-->
        <p>Вы пока что ничего не выбрали<br/>Но всегда это можно исправить<br/> Кликай на кнопочку снизу </p>
        <button @click="$router.push('/').catch(()=>{})" class="dark-button">Перейти в каталог</button>
      </div>
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
      this.$toasted.show('Товар удален из избранного')
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
.v-favorites{
  margin: 30px 60px;
}
</style>