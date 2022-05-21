<template>
  <div id="app">
    <v-main-wrapper></v-main-wrapper>
  </div>
</template>

<script>

import VMainWrapper from "./components/v-main-wrapper";
import axios from "axios";

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
    this.$store.commit('INIT_STORE')
    if (this.$store.state.token){
      axios.defaults.headers.common['Authorization'] = "Token " + this.$store.state.token
    } else {
      axios.defaults.headers.common['Authorization'] = ""
    }
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
@import url(https://fonts.googleapis.com/css?family=Montserrat:400,500,80);
#app {font-family: Montserrat, sans-serif;}
::-webkit-scrollbar{
  width: 8px;
}
::-webkit-scrollbar-track{
  background-color: rgba(0,0,0,0.2);
}
::-webkit-scrollbar-thumb{
  background-color: $dark-color;
  //border-radius: 5px;
}

</style>
