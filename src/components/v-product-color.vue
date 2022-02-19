<template>
  <div class="color-wrapper">
    <input
        type="radio"
        name="color"
        :id="color"
        :class="['color-wrapper__color__radio', color]"
    />
    <label :for="color" :class="['color-wrapper__color__label', color]"/>
  </div>
</template>

<script>

export default {
  name: "v-product-color",
  props:{
    color: String,
    default(){
      return {}
    }
  },
  mounted() {
    console.log(this.color)
  }
}
</script>

<style scoped>

</style>