<template>
<div class="container">
  <div class="email-confirm">
    <h2>Подтверждение Email</h2>
    <img src="@/assets/images/mailbox.png" alt="Проверьтк почту" class="image_confirm_mail link-img"/>
    <p>Пожалуйста, проверьте свою почту</p>
    <small>Это необходимо для активации аккаунта</small>
  </div>
</div>
</template>

<script>
export default {
  name: "confirm-email"
}
</script>

<style scoped>
.email-confirm{
  text-align: center;
  margin: 50px 0 ;
}
.image_confirm_mail{
  max-width: 400px;
}
</style>