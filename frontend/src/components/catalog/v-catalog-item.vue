<template>

  <div class="v-catalog-item nopadding">

    <!--MODAL-->
    <transition name="fade" appear>
      <v-modal
          v-if="isInfoModalVisible"
          tabindex="-1"
          aria-hidden="true"
          rightBtnTitle="Add to cart"
          :product_data="product_data"
          @closeModal="closeModal"
      />
    </transition>
    <!--MODAL END-->

    <div class="v-catalog-cart">
      <div class="v-catalog-item__image-wrapper">
        <img
            class="link-img v-catalog-item__image"
            @click="$router.push(`/product/${product_data.article}`)"
            :src="product_data.image"
            :alt="product_data.image"/>
      </div>

      <div class="v-catalog-item__info">
        <div class="v-catalog-item__name">{{ product_data.name }}</div>

        <div class="v-catalog-item__colors-wrapper">
          <b>Цвет: </b>
          <div
              v-for="(color,index) in getColorStack"
              :key="index"
              :class="[color, 'v-catalog-item__color']"
              :data-microtip="colorToRu(color)"
          />
        </div>

        <div class="v-catalog-item__bottom">
          <div class="v-catalog-item__price">{{ product_data.price.toLocaleString() }} ₽</div>
          <div>
            <button class="dark-button" @click="showModal">
              В корзину
              <i class="bi bi-bag"/>
            </button>

            <button class="dark-button" @click="addToFavorites">
              <i class="bi bi-heart-fill" v-if="this.isFavorite"/>
              <i class="bi bi-heart" v-else/>
            </button>
          </div>

        </div>
      </div>
    </div>
  </div>

</template>

<script>
import VModal from "../product/v-modal";
import {mapGetters} from "vuex";

export default {
  name: "v-catalog-item",
  components: {VModal},
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
  data() {
    return {
      isInfoModalVisible: false,
      isFavorite: false,
    }
  },

  methods: {
    addToFavorites() {
      this.$emit('addToFavorites', this.product_data)
      this.isFavorite = !this.isFavorite
    },
    showModal() {
      this.isInfoModalVisible = true;
    },
    closeModal() {
      this.isInfoModalVisible = false;
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
    },
    isFav() {
      let exists = false
      this.FAVORITES.forEach(fav => {
        if (fav.article === this.product_data.article) {
          this.isFavorite = true
          exists = true
        }
      })
      if (!exists) {
        this.isFavorite = false
      }
    }
  },
  mounted() {
    this.isFav()
  },
  computed: {
    ...mapGetters(['FAVORITES']),
    getColorStack() {
      let colorSet = new Set()
      this.product_data.variants.forEach(function (o) {
        colorSet.add(o.color)
      })
      return Array.from(colorSet)
    }
  }
}
</script>

<style lang="scss">
.v-catalog-cart {
  display: flex;
  height: 100%;
  flex-direction: column;
  box-shadow: 0 0 4px rgba(0, 0, 0, 0.3);
  margin: $margin/2;
  background-color: $second-color;
}

.v-catalog-item {
  display: flex;
  flex-direction: column;

  &__info {
    display: flex;
    flex-flow: column;
    padding: $padding;
  }

  &__image-wrapper {
    height: 90%;
  }

  &__name {
    text-align: left;
    font-weight: bold;
    margin-bottom: 0;
  }

  &__description {
    text-align: left;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  &__colors-wrapper {
    display: flex;
    flex-flow: wrap row;
    align-items: center;
  }

  &__color {
    width: 20px;
    height: 20px;
    border-radius: 2px;
    border: solid 1px $dark-color;
    cursor: pointer;
    margin: 0 $margin/8;
  }

  &__bottom {
    display: flex;
    flex-flow: row nowrap;
    margin-top: $margin;
    justify-self: flex-end;
    justify-content: space-between;
    align-items: center;
  }

  &__price {
    line-height: 22px;
    font-size: 22px;
    font-weight: bold;
  }


  &__image {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>