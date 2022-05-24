<template>
  <div class="container account">
    <div class="d-flex justify-content-between">
      <h2>Личный кабинет</h2>
      <button class="dark-button" @click="logout()">Выйти</button>
    </div>
    <div style="margin: 30px 0">
      Здравствуйте, <b>{{user.username}}</b>!
    </div>
    <div v-if="!orders.length"  style="margin: 30px 0">

      <div>
        Вы пока еще ничего не заказали
      </div>
      <div>
        <router-link to="/" style="color: white!important;" class="dark-button">Каталог</router-link>
      </div>
    </div>
    <div v-else style="margin: 30px 0">
      <h4>Ваши заказы</h4>
      <div
          class="order_card"
          style="margin: 0 0 50px 0; box-shadow: 4px 4px 8px 0 rgba(34, 60, 80, 0.2);"
          v-for="order in orders"
          :key="order.id"
      >
        <div class="order_card_body">

          <div>Номер заказа: {{ order.id }}</div>
          <div>Адрес доставки: {{ order.address }}</div>
          <div>Тип доставки: {{ order.delivery_type }}</div>
          <div>Статус: <b
              :class="order.track_status === 'Отменен'?'text-danger': 'text-success'">{{ order.track_status }}</b></div>


          <table class="table table-hover  table-light table-striped">
            <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Картинка</th>
              <th scope="col">Детали заказа</th>
              <th scope="col">Цена</th>
              <th scope="col">Количество</th>
              <th scope="col">Стоимость</th>
            </tr>
            </thead>
            <tbody>
            <tr
                v-for="(item, index) in order.items"
                :key="index"
            >
              <th scope="row">{{ index + 1 }}</th>
              <td>
                <img class="link-img" height="100"
                     @click="$router.push(`/product/${item.product.product.article}`)"
                     :src='"http://localhost:8000"+item.product.product.image+"/"'
                     alt="Картинка не найдена">
              </td>
              <td>
                <p @click="$router.push(`/product/${item.product.product.article}`)" class="link"><b>{{
                    item.product.product.name
                  }}</b></p>
                <div>Размер: {{ item.product.size }}</div>
                <div>Цвет: {{ item.product.color }}</div>
              </td>
              <td>
                <div>
                  {{ item.product.product.price.toLocaleString() }} ₽
                </div>
              </td>
              <td>
                <b>
                  {{ item.quantity }}
                </b>
              </td>
              <td>
                <b>
                  {{ (item.product.product.price * item.quantity).toLocaleString() }} ₽
                </b>
              </td>
            </tr>
            </tbody>
          </table>
          <div class="order_itogo">
            <div>Стоимость заказа: <b>{{order.cost}} ₽</b></div>
            <div>Стоимость доставки: <b>{{order.delivery_cost?order.delivery_cost.toLocaleString()+' ₽':'бесплатно'}}</b></div>
            <div>Итого: <b>{{order.total_cost}} ₽</b></div>
            <span style="align-self: flex-end" class="badge bg-dark">{{ order.created_at }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "v-account",
  data() {
    return {
      orders: [],
      user:{}
    }
  },
  methods: {
    logout() {
      axios
          .post('/api/token/logout/')
          .then(response => {
            console.log(response.data)
          }).catch(error => {
        console.log(JSON.stringify((error)))
      })

      axios.defaults.headers.common['Authorization'] = ''
      localStorage.removeItem('token')
      this.$store.commit('REMOVE_TOKEN')
      this.$router.push('/').catch(() => {
      })
    }
  },
  mounted() {
    this.$store.commit('SET_IS_LOADING', true)

    axios.get('api/users/me')
        .then(response => this.user = response.data)
        .catch(error => console.log(error))
    axios.get('/api/catalog/orders/')
        .then(response =>this.orders = response.data)
        .catch(error => {console.log(error)})
    this.$store.commit('SET_IS_LOADING', false)
  }
}
</script>

<style lang="scss" scoped>
.order_card{
  background-color: #F5F5F5;
  padding: 20px;
}
.order_card_body{
  display: flex;
  flex-flow: column;
}
.order_itogo{
  display: flex;
  flex-direction: column;
  align-self: flex-end;
}

</style>