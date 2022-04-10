<template>
  <div class="v-cart-item">
    <div class="col-3 v-cart-item__image-wrapper">
      <img class="v-cart-item__image" :src="this.variant.product.image"
           :alt="this.variant.product.article">
    </div>
    <div class="col-5 v-cart-item__info">
      <p><b>{{ this.variant.name }}</b></p>
      <div>Размер: {{ this.variant.size }}</div>
      <div>Цвет: {{ selectedColorToRussian }}</div>
    </div>
    <div class="col-4 v-cart-item__end">
      <div class="v-cart-item__price">
        {{ getPrice }} ₽
      </div>
      <div class="v-cart-item__quantity">
          <div class="input-group v-cart-item__btn-grp">
            <button @click="decrement" class="btn dark-button"><b>−</b></button>
            <span class="v-cart-item__quantity__input"  size="2" maxlength="2">{{cart_item_data.quantity}}</span>
            <button @click="increment" class="btn dark-button" ><b>+</b></button>
          </div>
      </div>
      <div class="v-cart-item__delete" @click="deleteFromCart">
        <i class="bi bi-trash"></i>
        Удалить
      </div>
    </div>
  </div>
</template>

<script>

import {mapActions} from "vuex";
import axios from "axios";

export default {
  name: "v-cart-item",
  data(){
    return{
      variant: {}
    }
  },
  props: {
    cart_item_data: {
      type: Object,
      default() {
        return {}
      }
    }
  },
  methods: {
    ...mapActions([
        'GET_VARIANT'
    ]),
    deleteFromCart() {
      this.$emit('deleteFromCart')
    },
    increment() {
      this.$emit('increment')
    },
    decrement() {
      this.$emit('decrement')
    },
  },
  mounted() {
    axios.get(`http://localhost:8000/api/catalog/variants/${this.cart_item_data.variant_id}/`)
        .then(response  => {this.variant = response.data})
        .catch(error => error)

  },
  computed: {
    getPrice: function () {
      return this.variant.product.price * this.cart_item_data.quantity
    },
    selectedColorToRussian() {
      switch (this.variant.color) {
        case 'white':
          return 'Белый'.toLowerCase();
        case 'black':
          return 'Черный'.toLowerCase();
        case 'bejeviy':
          return 'Бежевый'.toLowerCase();
        case 'pink':
          return 'Розовый'.toLowerCase();
        case 'gray':
          return 'Серый'.toLowerCase();
        case 'light-blue':
          return 'Голубой'.toLowerCase();
        case 'yellow':
          return 'Желтый'.toLowerCase();
        case 'liloviy':
          return 'Лиловый'.toLowerCase();
        case 'salad':
          return 'Салатовый'.toLowerCase();
        case 'blue':
          return 'Синий'.toLowerCase();
        case 'dark-blue':
          return 'Темно-синий'.toLowerCase();
        case 'bordoviy':
          return 'Бордовый'.toLowerCase();
        case 'red':
          return 'Красный'.toLowerCase();
        case 'green':
          return 'Зеленый'.toLowerCase();
        case 'vishneviy':
          return 'Вишневый'.toLowerCase();
        case 'haki':
          return 'Хаки'.toLowerCase();
        case 'coffee':
          return 'Кофейный'.toLowerCase();
        default :
          return '';
      }
    }
  },
}
</script>

<style lang="scss">
.v-cart-item {
  display: flex;
  flex-flow: row nowrap;
  height: 150px;
  background-color: $second-color;
  text-align: center;

  &__image-wrapper {
    display: block;
    padding: 0 !important;
    height: 100%;
  }

  &__image {
    height: 100%;
    width: 100%;
    object-fit: cover;
  }

  &__info {
    display: block;
    padding: $padding*2;
    text-align: left;
    overflow: hidden;
  }

  &__end {
    padding: $padding*2;
    display: flex;
    flex-flow: column;
    align-items: flex-end;
    justify-content: center;
    gap: $padding*2
  }

  &__quantity {
    &__input {
      border-radius: 0;
      padding: 0 $padding*2;
      display: block;
      text-align: center;
      font-weight: bold;
      line-height: 1.5;
    }
  }

  &__btn-grp {
    display: flex;
    justify-content: center;
    align-items: center;
    &__btn {
      background-color: $dark-color !important;
    }
  }

  &__price {
    align-self: flex-end;
    text-align: end;
    font-weight: bold;
    font-size: 20px;
  }

  &__delete {
    font-weight: bold;
    cursor: pointer;
  }

}
</style>