<template>
  <div class="color-wrapper">
    <input
        type="radio"
        name="color"
        :id="color"
        :class="['color-wrapper__color__radio', color]"
        @change="selectColor"
        :checked="isSelectedColor"
    />
    <label :for="color" :class="['color-wrapper__color__label', color]"/>
  </div>
</template>

<script>

export default {
  name: "v-product-color",
  props:{
    color:{
      type: String,
      default() {
        return "";
      }
    },
    selectedColor:{
      type: String,
      default() {
        return "";
      }
    }
  },
  methods:{
    selectColor(){
      this.$emit('selectColor', this.color)
    }
  },
  computed:{
    isSelectedColor() {
      return this.color === this.selectedColor;
    }
  }
}
</script>

<style scoped>

</style>