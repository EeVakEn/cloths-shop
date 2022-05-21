<template>
  <div class="v-catalog">
    <h2>Каталог</h2>
    <div class="row g-3 my-3">
      <div class="form-group col-md-9">
        <label for="search">Поиск</label>
        <input
            type="text"
            class="form-control "
            id="search"
            v-model="search"
            placeholder="Напишите что-то для поиска"
            @input="
          search!==''?
          $router.push({name:'catalog', query: {search:search, ordering:selectedOrdering}}):
          $router.push({name:'catalog'})"
        >
        <small>Например: <a class="link" @click="search=`худи`; $router.push({name:'catalog', query: {search:'худи'}})">худи</a></small>
      </div>
      <div class="form-group col-md-3">
        <label for="ordering">Сортировка</label>
        <select
            id="ordering"
            class="form-select "
            v-model="selectedOrdering"
            @change="$router.push(
              {name: $route.name,
              params: $route.params,
              query:{search:search,ordering:selectedOrdering}}
              )"
        >
          <option v-for="(option) in ordering" :key="option.value" v-bind:value="option.value">
            {{ option.text }}
          </option>
        </select>
      </div>
    </div>


    <p v-if="search.length">Поиск: {{ search }}</p>

    <v-breadcrumb v-else-if="isFetching" :categories_array='BREADCRUMB'/>
    <div class="container-fluid">
      <div v-if="isFetching && PRODUCTS.length" class="row">
        <v-catalog-item
            class="col-xl-3 col-lg-4 col-md-6 col-sm-12"
            v-for="product in PRODUCTS"
            :key="product.article"
            :product_data="product"
            @addToFavorites="addToFavorites"
        />
      </div>
      <div v-else>
        Ничего не найдено
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
      search: '',
      ordering: [
        {text: 'Сначала новые', value: '-updated_at'},
        {text: 'Сначала старые', value: 'updated_at'},
        {text: 'Сначала дешевые', value: 'price'},
        {text: 'Сначала дорогие', value: '-price'},
      ],
      selectedOrdering: '-updated_at',
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
      if (this.$route.params.cat_slug) {
        this.GET_CATEGORY_BREADCRUMB(this.$route.params.cat_slug)
        let params = {
          cat_slug: this.$route.params.cat_slug,
          ordering: this.selectedOrdering
        }
        let co = this.selectedOrdering
        this.GET_PRODUCTS_WITH_CATEGORY(params)
        this.selectedOrdering = co
      } else {
        this.GET_BREADCRUMB()
        let params = {
          search: this.$route.query.search,
          ordering: this.selectedOrdering,
        }
        let co = this.selectedOrdering
        this.GET_PRODUCTS_FROM_API(params)
        this.selectedOrdering = co
      }
      this.isFetching = true

      this.$store.commit('SET_IS_LOADING', false)
    }
  },
  mounted() {
    // следим за изменением параметров роутера (изменениями в URI)
    this.loadData()
  },
  watch: {
    '$route.params': {
      handler() {
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
  margin: 30px 60px;

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