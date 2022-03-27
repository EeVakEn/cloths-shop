import Vue from "vue"
import Vuex from "vuex"
import mutations from "./mutations/mutations";
import commonActions from "./actions/actions";
import apiRequests from "./actions/api-requests";
import getters from "./getters/getters";

Vue.use(Vuex)

// чтобы создать API из json файла нужно прописать команду
// Например 'http://localhost:3000/products'
// json-server --watch file.json

let store = new Vuex.Store({ //Центральное хранилище наших данных
    state: {
        products: [], // записываем пустой массив
        cart: [],
        favorites: [],
        categories: [],
        isAutenticated: false,
        token: '',
        isLoading: false,
    },//состоение, здесь хранятся коллекции объекты
    mutations, //синхронное(очередное) изменение данных в state
    actions: {...commonActions, ...apiRequests}, // тоже самое что и мутации только ассинхрона(выполняется без очереди не ожидая)
    getters, //взять данные из state
});

export default store;