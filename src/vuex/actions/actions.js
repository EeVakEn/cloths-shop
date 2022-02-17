export default {
    ADD_TO_CART({commit}, product) {
        commit('SET_CART', product);
    },
    DELETE_FROM_CART({commit}, index){
        commit('DEL_FROM_CART',index)
    },
    DELETE_ALL_FROM_CART({commit}){
        commit('DEL_ALL_FROM_CART')
    },
    INCREMENT_CART_ITEM({commit}, index){
        commit('INCREMENT_CART', index)
    },
    DECREMENT_CART_ITEM({commit}, index){
        commit('DECREMENT_CART', index)
    },
    ADD_TO_FAVORITES({commit}, product){
        commit('SET_FAVORITE', product)
    }
}