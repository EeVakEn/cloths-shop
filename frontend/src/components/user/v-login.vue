<template>
  <div class="container-fluid">
    <div class="d-flex flex-nowrap justify-content-center">
      <div style="margin: 63px">
        <h2>Вход</h2>
        <form class="reg_form" @submit.prevent="checkForm">
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
          </div>
          <div class="form-group mb-3">
            <label for="password">Пароль</label>
            <input
                class="form-control"
                :class="$v.form.password.$error ? 'is-invalid' : ''"
                type="password"
                id="password"
                placeholder="Введите пароль"
                v-model.trim="form.password"
            >
            <div v-if="$v.form.password.$dirty && !$v.form.password.required" class="invalid-feedback">
              Обязательное поле.
            </div>
          </div>
            <div v-if="errors.non_field_errors" class="alert alert-danger">
              {{ errors.non_field_errors[0] }}
            </div>
          <div class="mt-4 mb-3">
            <button type="submit" class="dark-button">Войти</button>
          </div>
        </form>
        <div  class="mb-5"  style="text-align: center" >
          <a class="link" @click="$router.push('/sign-up')">Зарегистрироваться</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import {validationMixin} from "vuelidate";
import {required} from 'vuelidate/lib/validators'

export default {
  mixins: [validationMixin],
  name: "v-login",
  data() {
    return {
      form: {
        username: '',
        password: '',
      },
      errors: [],
    }
  },
  methods: {
    async checkForm() {
      this.$v.form.$touch()
      if (!this.$v.form.$error) {
        this.$store.commit('SET_IS_LOADING', true)
        axios.defaults.headers.common['Authorization'] = ''
        localStorage.removeItem('token')
        const formData = {
          username: this.form.username,
          password: this.form.password
        }
        await axios
            .post('/api/token/login/', formData)
            .then(response => {
              const token = response.data.auth_token
              this.$store.commit('SET_TOKEN', token)
              axios.defaults.headers.common['Authorization'] = 'Token ' + token
              localStorage.setItem('token', token)
              this.$router.push('/account')
            })
            .catch(error => {
              console.log(error.response.data)
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
      username: {required},
      password: {required},
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