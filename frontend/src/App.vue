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
      cart:[]
    }
  },
  beforeCreate() {
    this.$store.commit('INIT_STORE')
  },
  mounted() {
    this.cart = this.$store.state.cart
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
