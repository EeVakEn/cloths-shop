<template>

  <div class="v-catalog-item">

    <v-modal
        v-if="isInfoModalVisible"
        rightBtnTitle="Add to cart"
        :modalTitle="product_data.name"
        @closeModal="closeModal"
        @subAction="addToCart"
    >
      <div class="v-modal__slot">
        <div class="v-modal__image-wrapper">
          <img class="v-modal__image" :src=" require('../../assets/images/products/' + product_data.image)"
               :alt="product_data.image">
        </div>
        <div class="v-modal__info">
          <h1 class="v-modal__name">{{ product_data.name }}</h1>
          <p class="v-modal__article">Артикул: {{ product_data.article }}</p>
          <div class="v-modal__size">
            <p>Размер:</p>
          </div>
          <div class="v-modal__color">
            <p>Цвет:</p>
            <div class="v-modal__color-check">
              <v-product-color
                  v-for="color in product_data.color"
                  :key="color"
                  :color="color"
              />

            </div>
          </div>

          <span class="v-modal__price">{{ getFormattedPrice }} ₽</span>
          <div class="v-modal__buttons">
            <div class="v-modal__quantity">
              <button class="v-modal__qty-btn dark-button" @click="decrementQty"><b>-</b></button>
              <input class="v-modal__input" :value="quantity" disabled/>
              <button class="v-modal__qty-btn dark-button" @click="incrementQty"><b>+</b></button>
            </div>
            <div class="v-modal__btn-grp">
              <button class="dark-button" @click="addToCart">
                В корзину
                <b-icon icon="basket"/>
              </button>
              <button class="dark-button" @click="addToFavorites">
                <b-icon v-if="product_data.isFavorite" icon="heart-fill"/>
                <b-icon v-else icon="heart"/>
              </button>
            </div>
          </div>
          <h2>Описание</h2>
          <p class="v-modal__description">{{ product_data.description }}</p>
          <a href="#" style="text-decoration: none">Ссылка на полноценную страницу с товаром</a>
        </div>
      </div>

    </v-modal>


    <div class="v-catalog-item__image-wrapper">
      <img class="v-catalog-item__image" :src=" require('../../assets/images/products/' + product_data.image)"
           :alt="product_data.image">
    </div>

    <p class="v-catalog-item__name">{{ product_data.name }}</p>
    <p class="v-catalog-item__description">{{ product_data.description }}</p>
    <div class="v-catalog-item__bottom">
      <span class="v-catalog-item__price">{{ getFormattedPrice }} ₽</span>
      <b-button-group class="v-catalog-item__btn-grp">
        <b-button class="v-catalog-item__btn-grp__btn" @click="showModal">
          В корзину
          <b-icon icon="basket" scale="1"/>
        </b-button>
        <b-button class="v-catalog-item__btn-grp__btn" @click="addToFavorites">
          <b-icon v-if="product_data.isFavorite" icon="heart-fill" scale="1"/>
          <b-icon v-else icon="heart" scale="1"/>
        </b-button>
      </b-button-group>
    </div>

  </div>
</template>

<script>
import VModal from "../v-modal";
import VProductColor from "../v-product-color";

export default {
  name: "v-catalog-item",
  components: {VProductColor, VModal},
  data() {
    return {
      isInfoModalVisible: false,
      quantity: 1,
    }
  },
  props: {
    product_data: {
      type: Object,
      default() {
        return {}
      },
    },
    favorites_data: {
      type: Array,
      default() {
        return [];
      }
    }
  },
  methods: {
    addToCart() {
      this.$emit('addToCart', this.product_data, this.quantity)
    },
    addToFavorites() {
      this.$emit('addToFavorites', this.product_data)
    },
    showModal() {
      this.isInfoModalVisible = true;
    },
    closeModal() {
      this.isInfoModalVisible = false;
    },
    incrementQty() {
      if (this.quantity < 50) {
        this.quantity++
      }
    },
    decrementQty() {
      if (this.quantity > 1) {
        this.quantity--
      }
    },

  },
  mounted() {
    this.$set(this.product_data, 'quantity', 1)
    this.$set(this.product_data, 'isFavorite', false)
    console.log(this.product_data.color)
  },
  computed: {
    getFormattedPrice: function () {
      return this.product_data.price.toLocaleString()
    },
  }
}
</script>

<style lang="scss">
.v-modal__slot {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-start;
  justify-content: flex-start;
}

.v-modal {
  &__color{
    display: block;
    align-self: flex-start;
    justify-self: flex-start;
  }
  &__color-check {
    display: flex;
    flex-flow: row wrap;
    gap: $padding/2;
  }

  &__image {
    width: 100%;
    object-fit: cover;
  }

  &__image-wrapper {
    display: block;
    width: 400px;
  }

  &__info {
    display: flex;
    flex-flow: column;
    align-items: flex-start;
    padding: 20px;
    width: 480px;
  }

  &__price {
    font-size: $font-size30;
    font-weight: bold;
  }

  &__input {
    display: inline-block;
    width: 45px;
    background-color: white;
    color: $dark-color;
    line-height: 1.5;
    border: 1px solid white;
    text-align: center;
    vertical-align: center;
    outline: none;
    padding: 0.375rem 0.75rem;
  }

  &__input:active {
    border: none;
    outline: none;
  }

  &__qty-btn {
    display: inline-block;
    width: 40px;
    padding: 0.375rem 0.75rem;
  }

  &__buttons {
    display: flex;

    flex-flow: row wrap;
    justify-self: flex-end;
    align-self: flex-end;
    padding: $padding*2 0;
  }

  &__quantity {
    display: block;
    font-size: 22px;
  }

  &__btn-grp {
    margin-left: $margin*2;
    align-self: flex-end;
    display: block;
    font-size: $font-size22;
  }

  &__description {
    padding-top: $padding;
    text-align: justify;
  }
}

.v-catalog-item {
  display: flex;
  flex-direction: column;
  background-color: $second-color;
  width: 300px;
  height: 500px;

  &__image-wrapper {
    width: 100%;
    height: 350px;
  }

  &__name {
    padding: $padding;
    text-align: left;
    font-weight: bold;
    margin-bottom: 0;
  }

  &__description {
    padding: 0 $padding;
    text-align: left;
    height: 50px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  &__bottom {
    position: relative;
    display: block;
    bottom: $padding;
  }

  &__price {
    line-height: 20px;
    font-size: 20px;
    font-weight: bold;
    padding-right: $padding*2;
  }

  &__btn-grp {
    width: 180px;

    &__btn {
      background-color: $dark-color !important;
      border-radius: 0 !important;
    }
  }

  &__image {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
}
</style>