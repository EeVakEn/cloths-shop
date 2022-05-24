<template>
  <div class="v-cart container">
    <div v-if="this.CART.length">

      <div class="v-cart__wrapper row">
        <div class="v-cart__cart col-lg-6">
          <h2>Корзина</h2>
          <div class="v-cart__cart-wrapper">
            <v-cart-item
              v-for="(item,index) in this.CART"
              :key="index"
              :cart_item_data="item"
              @deleteFromCart="deleteFromCart(index)"
              @increment="increment(index)"
              @decrement="decrement(index)"
          />
          <div class="v-cart__total">
            <div>Итого</div>
            <div><b>{{ totalPrice.toLocaleString() }} ₽</b></div>
            <a
                class="v-cart__total__delete"
                @click="deleteAllFromCart"
            >
              <i class="bi bi-trash"></i>
              Очистить корзину
            </a>
          </div>
          </div>

        </div>
        <div class="v-cart__delivery col-lg-6">
          <v-order-form :cost="totalPrice"></v-order-form>
        </div>
      </div>

    </div>
    <div
        v-else
        class="v-cart__no_items"
    >
      <h2>Корзина пуста</h2>
      <i style="font-size: 25vw ; padding: 30px 0" class="fa fa-basket-shopping"></i>
<!--      <img class="link-img" src="@/assets/images/shopping-cart-svgrepo-com.svg" alt="" style="max-width: 400px"/>-->
      <p>Но ты всегда можешь ее наполнить :) <br/> Кликай на кнопочку </p>
      <button class="dark-button" @click="$router.push('/')">Перейти в каталог</button>
    </div>
  </div>

</template>

<script>
import VCartItem from "./v-cart-item";
import {mapActions, mapGetters} from "vuex";
import VOrderForm from "@/components/cart/v-order-form";
import axios from "axios";

export default {
  name: "v-cart",
  components: {VOrderForm, VCartItem},
  data() {
    return {
      totalPrice: 0
    }
  },
  methods: {
    ...mapActions([
      'DELETE_FROM_CART',
      'INCREMENT_CART_ITEM',
      'DECREMENT_CART_ITEM',
      'DELETE_ALL_FROM_CART'
    ]),
    increment(index) {
      this.INCREMENT_CART_ITEM(index)
    },
    decrement(index) {
      this.DECREMENT_CART_ITEM(index)
    },
    deleteFromCart(index) {
      this.DELETE_FROM_CART(index)
    },
    deleteAllFromCart() {
      this.DELETE_ALL_FROM_CART();
    },
    async getTotal(){
      let res = 0
        for (let item of this.CART) {
          res += await axios.get(`/api/catalog/variants/${item.variant_id}/`)
              .then(response => response.data.product.price)
              .catch(error => error) * item.quantity
        }
        this.totalPrice = res
    }
  },
  mounted() {
    this.getTotal()
  },
  watch:{
    'CART':{
      deep: true,
      async handler(){
        this.getTotal()
      }
    }
  },
  computed: {
    ...mapGetters([
      'CART',
    ]),
  }

}

</script>

<style lang="scss">
.v-cart {
  &__wrapper {
  }
  &__cart-wrapper{
    box-shadow: 0 4px 25px 0 rgba(0, 0, 0, 0.3);
  }
  &__cart, &__delivery {

    padding: $padding;
  }

  &__total {
    display: block;
    justify-content: end;
    background-color: $dark-color;
    color: white;
    padding: $padding*2;
    font-weight: bold;
    font-size: 18px;
    text-align: right;

    &__delete {
      color: firebrick !important;
      text-decoration: none;
      cursor: pointer;
      font-size: 16px;
      font-weight: bold;
    }
  }

  &__no_items {
    margin: 50px 0;
    text-align: center;
  }


}
</style>