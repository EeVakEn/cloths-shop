import axios from "axios";

export default {
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
    },
}