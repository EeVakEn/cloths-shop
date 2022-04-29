import axios from "axios"

export default {
    async GET_PRODUCTS_FROM_API({commit}) { // метод для получение данных с API
        commit('SET_IS_LOADING', true)
        return await axios('/api/catalog/products/', { // axios запрос
            method: "GET"
        }).then((products) => { // если запрос прошел (статус 200)
            commit('SET_PRODUCTS_TO_STATE', products.data); // вызываем мутацию
            commit('SET_IS_LOADING', false)
            return products;
        }).catch((error) => { // иначе
            commit('SET_IS_LOADING', false)
            return error;
        })
    },
    async GET_PRODUCTS_WITH_CATEGORY({commit}, cat_slug) {
        commit('SET_IS_LOADING', true)
        return await axios(`/api/catalog/category/${cat_slug}/`, {
            method: "GET"
        }).then((products) => {
            commit('SET_PRODUCTS_TO_STATE_WITH_CATEGORY', products.data);
            commit('SET_IS_LOADING', false)
            return products.data;
        }).catch((error) => {
            commit('SET_IS_LOADING', false)
            return error
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
    GET_CATEGORY_BREADCRUMB({commit}, cat_slug) {
        commit('SET_IS_LOADING', true)
        return axios(`/api/catalog/breadcrumb/${cat_slug}/`, {
            method: "GET"
        }).then((breadcrumb) => {
            commit('SET_CAT_BREADCRUMB', breadcrumb.data);

            return breadcrumb.data;
        }).catch((error) => {
            return error
        })
    },
    async GET_DETAIL_PRODUCT({commit}, product_id) {

        commit('SET_IS_LOADING', true)
        return await axios(`/api/catalog/products/${product_id}/`, {
            method: "GET"
        }).then((product) => {
            commit('SET_PRODUCT', product.data);
            commit('SET_IS_LOADING', false)
            return product.data;
        }).catch((error) => {
            commit('SET_IS_LOADING', false)
            return error
        })
    },
    // async GET_PRODUCT_REVIEWS({commit}, product_id){
    //     return axios
    //         .get(`/api/catalog/products/${product_id}/reviews/`)
    //         .then((resp) => commit('SET_REVIEWS', resp.data))
    //         .catch(error=> {return error})
    // },
}