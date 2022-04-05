<template>
  <div class="modal_wrapper" ref="modal_wrapper">
    <span tabindex="0"></span>
    <div class='v-modal'>
      <div class="v-modal__close">
        <div class="cl-btn-2" @click="closeModal">
          <div>
            <div class="leftright"></div>
            <div class="rightleft"></div>
          </div>
        </div>
      </div>
      <div>
        <div class="v-modal__content">
          <div class="v-modal__slot">
            <div class="v-modal__image-wrapper">
              <img class="v-modal__image"
                   :src="this.product_data.image"
                   style="width:100%;"
                   :alt="this.product_data.image">
            </div>
            <div class="v-modal__info">
              <h1 class="v-modal__name">{{ product_data.name }}</h1>
              <p class="v-modal__article">Артикул: {{ product_data.article }}</p>

              <p style="margin-bottom: 10px">Цвет: {{ selectedColorToRussian }}</p>
              <div class="v-modal__color">
                <div class="v-modal__color-check">
                  <v-product-color
                      v-for="color in colors"
                      :key="color"
                      :color="color"
                      :selected-color="selectedColor"
                      @selectColor="selectColor"
                  />
                </div>
                <span class="v-modal__select" v-if="isColorNotSelected">Выберите цвет</span>
              </div>
              <p style="margin-bottom: 10px">Размер: {{ selectedSize }}</p>
              <div class="v-modal__size">
                <div class="v-modal__size-check">
                  <v-product-size
                      v-for="size in sizes"
                      :key="size"
                      :size="size"
                      :selected-size="selectedSize"
                      @selectSize="selectSize"
                  />
                </div>
                <span class="v-modal__select" v-if="isSizeNotSelected">Выберите размер</span>
              </div>
              <span class="v-modal__price">{{ this.product_data.price.toLocaleString() }} ₽</span>
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
              <a href="#" >Ссылка на полноценную страницу с товаром</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "v-modal",
  props: {
    colors: {
      type: Array,
      default() {
        return [];
      }
    },
    sizes: {
      type: Array,
      default() {
        return [];
      }
    },
    product_data: {
      type: Object,
      default() {
        return {}
      }
    },
    submitAction: {
      type: String,
      default: 'Ok'
    }
  },
  data() {
    return {
      isColorNotSelected: false,
      isSizeNotSelected: false,
      selectedSize: "",
      selectedColor: "",
      quantity: 1,
      hover: false,
    };
  },
  methods: {
    addToFavorites() {
      this.$emit('addToFavorites', this.product_data)
      this.isFavorite = this.product_data.isFavorite
    },
    closeModal() {
      this.$emit('closeModal')
    },
    selectSize(size) {
      this.selectedSize = size
      this.isSizeNotSelected = false
    },
    selectColor(color) {
      this.selectedColor = color
      this.isColorNotSelected = false
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
    addToCart() {
      this.$emit('addToCart', this.product_data, this.quantity, this.selectedColor, this.selectedSize)
      this.isColorNotSelected = this.selectedColor === ""
      this.isSizeNotSelected = this.selectedSize === ""
    },
  },
  mounted() {
  },
  computed: {
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
.modal_wrapper {
  overflow-y: auto;
  position: fixed;
  display: flex;
  justify-content: center;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 20000;
  background: rgba(0, 0, 0, 0.38);
}

.v-modal {
  border-radius: 5px;
  position: relative;
  top: 100px;
  margin-left: 85px;
  padding: $padding;
  width: 900px;
  background-color: white;
  z-index: 20030;

  &__close {
    display: inline-block;
    position: absolute;
    top: $margin;
    right: $margin;
    font-size: 22px;
  }

  &__close-btn {
    color: $dark-color;
    width: 30px;
    height: 30px;
    transition: .5s;
  }

  &__content {
    display: flex;
    flex-flow: row wrap;
  }


  // кнопка закрытия модального окна
  .cl-btn-2 {
    margin: 10px;
    display: flex;
    justify-content: center;
  }

  .cl-btn-2 div {
    cursor: pointer;
    position: relative;
    height: 34px;
    width: 25px;
  }

  .cl-btn-2 .leftright {
    height: 2px;
    width: 25px;
    position: absolute;
    margin-top: 12px;
    background-color: $dark-color;
    border-radius: 1px;
    transform: rotate(45deg);
    transition: all .2s ease-in;
  }

  .cl-btn-2 .rightleft {
    height: 2px;
    width: 25px;
    position: absolute;
    margin-top: 12px;
    background-color: $dark-color;
    border-radius: 1px;
    transform: rotate(-45deg);
    transition: all .2s ease-in;
  }

  .cl-btn-2 div:hover .leftright {
    transform: rotate(-45deg);
    background-color: $dark-color;
  }

  .cl-btn-2 div:hover .rightleft {
    transform: rotate(45deg);
    background-color: $dark-color;
  }

  .cl-btn-2 div:hover .close-btn {
    opacity: 1;
  }
}
</style>