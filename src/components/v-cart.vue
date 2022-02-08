<template>
  <div class="v-cart">
    <div v-if="cart_data.length">
      <router-link :to="{name:'catalog'}">
        <div class="v-catalog__link_to_cart">Back</div>
      </router-link>
      <h1>Корзина</h1>
    </div>

    <div
        v-if="!cart_data.length"
        class="v-cart__no_items"
    >
      <h2>Корзина пуста</h2>
      <p>Но ты всегда можешь ее наполнить :) <br/> Начни с главной страницы </p>
      <router-link :to="{name: 'catalog'}">
        <b-button
          variant="success"
        >
          Перейти в каталог
        </b-button>
      </router-link>
    </div>
    <v-cart-item
      v-for="(item,index) in cart_data"
      :key="item.article"
      :cart_item_data="item"
      @deleteFromCart = "deleteFromCart(index)"
    />
  </div>
</template>

<script>
import VCartItem from "./v-cart-item";
import {mapActions} from "vuex";
export default {
  name: "v-cart",
  components: {VCartItem},
  props:{
    cart_data:{
      type: Array,
      default(){
        return []
      }
    }
  },
  methods:{
    ...mapActions([
        'DELETE_FROM_CART'
    ]),
    deleteFromCart(index){
      this.DELETE_FROM_CART(index)
    }
  }

}

</script>

<style lang="scss">
  .v-cart{
    &__no_items{
    }
  }
</style>