<template>
  <div class="my_navbar container-fluid">
    <nav class="navbar navbar-expand-md my_nav mx-3">


      <button
          class="link navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbar"
          aria-controls="navbar"
          aria-expanded="false"
          aria-label="Toggle navigation"
          @click="isVisibleCatalog=false"
      >
        <i class="bi bi-list" style="color: #F5F5F5"></i>
      </button>

      <v-sidebar class="d-none d-md-block "></v-sidebar>
      <span class="navbar-brand link brand-link " @click="$router.push('/').catch(()=>{})">
        yourwear
      </span>

      <span class="d-md-none ">
        <span class="cart_favorites__link" @click="$router.push('/favorites').catch(()=>{})">
          <i class="bi bi-heart" style="color: #F5F5F5"></i>
          <span class="cart_favorites__count">{{ FAVORITES.length }}</span>
        </span>
        <span class="cart_favorites__link" @click="$router.push('/cart').catch(()=>{})">
          <i class="bi bi-bag" style="color: #F5F5F5"></i>
          <span class="cart_favorites__count">{{ getCartQuantity }}</span>
        </span>
      </span>

      <div class="collapse navbar-collapse justify-content-end" id="navbar">
        <ul class="navbar-nav ">
          <li class="nav-item d-md-none  mx-3">
            <span
                class="nav-link link dropdown-toggle"
                @click="isVisibleCatalog = !isVisibleCatalog"
            >Каталог
            </span>
            <div v-if="isVisibleCatalog"  class="nav-link" id="catalog">
              <v-categories-tree
                  class="d-md-none"
                  v-for="node in CATEGORIES"
                  :key="node.name"
                  :node="node"
                  :expanded="false"
                  @clicked="onCategoryClick"
              />
            </div>
          </li>
          <li class="nav-item d-none d-md-block   mx-3">
            <span class="nav-link link" @click="$router.push('/').catch(()=>{})">Каталог</span>
          </li>


          <li class="nav-item mx-2">
            <span class="nav-link link" @click="$router.push('/about').catch(()=>{})">
              О нас
            </span>
          </li>

          <li class="nav-item mx-2">
            <span class="nav-link link" @click="$router.push('/contacts').catch(()=>{})">
              Контакты
            </span>
          </li>

<!--          личный кабинет на маленьких экранах -->
          <li class="nav-item d-md-none mx-2">
            <div v-if="!$store.state.isAuthenticated">
              <span class="nav-link link" @click="$router.push('/log-in')">
                Личный кабинет
              </span>
            </div>
            <div v-else>
              <span class="nav-link link" @click="$router.push('/account')">
                Личный кабинет
              </span>
            </div>
          </li>

<!--          личный кабинет на больших экранах-->
          <li class="nav-item d-none d-md-block mx-2">
            <div v-if="!$store.state.isAuthenticated">
              <span class="nav-link link " @click="$router.push('/log-in')">
                <i class="bi bi-person-plus"></i>
              </span>
            </div>
            <div v-else>
              <span class="nav-link link " @click="$router.push('/account')">
                <i class="bi bi-person"></i>
              </span>
            </div>
          </li>

          <li class="nav-item d-none d-md-block mx-1">
            <span class="nav-link link" @click="$router.push('/favorites')">
              <i class="bi bi-heart"></i>
              <span class="cart_favorites__count">{{ FAVORITES.length }}</span>
            </span>
          </li>

          <li class="nav-item d-none d-md-block mx-1">
            <span class="nav-link link" @click="$router.push('/cart')">
              <i class="bi bi-bag"></i>
              <span class="cart_favorites__count">{{ getCartQuantity }}</span>
            </span>
          </li>


        </ul>

      </div>

    </nav>

  </div>
</template>

<script>
import VCategoriesTree from "@/components/sidebar/v-categories-tree";
import {mapActions, mapGetters} from "vuex";
import VSidebar from "@/components/sidebar/v-sidebar";

export default {
  name: "v-navbar",
  components: {VSidebar, VCategoriesTree},
  data() {
    return {
      isVisibleCatalog: false
    }
  },
  computed: {
    ...mapGetters([
      'CATEGORIES',
      'CART',
      'FAVORITES'
    ]),
    hasChildren() {
      return this.node.children.length
    },
    getCartQuantity() {
      let res = 0;
      for (let i = 0; i < this.CART.length; i++) {
        res += this.CART[i].quantity;
      }
      return res;
    }
  },
  mounted() {
    this.GET_CATEGORIES_FROM_API()
  },
  watch: {
    '$route'(to, from) {
      if (to !== from) {
        this.isVisibleCatalog = false;
      }
    }
  },
  methods: {
    ...mapActions([
      'GET_CATEGORIES_FROM_API'
    ]),
    onCategoryClick() {
      console.log("false visible")
      this.isVisibleCatalog = false
    }

  }
}
</script>

<style lang="scss" scoped>
.my_navbar {
  background-color: $dark-color !important;
  margin-bottom: 30px;
}

.brand-link {
  font-size: 26px;
  font-weight: 600;
}

.link {
  color: $second-color !important;
}
</style>