export default {
    SET_PRODUCTS_TO_STATE:(state,products) =>{ // заполняем state данными
        state.products = products;
    },
    SET_CART:(state, product) => {
        if(state.cart.length){
            let isExist = false;
            state.cart.map(function (item){
                if (item.article === product.article){
                    isExist = true;
                    item.quantity++;
                }
            })
            if(!isExist){
                state.cart.push(product)
            }
        } else state.cart.push(product)
    },
    DEL_FROM_CART:(state, index) => {
        state.cart.splice(index,1)
    },
    INCREMENT_CART:(state, index) => {
        if (state.cart[index].quantity < 50)
            state.cart[index].quantity++
    },
    DECREMENT_CART:(state, index) => {
        if (state.cart[index].quantity > 1)
            state.cart[index].quantity--
    }
}