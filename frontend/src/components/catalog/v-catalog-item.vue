<template>

  <div class="v-catalog-item">

    <v-modal
        v-if="isInfoModalVisible"
        rightBtnTitle="Add to cart"
        :product_data="product_data"
        :colors="getColorStack"
        :sizes="getSizeStack"
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
        <div class="v-catalog-item__price">{{ this.product_data.price.toLocaleString() }} ₽</div>
        <b-button-group class="v-catalog-item__btn-grp">
          <b-button class="v-catalog-item__btn-grp__btn" @click="showModal">
            В корзину
            <b-icon icon="basket" scale="1"/>
          </b-button>
          <b-button class="v-catalog-item__btn-grp__btn" @click="addToFavorites">
            <b-icon v-if="isFavorite" icon="heart-fill" scale="1"/>
            <b-icon v-else icon="heart" scale="1"/>
          </b-button>
        </b-button-group>
      </div>
    </div>


  </div>
</template>

<script>
import VModal from "../product/v-modal";

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
      quantity: 1,
      isFavorite: false,
    }
  },

  methods: {
    addToFavorites() {
      this.$emit('addToFavorites', this.product_data)
      this.isFavorite = this.product_data.isFavorite
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
    }

  },
  activated() {
    this.isFavorite = this.product_data.isFavorite
  },
  mounted() {
    this.$set(this.product_data, 'quantity', 1)
  },
  computed: {
    getColorStack(){
      let colorSet = new Set()
      this.product_data.variants.forEach(function (o){
        colorSet.add(o.color)
      })
      return Array.from(colorSet)
    },
    getSizeStack(){
      let sizeSet = new Set()
      this.product_data.variants.forEach(function (o){
        sizeSet.add(o.size)
      })
      return Array.from(sizeSet)
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
    padding: $padding !important;
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
  &__info{
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
    padding: $padding/2 0;
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
  }

  &__color {
    width: 20px;
    height: 20px;
    border-radius: 2px;
    border: solid 1px $dark-color;
    cursor: pointer;
    margin: 0 $margin/3;
  }

  &__bottom {
    position: relative;
    display: flex;
    flex-flow: row nowrap;
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