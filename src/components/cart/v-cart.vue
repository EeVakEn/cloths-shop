<template>
  <div class="v-cart">
    <div v-if="cart_data.length">
      <router-link :to="{name:'catalog'}">
        <div class="v-catalog__link_to_cart">Back</div>
      </router-link>
      <h1>Корзина</h1>
      <v-cart-item
          v-for="(item,index) in cart_data"
          :key="item.article"
          :cart_item_data="item"
          @deleteFromCart = "deleteFromCart(index)"
          @increment="increment(index)"
          @decrement="decrement(index)"
      />
      <div class="v-cart__total">
        <p>Total: {{cartTotalCost}}</p>
      </div>
    </div>

    <div
        v-else
        class="v-cart__no_items"
    >
      <h2>Корзина пуста</h2>
      <p>Но ты всегда можешь ее наполнить :) <br/> Кликай на кнопочку </p>
      <router-link :to="{name: 'catalog'}">
        <b-button
          variant="success"
        >
          Перейти в каталог
        </b-button>
      </router-link>
    </div>


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
      'DELETE_FROM_CART',
      'INCREMENT_CART_ITEM',
      'DECREMENT_CART_ITEM'
    ]),
    increment(index) {
      this.INCREMENT_CART_ITEM(index)
    },
    decrement(index) {
      this.DECREMENT_CART_ITEM(index)
    },
    deleteFromCart(index){
      this.DELETE_FROM_CART(index)
    }
  },
  computed:{
    cartTotalCost(){
      let result = 0

      for (let item of this.cart_data){
        result += item.price * item.quantity
      }
      // for (let item of this.cart_data){
      //   result.push(item.price * item.quantity);
      // }
      // result = result.reduce(function (sum,el){
      //   return sum + el
      // })
      return result;
    }
  }

}

</script>

<style lang="scss">
  .v-cart{
    &__no_items{
    }
    &__total{

    }
  }
</style>