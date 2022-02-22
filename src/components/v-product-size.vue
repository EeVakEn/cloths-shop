<template>
  <div class="size-wrapper">
    <input
        :id="size"
        :checked="isSelectedSize"
        class="size-wrapper__size__radio"
        name="size"
        type="radio"
        @change="selectSize"
    />
    <label :for="size" class="size-wrapper__size__label">{{size}}</label>
  </div>
</template>

<script>
export default {
  name: "v-product-size",
  props:{
    selectedSize: {
      type: String,
      default() {
        return "";
      }
    },
    size: {
      type:String,
      default(){
        return ""
      }
    }
  },
  methods:{
    selectSize(){
      this.$emit('selectSize', this.size)
    }
  },
  computed: {
    isSelectedSize(){
      return this.size===this.selectedSize
    }
  }
}
</script>

<style scoped>

</style>