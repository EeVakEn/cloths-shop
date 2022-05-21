<template>
  <div class="container-fluid">
    <div class="d-flex justify-content-center">
      <div>
        <h1>Регистрация</h1>
        <form class="reg_form" @submit.prevent="checkForm">
          <div class="form-group mb-3">
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

          <div class="form-group mb-3">
            <label for="username">Имя пользователя</label>
            <input
                class="form-control"
                :class="($v.form.username.$error || errors.username) ? 'is-invalid' : ''"
                type="text"
                id="username"
                placeholder="Введите имя пользователя"
                v-model.trim="form.username"
            >
            <div v-if="$v.form.username.$dirty && !$v.form.username.required" class="invalid-feedback">
              Обязательное поле.
            </div>
            <div v-if="$v.form.password1.$dirty && errors.username" class="invalid-feedback">
              <p v-for="(err,index) in errors.username" :key="index">
                {{ err }}
              </p>
            </div>
          </div>

          <div class="form-group mb-3">
            <label for="password1">Пароль</label>
            <input
                class="form-control"
                :class="($v.form.password1.$error || errors.password) ? 'is-invalid' : ''"
                type="password"
                name="password1"
                id="password1"
                placeholder="Введите пароль"
                v-model.trim="form.password1"
            >
            <div v-if="$v.form.password1.$dirty && !$v.form.password1.required" class="invalid-feedback">
              Обязательное поле.
            </div>
            <div v-if="$v.form.password1.$dirty && errors.password" class="invalid-feedback">
              <p v-for="(err,index) in errors.password" :key="index">
                {{ err }}
              </p>
            </div>
          </div>

          <div class="form-group">
            <label for="password2">Подтверждение пароля</label>
            <input
                class="form-control"
                :class="$v.form.password2.$error ? 'is-invalid' : ''"
                type="password"
                name="password2"
                id="password2"
                placeholder="Повторно введите пароль"
                v-model.trim="form.password2"
            >
            <div v-if="$v.form.password2.$dirty && !$v.form.password2.required" class="invalid-feedback">
              Обязательное поле.
            </div>
            <div v-if="$v.form.password2.$dirty && !$v.form.password2.sameAs" class="invalid-feedback">
              Пароль должен совпадать.
            </div>
          </div>
          <button type="submit" class="dark-button mb-2 mt-4">Зарегистрироваться</button>
          <div style="text-align: center">
            <p class="mb-5">Если есть аккаунт, <router-link class="link" to="log-in">войдите</router-link></p>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import {validationMixin} from 'vuelidate'
import {required, email, sameAs} from 'vuelidate/lib/validators'
import axios from "axios"

axios.defaults.baseURL = 'http://localhost:8000'

export default {
  components: {},

  mixins: [validationMixin],
  name: "v-sign-up",
  data() {
    return {
      form: {
        email: '',
        username: '',
        password1: '',
        password2: '',
      },
      errors: [],
    }
  },
  methods: {
    async checkForm() {
      this.$v.form.$touch()
      this.errors = []
      if (!this.$v.form.$error) {
        this.$store.commit('SET_IS_LOADING', true)
        console.log('Валидация прошла успешно')
        const formData = {
          email: this.form.email,
          username: this.form.username,
          password: this.form.password1
        }
        await axios
            .post('/api/users/', formData)
            .then(() => {
              this.$router.push({name: 'login'})
            })
            .catch(error => {
              if (error.response) {
                this.errors = error.response.data
              }
            })

        this.$store.commit('SET_IS_LOADING', false)
      }
    }
  },
  validations: {
    form: {
      email: {required, email},
      username: {required},
      password1: {required,},
      password2: {required, sameAsPassword: sameAs('password1')}
    }
  },
}
</script>

<style lang="scss" scoped>
.form-group {
  margin-bottom: $margin;
}
.reg_form{
  width: 500px;
}
@media screen and (max-width: 550px){
  .reg_form{
    width: auto;
  }
}
.dark-button {
  width: 100%;
}
</style>