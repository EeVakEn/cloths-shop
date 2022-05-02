<template>
  <div class="v-catalog">
    <h2>Каталог</h2>

    <v-breadcrumb v-if="isFetching" :categories_array='BREADCRUMB'/>
    <div class="container-fluid">
      <div  v-if="isFetching" class="row" >
        <v-catalog-item
            class="col-xl-3 col-lg-4 col-md-6 col-sm-12"
            v-for="product in PRODUCTS"
            :key="product.article"
            :product_data="product"
            @addToFavorites="addToFavorites"
        />
      </div>
    </div>

  </div>
</template>

<script>
import VCatalogItem from "./v-catalog-item";
import {mapActions, mapGetters} from 'vuex';
import VBreadcrumb from "@/components/catalog/v-breadcrumb";

export default {
  name: "v-catalog",
  components: {VBreadcrumb, VCatalogItem},
  data() {
    return {
      isFetching: false,
    }
  },
  methods: {
    ...mapActions([
      'GET_PRODUCTS_FROM_API',
      'GET_PRODUCTS_WITH_CATEGORY',
      'GET_BREADCRUMB',
      'GET_CATEGORY_BREADCRUMB',
      'ADD_TO_FAVORITES'
    ]),
    addToFavorites(data) {
      this.ADD_TO_FAVORITES(data)
    },
    async loadData() {
      this.$store.commit('SET_IS_LOADING', true)
      setTimeout(()=>{}, 1000)
      if (this.$route.params.cat_slug) {
        this.GET_CATEGORY_BREADCRUMB(this.$route.params.cat_slug)
        this.GET_PRODUCTS_WITH_CATEGORY(this.$route.params.cat_slug)
      } else {
        this.GET_BREADCRUMB()
        this.GET_PRODUCTS_FROM_API()
      }
      this.isFetching = true

      this.$store.commit('SET_IS_LOADING', false)
    }
  },
  mounted() {
    // следим за изменением параметров роутера (изменениями в URI)
    this.loadData()
  },
  watch:{
    '$route.params':{
      handler(){
        this.loadData()
      }
    }
  },
  computed: {
    ...mapGetters([
      'PRODUCTS',
      'CART',
      'FAVORITES',
      'BREADCRUMB',
    ]),
    getCartQuantity: function () {
      let res = 0;
      for (let i = 0; i < this.CART.length; i++) {
        res += this.CART[i].quantity;
      }
      return res;
    }
  }
}
</script>

<style lang="scss">
.v-catalog {
  margin: 30px;

  &__list {
    display: grid;
    grid-template-columns: repeat(auto-fill, 300px);
    justify-content: center;
    grid-gap: 10px;
  }

}

.cart_favorites {
  position: fixed;
  display: flex;
  flex-wrap: wrap;
  top: 10px;
  right: 20px;

  &__link {
    text-decoration: none;
    padding: $padding;
  }

  &__count {
    display: inline-block;
    position: relative;
    top: -15px;
    right: 0;
    width: 15px;
    height: 15px;
    text-align: center;
    line-height: 15px;
    background: $dark-color;
    color: $second-color;
    border-radius: 50%;
    font-size: 11px;
  }


}
</style>