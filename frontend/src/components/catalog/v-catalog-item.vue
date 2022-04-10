<template>

  <div class="v-catalog-item">

    <v-modal
        v-if="isInfoModalVisible"
        rightBtnTitle="Add to cart"
        :product_data="product_data"
        @closeModal="closeModal"
    />


    <div class="v-catalog-item__image-wrapper">
      <img class="v-catalog-item__image" :src="product_data.image"
           :alt="product_data.image">
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

      <div class="v-catalog-item__description">{{ product_data.description }}</div>
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
    isFav(){
      let exists = false
      this.FAVORITES.forEach(fav => {
        if (fav.article === this.product_data.article) {
          this.isFavorite = true
          exists = true
        }
      })
      if (!exists){
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
.v-catalog-item {
  display: flex;
  flex-direction: column;
  background-color: $second-color;
  width: 300px;
  height: 500px;

  &__info {
    display: flex;
    flex-flow: column;
    padding: $padding;
  }

  &__image-wrapper {
    width: 100%;
    height: 350px;
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