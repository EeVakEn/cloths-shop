<template>
  <div class="modal_wrapper" ref="modal_wrapper">
    <span tabindex="0"></span>
    <div class='v-modal'>
      <div class="v-modal__close" @click="closeModal">
        <i class="bi bi-x link"></i>
      </div>
      <div class="row">
        <div class="col-md-6">
          <img class="v-modal__image"
               :src="this.product_data.image"
               :alt="this.product_data.image">

        </div>
        <div class="col-md-6 v-modal__info">
          <h1 class="v-modal__name">{{ product_data.name }}</h1>
          <p class="v-modal__article">Артикул: {{ product_data.article }}</p>
          <h4>Выбор варианта товара: <i @click="reloadData" class="bi bi-arrow-clockwise refresh-btn"/></h4>

          <p>Цвет: {{ selectedColorToRussian }}</p>
          <div class="v-modal__color">
            <div class="v-modal__color-check">
              <div class="color-wrapper"
                   v-for="(color, index) in this.data_color"
                   :key="index"
              >
                <input
                    :disabled="!color.isActive"
                    type="radio"
                    name="color"
                    :id="color.name"
                    :class="['color-wrapper__color__radio', color.name]"
                    @change="selectColor(color.name)"
                />
                <label :for="color.name"
                       :class="['color-wrapper__color__label', color.name, !color.isActive?'disabled':'']"/>
              </div>
            </div>
            <span class="v-modal__select" v-if="isColorNotSelected">Выберите цвет</span>
          </div>
          <p style="margin-bottom: 10px">Размер: {{ selectedSize }}</p>
          <div class="v-modal__size">
            <div class="v-modal__size-check">
              <div class="size-wrapper"
                   v-for="(size, index) in this.data_size"
                   :key="index"
              >
                <input
                    :disabled="!size.isActive"
                    :id="size.name"
                    class="size-wrapper__size__radio"
                    name="size"
                    type="radio"
                    @change="selectSize(size.name)"
                />
                <label :for="size.name"
                       :class="{'size-wrapper__size__label':true,'disabled': !size.isActive }">{{ size.name }}</label>
              </div>
            </div>
            <span class="v-modal__select" v-if="isSizeNotSelected">Выберите размер</span>
          </div>
          <span class="v-modal__price">{{ this.product_data.price.toLocaleString() }} ₽</span>
          <div class="v-modal__buttons">
            <div class="v-modal__quantity">
              <button class="dark-button" @click="decrementQty"><b>−</b></button>
              <span class="v-modal__input" :value="quantity">{{ quantity }}</span>
              <button class="dark-button" @click="incrementQty"><b>+</b></button>
            </div>
            <div class="v-modal__btn-grp">
              <button class="dark-button" @click="addToCart">
                В корзину
                <i class="bi bi-bag"/>
              </button>
              <button class="dark-button" @click="addToFav">
                <i class="bi bi-heart-fill" v-if="isFavorite"/>
                <i class="bi bi-heart" v-else/>
              </button>
            </div>
          </div>
          <span class="v-modal__select" style="text-align: right"
                v-if="isQntOverflow">На складе остолось только {{ varQnt }} единиц данной вариации товара!</span>
          <h2>Описание</h2>
          <p class="v-modal__description" v-html="product_data.description"></p>
          <span class="link" @click="$router.push(`/product/${product_data.article}`)">Подробнее</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";

export default {
  name: "v-modal",
  props: {
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
      data_size: [],
      data_color: [],
      selectedSize: '',
      selectedColor: '',
      isColorNotSelected: false,
      isSizeNotSelected: false,
      isQntOverflow: false,
      varQnt: 1,
      quantity: 1,
      hover: false,
      isFavorite: false
    };
  },
  methods: {
    ...mapActions([
      'ADD_TO_CART',
      'ADD_TO_FAVORITES'
    ]),
    addToFav() {
      this.ADD_TO_FAVORITES(this.product_data)
      this.setIsFav()
    },
    setIsFav() {
      let exists = false
      this.FAVORITES.forEach(fav => {
        if (fav.article === this.product_data.article) {
          this.isFavorite = true
          exists = true
        }
      })
      if (exists === false)
        this.isFavorite = false
    },
    closeModal() {
      this.$emit('closeModal')
    },
    selectSize(selectedSize) {
      this.selectedSize = selectedSize
      let variants = this.product_data.variants

      let colors_list = Array.from(new Set(variants.map((variant) => variant.color)));
      let data_color = [];
      if (selectedSize !== '') {
        data_color = colors_list.map(color => {
          let qnt = variants.filter(variant => (color === variant.color && selectedSize === variant.size)).reduce((total, variant) => total + variant.quantity, 0)
          return {'name': color, 'quantity': qnt, 'isActive': qnt > 0}
        });
      } else {
        data_color = colors_list.map(color => {
          let qnt = variants.filter(variant => color === variant.color).reduce((total, variant) => total + variant.quantity, 0);
          return {'name': color, 'quantity': qnt, 'isActive': qnt > 0,};
        });
      }
      this.data_color = data_color;
      this.isSizeNotSelected = false
    },
    selectColor(selectedColor) {
      this.selectedColor = selectedColor;
      let variants = this.product_data.variants
      let sizes_list = Array.from(new Set(variants.map((variant) => variant.size)));
      let data_size = [];
      if (selectedColor !== '') {
        data_size = sizes_list.map(size => {
          let qnt = variants.filter(variant => (size === variant.size && selectedColor === variant.color)).reduce((total, variant) => total + variant.quantity, 0)
          return {'name': size, 'quantity': qnt, 'isActive': qnt > 0}
        });
      } else {
        data_size = sizes_list.map(size => {
          let qnt = variants.filter(variant => size === variant.size).reduce((total, variant) => total + variant.quantity, 0)
          return {'name': size, 'quantity': qnt, 'isActive': qnt > 0}
        });
      }
      this.data_size = data_size;
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
      this.isColorNotSelected = this.selectedColor === ""
      this.isSizeNotSelected = this.selectedSize === ""
      if (this.selectedColor !== '' && this.selectedSize !== '') {
        let selectedVariant = this.product_data.variants.filter(variant => (variant.color === this.selectedColor && variant.size === this.selectedSize))
        if (selectedVariant.length === 1) {
          selectedVariant = selectedVariant.at(0)
          let variant_id = selectedVariant.id
          if (selectedVariant.quantity >= this.quantity) {
            this.isQntOverflow = false
            const item = {
              variant_id: variant_id,
              quantity: this.quantity
            }
            this.ADD_TO_CART(item)
            this.$toasted.show(
                this.quantity % 10 === 0 || this.quantity % 10 >= 5 ?
                    this.quantity.toLocaleString() + ' товаров добавлено в корзину' :
                    (this.quantity === 1 ? 'Товар добавлен в корзину' :
                        this.quantity.toLocaleString() + ' товара добавлено в корзину'),
                {
                  icon: 'cart-shopping'
                }
            )
          } else {
            this.isQntOverflow = true
            this.varQnt = selectedVariant.quantity
          }
        }
      }
    },
    reloadData() {
      if (document.querySelector('input[name="color"]:checked'))
        document.querySelector('input[name="color"]:checked').checked = false

      if (document.querySelector('input[name="size"]:checked'))
        document.querySelector('input[name="size"]:checked').checked = false
      this.selectedColor = ''
      this.selectedSize = ''
      this.data_color = this.initColorData
      this.data_size = this.initSizeData
    }
  },
  computed: {
    ...mapGetters(['FAVORITES']),
    initColorData() {
      let variants = this.product_data.variants
      let colors_list = Array.from(new Set(variants.map((variant) => variant.color)));
      let data_color = colors_list.map(color => {
        let qnt = variants.filter(variant => color === variant.color).reduce((total, variant) => total + variant.quantity, 0)
        return {'name': color, 'quantity': qnt, 'isActive': qnt > 0}
      });
      return data_color
    },
    initSizeData() {
      let variants = this.product_data.variants
      let sizes_list = Array.from(new Set(variants.map((variant) => variant.size)));
      let data_size = sizes_list.map(size => {
        let qnt = variants.filter(variant => size === variant.size).reduce((total, variant) => total + variant.quantity, 0)
        return {'name': size, 'quantity': qnt, 'isActive': qnt > 0};
      });
      return data_size
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
  },
  mounted() {
    this.data_color = this.initColorData;
    this.data_size = this.initSizeData;
    this.setIsFav()
    document.addEventListener('click', item => {
      if (item.target === this.$refs['modal_wrapper']) this.closeModal()
    })
  },
  watch: {
    isFavorite: function (val){
      if (val)
        this.$toasted.success('Товар добавлен в избранное', {icon: 'heart',})
      else
        this.$toasted.error('Товар удален из избранного', {icon: 'heart-crack',})
    }
  }
}
</script>

<style lang="scss">
.modal_wrapper {
  z-index: 11;
  overflow-y: auto;
  position: fixed;
  display: flex;
  justify-content: center;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.8);
}

.v-modal {
  z-index: 20000;
  border-radius: 5px;
  position: absolute;
  top: 100px;
  padding: $padding;
  width: 70%;
  background-color: white;


  &__close {
    font-size: 40px;
    position: absolute;
    line-height: 1;
    top: 0;
    right: 0;
  }


  &__select {
    color: red;
    display: block;
    font-size: 12px;
  }

  &__size, &__color {
    display: block;
    position: relative;
    align-self: flex-start;
    justify-self: flex-start;
    margin-bottom: 14px;
  }

  &__size-check, &__color-check {
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
    width: 50%;
  }

  &__info {
    padding-left: 20px;
  }

  &__price {
    font-size: $font-size30;
    font-weight: bold;
  }

  &__input {
    background-color: white;
    margin: 0 $margin*2;
    color: $dark-color;
    line-height: 1.5;
    border: none;
    outline: none;
    text-align: center;
    vertical-align: center;
  }

  &__buttons {
    display: flex;
    font-size: $font-size22;
    flex-flow: row wrap;
    justify-content: flex-end;
  }

  &__quantity {
    padding-right: $padding;
  }

  &__btn-grp {
    display: block;
  }

  &__description {
    padding-top: $padding;
    text-align: justify;
  }

}
</style>