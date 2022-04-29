<template>
  <div class="d-flex justify-content-center" v-if="$store.state.isLoading">
    <div class="spinner-border" role="status">
      <span class="visually-hidden">Loading...</span>
    </div>
  </div>
</template>

<script>
export default {
  name: "v-is-loading"
}
</script>

<style scoped>

</style>