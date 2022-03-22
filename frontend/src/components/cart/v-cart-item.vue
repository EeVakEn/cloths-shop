<template>
  <div class="v-cart-item">
    <div class="v-cart-item__image-wrapper">
      <img class="v-cart-item__image" :src="cart_item_data.image"
           :alt="cart_item_data.artcle">
    </div>
    <div class="v-cart-item__info">
      <p><b>{{ cart_item_data.name }}</b></p>
      <div>Размер: {{ cart_item_data.selectedSize }}</div>
      <div>Цвет: {{ selectedColorToRussian }}</div>
    </div>
    <div class="v-cart-item__quantity">
      <form class="v-cart-item__quantity-form">
        <b-input-group class="v-cart-item__btn-grp">
          <b-button @click="decrement" class="v-cart-item__btn-grp__btn"><b>-</b></b-button>
          <b-input disabled class="v-cart-item__quantity__input" :value="cart_item_data.quantity"/>
          <b-button @click="increment" class="v-cart-item__btn-grp__btn"><b>+</b></b-button>
        </b-input-group>
      </form>
    </div>
    <div class="v-cart-item__price">
      <span>{{ getPrice }} ₽</span>
      <br/>
      <span
          class="v-cart-item__delete"
          @click="deleteFromCart"
      >
        <b-icon icon="trash"></b-icon> Удалить
      </span>
    </div>
  </div>
</template>

<script>

export default {
  name: "v-cart-item",
  props: {
    cart_item_data: {
      type: Object,
      default() {
        return {}
      }
    }
  },
  methods: {
    deleteFromCart() {
      this.$emit('deleteFromCart')
    },
    increment() {
      this.$emit('increment')
    },
    decrement() {
      this.$emit('decrement')
    }
  },
  computed: {
    getPrice: function () {
      return this.cart_item_data.price * this.cart_item_data.quantity
    },
    selectedColorToRussian() {
      switch (this.cart_item_data.selectedColor) {
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
  width: 100%;
  height: 120px;
  grid-template-columns: 1fr 4fr 1fr 1fr;
  display: grid;
  background-color: $second-color;
  text-align: center;
  //padding: $padding;

  &__image-wrapper {
    height: 120px;
  }

  &__image {
    height: 100%;
    width: 100%;
    object-fit: cover;
  }

  &__info {
    padding: $padding;
    text-align: left;
    overflow: hidden;
  }

  &__quantity {
    align-self: center;

    &_form {
      width: 120px;
    }

    &__input {
      border-radius: 0;
      text-align: center;
      font-weight: bold;
      line-height: 1.5;
    }
  }

  &__btn-grp {
    width: 150px;

    &__btn {
      background-color: $dark-color !important;
      border-radius: 0 !important;
    }
  }

  &__price {
    align-self: center;
    margin: 0 auto;
    font-weight: bold;
  }

  &__delete {
    font-weight: bold;
    cursor: pointer;
  }

}
</style>