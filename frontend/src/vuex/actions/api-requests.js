import axios from "axios";
axios.defaults.baseURL = 'http://localhost:8000'
export default {
    GET_PRODUCTS_FROM_API({commit}) { // метод для получение данных с API
        return axios('/api/catalog/products/', { // axios запрос
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
        return axios('/api/catalog/categories/', { // axios запрос
            method: "GET"
        }).then((categories) => { // если запрос прошел (статус 200)
            commit('SET_CATEGORIES_TO_STATE', categories.data); // вызываем мутацию
            return categories;
        }).catch((error) => { // иначе
            console.log(error);
            return error;
        })
    },
    GET_PRODUCTS_WITH_CATEGORY({commit}, cat_slug){
        return axios(`/api/catalog/category/${cat_slug}/`, {
            method: "GET"
        }).then((products)=>{
            commit('SET_PRODUCTS_TO_STATE_WITH_CATEGORY', products.data);
            return products.data;
        }).catch((error)=>{
            return error
        })
    },
    GET_CATEGORY_BREADCRUMB({commit}, cat_slug){
        return axios(`/api/catalog/breadcrumb/${cat_slug}/`, {
            method: "GET"
        }).then((breadcrumb)=>{
            commit('SET_BREADCRUMB', breadcrumb.data);
            return breadcrumb.data;
        }).catch((error)=>{
            return error
        })
    }
}