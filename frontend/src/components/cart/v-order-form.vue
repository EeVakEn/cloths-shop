<template>
  <div class="order-form container-fluid">
    <form class="row g-3">
      <section class="customer">
        <h3><i class="bi bi-person"/> Покупатель </h3>
        <router-link class="link" to="/log-in">Войти или зарегистрироваться</router-link>
        <hr/>
        <div class="row">
          <div class="col-md-6 my-2">
            <label for="firstname" class="form-label">Имя</label>
            <input type="text" class="form-control" id="firstname" required>
            <div class="invalid-feedback"></div>
          </div>
          <div class="col-md-6 my-2">
            <label for="lastname" class="form-label">Фамилия</label>
            <input type="text" class="form-control" id="lastname" required>
            <div class="invalid-feedback"></div>
          </div>
          <div class="col-md-6 my-2">
            <label for="firstname" class="form-label">Телефон</label>
            <input type="text" class="form-control" id="phone" required>
            <div class="invalid-feedback"></div>
          </div>
          <div class="col-md-6 my-2">
            <label for="lastname" class="form-label">Email</label>
            <input type="text" class="form-control" id="email" required>
            <div class="invalid-feedback"></div>
          </div>
        </div>

      </section>
      <section class="delivery">
        <h3><i class="bi bi-truck"/> Доставка</h3>
        <hr/>
        <div class="row">
          <div class="col-md-6 my-2">
            <label for="postal_code" class="form-label">Индекс</label>
            <input type="text" class="form-control" id="postal_code" required>
            <div class="invalid-feedback"></div>
          </div>
          <div class="col-md-6 my-2">
            <label for="region" class="form-label">Регион</label>
            <input type="text" class="form-control" name="region" id="region" required>
            <div class="invalid-feedback"></div>
          </div>
          <div class="col-md-6 my-2">
            <label class="form-label">Город</label>
            <dadata-suggestions
                :fullInfo.sync="city"
                type="ADDRESS"
            />
            <div class="invalid-feedback"></div>
          </div>
          <div class="col-md-6 my-2">
            <label for="street" class="form-label">Улица</label>
            <input type="text" class="form-control" name="street" id="street" required>
            <div class="invalid-feedback"></div>
          </div>
          <div class="col-md-6 my-2">
            <label for="house" class="form-label">Дом</label>
            <input type="text" class="form-control" name="house" id="house" required>
            <div class="invalid-feedback"></div>
          </div>
          <div class="col-md-6 my-2">
            <label for="room" class="form-label">Квартира</label>
            <input type="text" class="form-control" name="room" id="room" required>
            <div class="invalid-feedback"></div>
          </div>
        </div>
      </section>
      <section class="payment">
        <h3><i class="bi bi-credit-card"/> Оплата</h3>
        <hr/>
      </section>
    </form>
  </div>
</template>

<script>
export default {
  name: "v-order-form",
  data(){
    return{
      city: null
    }
  },
  mounted() {
  }
}
</script>

<style scoped>

</style>