<template>
  <div class="v-cart container-fluid">
    <div v-if="this.CART.length">

      <div class="v-cart__wrapper row">
        <div class="v-cart__delivery col-lg-6">
          <h2>Оформление</h2>
          <v-order-form></v-order-form>
        </div>
        <div class="v-cart__cart col-lg-6">
          <h2>Корзина</h2>
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
            <div><b>{{ getFormattedPrice }} ₽</b></div>
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

    </div>
    <div
        v-else
        class="v-cart__no_items"
    >
      <h2>Корзина пуста</h2>
      <p>Но ты всегда можешь ее наполнить :) <br/> Кликай на кнопочку </p>
      <button class="dark-button" @click="$router.push('/')">Перейти в каталог</button>
    </div>
  </div>

</template>

<script>
import VCartItem from "./v-cart-item";
import {mapActions, mapGetters} from "vuex";
import VOrderForm from "@/components/cart/v-order-form";

export default {
  name: "v-cart",
  components: {VOrderForm, VCartItem},
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

  },
  mounted() {
  },
  computed: {
    cartTotalCost() {
      let result = 0

      for (let item of this.CART) {
        result += item.variant_id * item.quantity
      }
      return result;
    },
    getFormattedPrice: function () {
      return this.cartTotalCost.toLocaleString()
    },
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
    text-align: center;
  }


}
</style>