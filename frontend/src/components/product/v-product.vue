<template>
  <div class="container" v-if="isFetching">
    <div class="row">
      <div class="col-md-6 image_wrapper">
        <img class="image" :src="PRODUCT.image" alt="Картинка товара отсутствует"/>
      </div>
      <div class="col-md-6 info">
        <h1>{{ PRODUCT.name }}</h1>
        <p>Артикул: <span class="badge rounded-pill bg-dark">{{ PRODUCT.article }}</span></p>


        <h4>Выбор варианта товара: <i @click="reloadData" class="bi bi-arrow-clockwise refresh-btn"/></h4>
        <div v-if="isFetching">
          <p>Цвет: {{ selectedColorToRussian }}</p>
          <div class="v-modal__color">
            <div class="v-modal__color-check">
              <div class="color-wrapper"
                   v-for="(color, index) in data_color"
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
                   v-for="(size, index) in data_size"
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
          <span class="v-modal__price">{{ PRODUCT.price.toLocaleString() }} ₽</span>
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
        </div>


        <h3>
          <a data-bs-toggle="collapse" href="#description" role="button"
             aria-expanded="false" aria-controls="description">
            Описание
          </a>
        </h3>
        <div class="collapse" id="description">
          <div style="text-align: justify" v-html="PRODUCT.description"/>
        </div>
        <hr/>
        <h3>
          <a data-bs-toggle="collapse" href="#reviews" role="button"
             aria-expanded="false" aria-controls="reviews">
            Отзывы <i>({{ reviews.length }})</i>
          </a>
        </h3>
        <div class="collapse" id="reviews">
          <form class="review" @submit="addReview" @submit.prevent="">
            <h4><b>Оставьте ваш отзыв</b></h4>
            <label for="markReview" class="form-label">Оцените товар</label>
            <star-rating id="markReview" style="margin-bottom: 10px" :show-rating="false" :star-size="25"
                         :animate="true" active-color="#000" active-border-color="#000" :border-width="2"
                         :active-on-click="true" :padding="3" aria-required="true" v-model="mark"></star-rating>
            <div class="mb-3">
              <label for="textReview" class="form-label">Отзыв</label>
              <textarea class="form-control" v-model="reviewText" id="textReview" rows="2"
                        placeholder="Напишите свой отзыв..." required></textarea>
            </div>
            <button type="submit" class="dark-button">Отправить</button>
          </form>
          <transition-group name="slide-fade">
            <div class="review" v-for="item in reviews" :key='item.id'>

              <div class="review_header">
                <div class="author">
                  <div class="author_img">
                    {{ item.review_author[0].toUpperCase() }}
                  </div>
                  <b>
                    {{ item.review_author }}
                  </b>
                  <div style="transform: translateY(-3px)">
                    <star-rating :read-only="true" active-color="#000" active-border-color="#000"
                                 :rating="item.raiting"
                                 :show-rating="false" :star-size="15"></star-rating>
                  </div>
                </div>
                <div>
                    <span v-if="item.updated_at === item.created_at"
                          class="badge rounded-pill bg-light text-dark"><i>{{ item.updated_at }}</i></span>
                  <span v-else class="badge rounded-pill bg-light text-dark"><i class="bi bi-pencil"> {{
                      item.updated_at
                    }}</i></span>
                </div>

              </div>
              <div class="review_body">
                <div class="review_text">{{ item.review }}</div>
              </div>

            </div>
          </transition-group>
        </div>
        <hr/>


      </div>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";
import StarRating from 'vue-star-rating'
import axios from "axios";
import router from "@/router/router";

export default {
  name: "v-product",
  components: {
    StarRating
  },
  data() {
    return {
      reviews: [],
      mark: 1,
      reviewText: '',
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
      isFetching: false,
      isFetchingData: false,
      isFavorite: false
    };
  },
  methods: {
    ...mapActions([
      'ADD_TO_CART',
      'GET_DETAIL_PRODUCT',
      'ADD_TO_FAVORITES'
    ]),
    async addReview() {
      if (this.$store.state.isAuthenticated) {
        const data = {
          'review': this.reviewText,
          'raiting': parseInt(this.mark)
        }
        this.reviewText = ''
        this.mark = 1
        await axios.post(`/api/catalog/products/${this.PRODUCT.article}/review/`, data)
            .then().catch(error => {
              console.log(error)
            })
        await axios.get(`/api/catalog/products/${this.PRODUCT.article}/reviewlist/`)
            .then(resp => {
              this.reviews = resp.data.results
            })
            .catch(error => {
              console.log(error)
            })
      } else {
        router.push('/log-in')
      }
    },
    addToFav() {
      this.ADD_TO_FAVORITES(this.PRODUCT)
      this.setIsFav()
    },
    setIsFav() {
      let exists = false
      this.FAVORITES.forEach(fav => {
        if (fav.article === this.PRODUCT.article) {
          this.isFavorite = true
          exists = true
        }
      })
      if (exists === false)
        this.isFavorite = false
    },
    selectSize(selectedSize) {
      this.selectedSize = selectedSize
      let variants = this.PRODUCT.variants

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
      let variants = this.PRODUCT.variants
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
        let selectedVariant = this.PRODUCT.variants.filter(variant => (variant.color === this.selectedColor && variant.size === this.selectedSize))
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
    },
    async loadData() {
      await this.GET_DETAIL_PRODUCT(this.$route.params.product_id)
      this.data_color = this.initColorData
      this.data_size = this.initSizeData
      if (document.querySelector('input[name="color"]:checked'))
        document.querySelector('input[name="color"]:checked').checked = false

      if (document.querySelector('input[name="size"]:checked'))
        document.querySelector('input[name="size"]:checked').checked = false
      this.selectedColor = ''
      this.selectedSize = ''
      this.isFetching = true

    },
  },
  async mounted() {
    await this.loadData();
    this.setIsFav()
    this.reviews = this.PRODUCT.reviews
  },
  computed: {
    ...mapGetters(['PRODUCT', 'FAVORITES']),

    initColorData() {
      let variants = this.PRODUCT.variants
      let colors_list = Array.from(new Set(variants.map((variant) => variant.color)));
      return colors_list.map(color => {
        let qnt = variants.filter(variant => color === variant.color).reduce((total, variant) => total + variant.quantity, 0)
        return {'name': color, 'quantity': qnt, 'isActive': qnt > 0}
      });
    },
    initSizeData() {
      let variants = this.PRODUCT.variants
      let sizes_list = Array.from(new Set(variants.map((variant) => variant.size)));
      return sizes_list.map(size => {
        let qnt = variants.filter(variant => size === variant.size).reduce((total, variant) => total + variant.quantity, 0)
        return {'name': size, 'quantity': qnt, 'isActive': qnt > 0};
      });
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

}
</script>

<style lang="scss" scoped>
.image {
  width: 100%;
}


.author {
  font-size: $font-size18;
  display: flex;
  align-items: center;
  gap: $margin*1.5;
}

.author_img {
  display: flex;
  box-shadow: 0 4px 15px 0 rgba(0, 0, 0, 0.2);
  justify-content: center;
  align-items: center;
  font-size: $font-size22;
  font-weight: 600;
  color: white;
  background-color: darkcyan;
  border-radius: 50%;
  width: 40px;
  height: 40px;
}

.review_body {
  display: flex;
  flex-flow: column;
}

.review_header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: $margin;
}

.review {
  box-shadow: 0 4px 15px 0 rgba(0, 0, 0, 0.1);
  padding: $padding*2;
  margin-bottom: $margin*2;
  border-radius: $padding;
}

.slide-fade-enter-active {
  transition: all .3s ease;
}

.slide-fade-leave-active {
  transition: all .8s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}

.slide-fade-enter, .slide-fade-leave-to
  /* .slide-fade-leave-active до версии 2.1.8 */
{
  transform: translateX(10px);
  opacity: 0;
}
</style>