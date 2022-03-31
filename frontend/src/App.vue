<template>
  <div id="app">
    <v-main-wrapper></v-main-wrapper>
  </div>
</template>

<script>

import VMainWrapper from "./components/v-main-wrapper";

export default {
  name: 'App',
  components: {
    VMainWrapper

  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  margin-top: 80px;
}
</style>
