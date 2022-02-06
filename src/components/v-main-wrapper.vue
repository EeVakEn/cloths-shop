<template>
  <div class="v-main-wrapper">
    <p>{{title}}</p>
    <v-catalog/>
    <v-cart/>
  </div>

</template>

<script>
  import VCatalog from "./v-catalog";
  import VCart from "./v-cart";
  export default {
    name: 'v-main-wrapper',
    components:{
      VCart,
      VCatalog

    },
    props:{},
    data() {
      return {
        title: 'Main wrapper'
      }
    },
    computed: {},
    methods: {

    },
    watch: {},
    mounted() {
      console.log('Hi im wrapper')
    }
  }
</script>

<style lang="scss">
  .v-main-wrapper{
    max-width: 900px;
    margin: 0 auto;
  }
</style>