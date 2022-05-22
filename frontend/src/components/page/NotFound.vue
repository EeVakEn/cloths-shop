<template>
<div style="text-align: center;  margin: 50px 0">
  <h2>Страницы не существует</h2>
  <h1  style="font-size: 400px;">404</h1>
  <button class="dark-button" @click="$router.push('/')">На главную</button>
</div>
</template>

<script>
export default {
  name: "NotFound"
}
</script>

<style scoped>

</style>