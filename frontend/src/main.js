import Vue from 'vue'
import App from './App.vue'
import store from "./vuex/store"
import router from "./router/router"
import './assets/styles/styles.scss'
import axios from 'axios'
import DadataSuggestions from "vue-dadata-suggestions";

Vue.use(DadataSuggestions, {
  token: "698bf101eea50d9aa4bce13d0672ccfb3365bc18",
  type: "ADDRESS"
});

Vue.config.productionTip = false
axios.defaults.baseURL = 'http://localhost:8000'

new Vue({
    render: h => h(App),
    store,
    router,
    axios,

}).$mount('#app')
