import Vue from "vue"
import Vuex from "vuex"
import axios from "axios";

Vue.use(Vuex)

// чтобы создать API из json файла нужно прописать команду
// Например 'http://localhost:3000/products'
// json-server --watch file.json

let store = new Vuex.Store({ //Центральное хранилище наших данных
    state:{
        products:[] // записываем пустой массив
    },//состоение, здесь хранятся коллекции объекты
    mutations:{
        SET_PRODUCTS_TO_STATE:(state,products) =>{ // заполняем state данными
            state.products = products;
        }
    }, //синхронное(очередное) изменение данных в state
    actions:{
        GET_PRODUCTS_FROM_API({commit}) { // метод для получение данных с API
            return axios('http://localhost:3000/products', { // axios запрос
                method: "GET"
            }).then((products) => { // если запрос прошел (статус 200)
                commit('SET_PRODUCTS_TO_STATE', products.data); // вызываем мутацию
                return products;
            }).catch((error)=>{ // иначе
                console.log(error);
                return error;
            })
        }
    }, // тоже самое что и мутации только ассинхрона(выполняется без очереди не ожидая)
    getters:{
       PRODUCTS(state){
           return state.products;
       }
    }, //взять данные из state
});

export default store;