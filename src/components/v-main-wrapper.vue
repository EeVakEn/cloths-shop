<template>
  <div class="v-main-wrapper">
    <v-catalog />
    <v-cart
        v-if="CART.length"
        v-bind:cart_data="CART"
    />
  </div>

</template>

<script>
  import VCatalog from "./v-catalog";
  import VCart from "./v-cart";
  import {mapGetters} from "vuex";
  export default {
    name: 'v-main-wrapper',
    components:{
      VCart,
      VCatalog

    },
    props:{

    },
    data() {
      return {
      }
    },
    computed: {
      ...mapGetters([
          'CART'
      ])
    },
    methods: {

    },
    watch: {},
    mounted(){}
  }
</script>

<style lang="scss">
  .v-main-wrapper{
    max-width: 1200px;
    margin: 0 auto;
  }
</style>