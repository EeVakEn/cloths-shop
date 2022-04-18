<template>
  <nav class="navbar">
    <div class="navbar-brand">
      <router-link to="/" class="navbar-item">
        <strong class="logo">yourwear</strong>
      </router-link>
    </div>
    <div class="navbar-menu">
      <div class="navbar-end">
        <div class="navbar-item">
          <router-link to="/sign-up">
            <i class="bi bi-person-plus"> Регистрация</i>
          </router-link>
          <router-link to="/log-in">
            <i class="bi bi-person"> Войти</i>
          </router-link>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "v-navbar"
}
</script>

<style scoped>
.navbar{
  font-size: 28px;
}
.logo{
  font-size: 28px;
}
</style>