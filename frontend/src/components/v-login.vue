<template>
  <div class="container-fluid">
    <div class="d-flex flex-nowrap justify-content-center">
      <div >
        <h2>Вход</h2>
        <form class="reg_form" @submit.prevent="checkForm">
          <div class="form-group">
            <label for="email">Почта</label>
            <input
                class="form-control"
                :class="$v.form.email.$error ? 'is-invalid' : ''"
                type="email"
                id="email"
                placeholder="Введите email"
                v-model.trim="form.email"
            >
            <div v-if="$v.form.email.$dirty && !$v.form.email.required" class="invalid-feedback">
              Обязательное поле.
            </div>
            <div v-if="$v.form.email.$dirty && !$v.form.email.email" class="invalid-feedback">
              Пожалуйста, введите корректный адрес электронной почты.
            </div>
          </div>

          <div class="form-group">
            <label for="password1">Пароль</label>
            <input
                class="form-control"
                :class="$v.form.password1.$error ? 'is-invalid' : ''"
                type="password"
                name="password1"
                id="password1"
                placeholder="Введите пароль"
                v-model.trim="form.password1"
            >
            <div v-if="$v.form.password1.$dirty && !$v.form.password1.required" class="invalid-feedback">
              Обязательное поле.
            </div>
            <div v-if="$v.form.password1.$dirty && !$v.form.password1.minLength" class="invalid-feedback">
              Пароль должен содержать 6 символов.
            </div>
          </div>
          <button type="submit" class="dark-button">Войти</button>
        </form>
        <router-link :to="{name: 'sign-up'}">Зарегистрироваться</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import {validationMixin} from "vuelidate";
import {required, minLength, email} from 'vuelidate/lib/validators'

export default {
  mixins: [validationMixin],
  name: "v-login",
  data() {
    return {
      form: {
        email: '',
        password1: '',
      },
    }
  },
  methods: {
    checkForm() {
      this.$v.form.$touch()
      if (!this.$v.form.$error) {
        console.log('Валидация прошла успешно')
      }
    }
  },
  validations: {
    form: {
      email: {required, email},
      password1: {required, minLength: minLength(6)},
    }
  },
}
</script>

<style lang="scss" scoped>
.form-group {
  margin-bottom: $margin;
}

.reg_form {
  width: 500px;
}

.dark-button {
  width: 100%;
}
</style>