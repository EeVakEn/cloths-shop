import Vue from 'vue'
import App from './App.vue'
import store from "./vuex/store"
import router from "./router/router"
import './assets/styles/styles.scss'
import axios from 'axios'
import { BootstrapVue } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
Vue.use(BootstrapVue)

Vue.config.productionTip = false
axios.defaults.baseURL = 'http://localhost:8000'

new Vue({
    render: h => h(App),
    store,
    router,
    axios,

}).$mount('#app')
