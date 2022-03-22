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
          <img class="v-modal__image"
               :src="product_data.image"
               style="width:100%;"
               :alt="product_data.image">
        </div>
        <div class="v-modal__info">
          <h1 class="v-modal__name">{{ product_data.name }}</h1>
          <p class="v-modal__article">Артикул: {{ product_data.article }}</p>
          <p style="margin-bottom: 10px">Размер: {{ selectedSize }}</p>
          <div class="v-modal__size">
            <div class="v-modal__size-check">
              <v-product-size
                  v-for="size in product_data.size"
                  :key="size"
                  :size="size"
                  :selected-size="selectedSize"
                  @selectSize="selectSize"
              />
            </div>
            <span class="v-modal__select" v-if="isSizeNotSelected">Выберите размер</span>
          </div>
          <p style="margin-bottom: 10px">Цвет: {{ selectedColorToRussian }}</p>
          <div class="v-modal__color">
            <div class="v-modal__color-check">
              <v-product-color
                  v-for="color in product_data.color"
                  :key="color"
                  :color="color"
                  :selected-color="selectedColor"
                  @selectColor="selectColor"
              />
            </div>
            <span class="v-modal__select" v-if="isColorNotSelected">Выберите цвет</span>
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
      <img class="v-catalog-item__image" :src="product_data.image"
           :alt="product_data.image">
    </div>

    <p class="v-catalog-item__name">{{ product_data.name }}</p>

    <div class="v-catalog-item__colors-wrapper">
      <b>Цвет: </b>
      <div
          v-for="(color,index) in product_data.color"
          :key="index"
          :class="[color, 'v-catalog-item__color']"
          :data-microtip="colorToRu(color)"
      />
    </div>


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
import VProductSize from "../v-product-size";

export default {
  name: "v-catalog-item",
  components: {VProductColor, VProductSize, VModal},
  data() {
    return {
      isColorNotSelected: false,
      isSizeNotSelected: false,
      isInfoModalVisible: false,
      quantity: 1,
      selectedSize: "",
      selectedColor: ""
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
      this.$emit('addToCart', this.product_data, this.quantity, this.selectedColor, this.selectedSize)
      this.isColorNotSelected = this.selectedColor === ""
      this.isSizeNotSelected = this.selectedSize === ""
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
    selectSize(size) {
      this.selectedSize = size
      this.isSizeNotSelected = false
    },
    selectColor(color) {
      this.selectedColor = color
      this.isColorNotSelected = false
    },
    colorToRu(c) {
      switch (c) {
        case 'white':
          return 'Белый';
        case 'black':
          return 'Черный';
        case 'bejeviy':
          return 'Бежевый';
        case 'pink':
          return 'Розовый';
        case 'gray':
          return 'Серый';
        case 'light-blue':
          return 'Голубой';
        case 'yellow':
          return 'Желтый';
        case 'liloviy':
          return 'Лиловый';
        case 'salad':
          return 'Салатовый';
        case 'blue':
          return 'Синий';
        case 'dark-blue':
          return 'Темно-синий';
        case 'bordoviy':
          return 'Бордовый';
        case 'red':
          return 'Красный';
        case 'green':
          return 'Зеленый';
        case 'vishneviy':
          return 'Вишневый';
        case 'haki':
          return 'Хаки';
        case 'coffee':
          return 'Кофейный';
        default :
          return '';
      }
    }

  },
  mounted() {
    this.$set(this.product_data, 'quantity', 1)
    this.$set(this.product_data, 'isFavorite', false)
  },
  computed: {
    getFormattedPrice() {
      return this.product_data.price.toLocaleString()
    },
    selectedColorToRussian() {
      switch (this.selectedColor) {
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
  &__select {
    color: red;
    display: block;
    font-size: 12px;
    position: absolute;
    top: 36px;
  }

  &__size {
    display: block;
    position: relative;
    align-self: flex-start;
    justify-self: flex-start;
    margin-bottom: 14px;
  }

  &__size-check {
    display: flex;
    flex-flow: row wrap;
    gap: $padding/2;
  }

  &__color {
    display: block;
    position: relative;
    align-self: flex-start;
    justify-self: flex-start;
    margin-bottom: 14px;
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

  &__colors-wrapper {
    display: flex;
    flex-flow: wrap row;
    align-items: center;
    padding: 0 $padding;
  }

  &__color {
    width: 20px;
    height: 20px;
    cursor: pointer;
    margin: 0 $margin/3;
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