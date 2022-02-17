<template>
  <div class="v-main-wrapper">
    <keep-alive>
      <router-view></router-view>
    </keep-alive>
  </div>

</template>

<script>
  import {mapGetters} from "vuex";
  export default {
    name: 'v-main-wrapper',
    computed: {
      ...mapGetters([
          'CART'
      ])
    }
  }
</script>

<style lang="scss">
  .v-main-wrapper{
    max-width: calc(100% - 100px);
    padding-left: 80px;
    margin: 0 auto;
  }
</style>