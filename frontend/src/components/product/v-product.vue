<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col image">
        <img :src="PRODUCT.image" alt="Картинка товара отсутствует"/>
      </div>
      <div class="col info">
        <h1>Информация о товаре</h1>
        <p>{{PRODUCT.price}}</p>
      </div>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";

export default {
  name: "v-product",
  data() {
    return {
      product: Object,
    }
  },
  methods: {
    ...mapActions(['GET_DETAIL_PRODUCT']),
  },
  mounted() {
    this.GET_DETAIL_PRODUCT(this.$route.params.product_id)
  },
  computed:{
    ...mapGetters(['PRODUCT'])
  },

}
</script>

<style scoped>

</style>