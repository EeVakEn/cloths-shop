import axios from "axios";

export default {
    GET_PRODUCTS_FROM_API({commit}) { // метод для получение данных с API
        return axios('http://localhost:8000/api/cloths_shop/products/', { // axios запрос
            method: "GET"
        }).then((products) => { // если запрос прошел (статус 200)
            commit('SET_PRODUCTS_TO_STATE', products.data); // вызываем мутацию
            return products;
        }).catch((error) => { // иначе
            console.log(error);
            return error;
        })
    },
    GET_CATEGORIES_FROM_API({commit}) { // метод для получение данных с API

        return axios('http://localhost:3000/categories', { // axios запрос
            method: "GET"
        }).then((categories) => { // если запрос прошел (статус 200)
            commit('SET_CATEGORIES_TO_STATE', categories.data); // вызываем мутацию
            return categories;
        }).catch((error) => { // иначе
            console.log(error);
            return error;
        })
    },
}