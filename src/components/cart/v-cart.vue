<template>
  <div class="v-cart">
    <div v-if="cart_data.length">
      <router-link :to="{name:'catalog'}">
        <div class="v-catalog__link_to_cart">Back</div>
      </router-link>
      <h1>Корзина</h1>
      <div class="v-cart__wrapper">
        <div class="v-cart__delivery">

        </div>
        <div class="v-cart__cart">
          <v-cart-item
              v-for="(item,index) in cart_data"
              :key="item.article"
              :cart_item_data="item"
              @deleteFromCart="deleteFromCart(index)"
              @increment="increment(index)"
              @decrement="decrement(index)"
          />
          <div class="v-cart__total">
            <div>Total</div>
            <div class="v-cart__total__price"><b>{{ getFormattedPrice }} ₽</b></div>
            <div
                class="v-cart__delete"
                @click="deleteAllFromCart"
            >
              Очистить корзину
            </div>
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
      <router-link :to="{name: 'catalog'}">
        <button class="dark-button">Перейти в каталог</button>
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
  props: {
    cart_data: {
      type: Array,
      default() {
        return []
      }
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
    }
  },
  computed: {
    cartTotalCost() {
      let result = 0

      for (let item of this.cart_data) {
        result += item.price * item.quantity
      }
      return result;
    },
    getFormattedPrice: function () {
      return this.cartTotalCost.toLocaleString()
    },
  }

}

</script>

<style lang="scss">
.v-cart {
  &__wrapper {
    display: grid;

    grid-template-columns: 1fr 1fr;
  }

  &__total {
    display: flex;
    flex-direction: column;
    align-items: end;
    width: 100%;
    background-color: $dark-color;
    color: white;
    padding: $padding $padding*3;

    &__price {
      font-weight: bold;
      font-size: 22px;
    }
  }

  &__delete {
    font-weight: bold;
    cursor: pointer;
  }

}
</style>