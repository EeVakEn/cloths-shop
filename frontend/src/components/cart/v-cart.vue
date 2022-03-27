<template>
  <div class="v-cart">
    <div v-if="cart_data.length">
      <h1>Корзина</h1>
      <div class="v-cart__wrapper row">
        <div class="v-cart__delivery col-lg-6">
          <img
              src="https://mykaleidoscope.ru/uploads/posts/2021-10/1634164062_50-mykaleidoscope-ru-p-rizhii-tsvet-volos-krasivaya-pricheska-dev-54.jpg"
              style="width: 100%"/>
        </div>
        <div class="v-cart__cart col-lg-6">
          <v-cart-item
              v-for="(item,index) in cart_data"
              :key="item.article"
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
      color: white !important;
      text-decoration: none;
      cursor: pointer;
      font-size: 16px;
      font-weight: bold;
    }
  }


}
</style>