<template>
  <div class="order-form container-fluid">
    <form class="row g-3">
      <h2>Оформление</h2>
      <section class="customer">
        <h3><i class="bi bi-person"/> Покупатель </h3>
        <router-link class="link" to="/log-in">Войти или зарегистрироваться</router-link>
        <hr/>
        <div class="row">
          <div class="col-md-6 my-2">
            <label for="firstname" class="form-label">Имя</label>
            <input type="text" v-model="firstname" class="form-control" id="firstname" required>
            <div class="invalid-feedback"></div>
          </div>
          <div class="col-md-6 my-2">
            <label for="lastname" class="form-label">Фамилия</label>
            <input type="text" v-model="lastname" class="form-control" id="lastname" required>
            <div class="invalid-feedback"></div>
          </div>
          <div class="col-md-6 my-2">
            <label for="phone" class="form-label">Телефон</label>
            <input type="text" v-model="phone" class="form-control" id="phone" required>
            <small>Например: +7(999)999-99-99</small>
          </div>
          <div class="col-md-6 my-2">
            <label for="email" class="form-label">Email</label>
            <input type="email" v-model="email" class="form-control" id="email" required>
            <small>Для получения информации о заказе и связи</small>
          </div>
        </div>

      </section>
      <section class="delivery">
        <h3><i class="bi bi-truck"/> Доставка</h3>
        <hr/>
        <div class="row">
          <div class="col-md-6 my-2">
            <label for="region">Регион</label>
            <dadata-suggestions
                class="form-control"
                id="region"
                v-model="region"
                :fullInfo.sync="addressfull"
                field-value="value"
                :options="regionOptions"
            />
            <small>Например: Омская обл</small>
          </div>

          <div class="col-md-6 my-2">
            <label for="city">Город</label>
            <dadata-suggestions
                class="form-control"
                v-model="city"
                id="city"
                :fullInfo.sync="addressfull"
                field-value="value"
                :options="cityOptions"
            />
            <small>Например: г Омск</small>
          </div>

          <div class="col-md-6 my-2">
            <label for="street">Улица и дом</label>
            <dadata-suggestions
                class="form-control"
                v-model="street"
                id="street"
                :fullInfo.sync="addressfull"
                field-value="value"
                :options="streetOptions"
            />
            <small>Например: ул Ленина</small>
          </div>

          <div class="col-md-6 my-2">
            <label for="room">Квартира</label>
            <input class="form-control" v-model="room" id="room"/>
            <small>Оставьте пустым, если нет номера квартиры</small>
          </div>
        </div>
        <div class="delivery_select">
          <h5>Выберите способ доставки</h5>
          <div class="raw">
            <label class="card-radio-btn">
              <input type="radio" name="demo" class="card-input-element d-none" id="demo1" checked="">
              <div class="card card-body">
                <div class="content_head">Курьер</div>
                <div class="content_sub">250,00 руб.</div>
              </div>
            </label>
            <label class="card-radio-btn">
              <input type="radio" name="demo" class="card-input-element d-none" value="demo2">
              <div class="card card-body">
                <div class="content_head">Отделение Почта России 644105</div>
                <div class="content_sub">200,00 руб.</div>
              </div>
            </label>
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
import IMask from 'imask'
export default {
  name: "v-order-form",
  data() {
    return {
      firstname: "",
      lastname: "",
      phone: "",
      email: "",

      region: "",
      city: "",
      street: "",
      house: "",
      room: "",

      addressfull: {},
      regionOptions: {
        bounds: "region-area",
        count: 5,
      },
      cityOptions: {
        bounds: "city-settlement",
        constraints: this.region,
        count: 5,
      },
      streetOptions: {
        bounds: "street-house",
        constraints: this.city,
        count: 5,
      },
      mask: ''
    };
  },
  mounted() {
    this.mask = new IMask(document.getElementById('phone'), {mask:'+7(000)000-00-00'})
  }
}
</script>

<style lang="scss" scoped>
.card {
  border: 2px solid rgba(0, 0, 0, 0.1);
  border-radius: 0.65rem;
}


/*Card Button CSS*/
.card-radio-btn {
  display: block;
}

.card-radio-btn .content_head {
  color: #333;
  text-align: left;
  font-size: 1.2rem;
  line-height: 30px;
  font-weight: 500;
}

.card-radio-btn .content_sub {
  color: #9e9e9e;
  text-align: right;
  font-size: 14px;
}

.card-input-element + .card {
  width: auto;
  margin-bottom: 10px;
  justify-content: center;
  color: var(--primary);
  border: 2px solid transparent;
  border-radius: 10px;
  text-align: center;
  box-shadow: 0 4px 25px 0 rgba(0, 0, 0, 0.1);
}

.card-input-element + .card:hover {
  cursor: pointer;
}

.card-input-element:checked + .card {
  border: 2px solid $dark-color;
  transition: border 0.5s;
}

.card-input-element:checked + .card::after {
  content: "✔";
  color: rgba(0, 100, 0, 0.6);
  border: solid 2px;
  border-radius: 50%;
  width: 25px;
  height: 25px;
  position: absolute;
  right: 10px;
  top: 10px;
  font-style: normal;
  font-size: 1rem;
  font-weight: 900;
  line-height: 1.32;
  animation-name: fadeInCheckbox;
  animation-duration: 0.5s;
}


@keyframes fadeInCheckbox {
  from {
    opacity: 0;
    transform: rotateZ(-20deg);
  }

  to {
    opacity: 1;
    transform: rotateZ(0deg);
  }
}

</style>