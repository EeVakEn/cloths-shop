import Vue from 'vue'
import App from './App.vue'
import store from "./vuex/store"
import router from "./router/router"
import {BootstrapVue, BootstrapVueIcons} from 'bootstrap-vue'
import './assets/styles/styles.scss'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'



Vue.config.productionTip = false
Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)

new Vue({
    render: h => h(App),
    store,
    router,
}).$mount('#app')
