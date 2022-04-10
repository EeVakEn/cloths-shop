<template>
  <div id="app">
    <v-main-wrapper></v-main-wrapper>
  </div>
</template>

<script>

import VMainWrapper from "./components/v-main-wrapper";

export default {
  name: 'App',
  data(){
    return{
      cart:[],
      favorites:[],
    }
  },
  beforeCreate() {
    this.$store.commit('INIT_CART')
    this.$store.commit('INIT_FAVORITES')
  },
  mounted() {
    this.cart = this.$store.state.cart
    this.favorites = this.$store.state.favorites
  },
  components: {
    VMainWrapper
  }
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  margin-top: 80px;
}
</style>
