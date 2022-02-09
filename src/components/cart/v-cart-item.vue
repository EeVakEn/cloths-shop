<template>
  <div class="v-cart-item">
    <img class="v-cart-item__image" :src=" require('../../assets/images/' + cart_item_data.image)" :alt="cart_item_data.artcle">
    <div class="v-cart-item__info">
      <p>{{cart_item_data.name}}</p>
      <p>{{cart_item_data.price}} ₽</p>
    </div>
    <div class="v-cart-item__quantity">
      <p>Количество: </p>
      <form class ="v-cart-item__quantity_form">
        <b-input-group>
          <b-button @click="decrement">-</b-button>
          <b-form-input
              class="v-cart-item__quantity_input"
              type="text"
              disabled
              :value="cart_item_data.quantity"/>
          <b-button @click="increment">+</b-button>
        </b-input-group>
      </form>


    </div>
    <b-button
      variant="danger"
      @click ="deleteFromCart"
    >
      Удалить
    </b-button>
  </div>
</template>

<script>

export default {
  name: "v-cart-item",
  props:{
    cart_item_data:{
      type: Object,
      default(){
        return {}
      }
    }
  },
  methods:{
    deleteFromCart(){
      this.$emit('deleteFromCart')
    },
    increment(){
      this.$emit('increment')
    },
    decrement(){
      this.$emit('decrement')
    }
  },
  mounted() {
  }
}
</script>

<style lang="scss">
  .v-cart-item{
    display: flex;
    flex-wrap: nowrap;
    justify-content: space-between;
    align-items: center;

    box-shadow: 0 0 10px 0 $main-color;
    padding: $padding*2;
    margin-bottom: $margin*2;
    background-color: $second-color;
    border-radius: $radius*4;
    &__image {
      max-width: 100px;
    }
    &__quantity{
      &_form{
        width: 120px;
      }
      &_input{
        text-align: center;
      }
    }
  }
</style>