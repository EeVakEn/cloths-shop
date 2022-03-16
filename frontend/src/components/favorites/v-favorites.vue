<template>

  <div class="v-favorites">
    <h1>Избранное</h1>
    <div v-if="FAVORITES.length">
      <div class="v-catalog__list">
        <v-favorite-item
            v-for="(item) in favorites_data"
            :key="item.article"
            :favorite_item_data="item"
            @addToCart="addToCart"
            @addToFavorites="addToFavorites"
        />
      </div>
    </div>
    <div v-else>
      <p>Вы пока что ничего не выбрали<br/>Но всегда это можно исправить<br/> Кликай на кнопочку снизу </p>
      <router-link :to="{name: 'catalog'}">
        <button class="dark-button">Перейти в каталог</button>
      </router-link>
    </div>

  </div>

</template>

<script>
import {mapGetters, mapActions} from "vuex";
import VFavoriteItem from "./v-favorite-item";

export default {
  name: "v-favorites",
  components: {VFavoriteItem},
  props: {
    favorites_data: {
      type: Array,
      default() {
        return []
      }
    }
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
  computed: {
    ...mapGetters([
      'FAVORITES'
    ])
  }

}
</script>

<style lang="scss">
</style>