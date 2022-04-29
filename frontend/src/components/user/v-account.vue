<template>
  <div class="container-fluid account">
    <h1>Личный кабинет</h1>
    <button class="dark-button" @click="logout()">Выйти</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "v-account",
  methods: {
    async logout() {
      await axios
          .post('/api/token/logout')
          .then(response => {
            console.log(response.data)
          }).catch(error => {
            console.log(JSON.stringify((error)))
          })

      axios.defaults.headers.common['Authorization'] = ''
      localStorage.removeItem('token')
      this.$store.commit('REMOVE_TOKEN')
      this.$router.push('/').catch(()=>{})
    }
  }
}
</script>

<style scoped>

</style>