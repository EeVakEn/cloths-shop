export default {
    SET_PRODUCTS_TO_STATE_WITH_CATEGORY: (state, products) => { // заполняем state данными
        state.products = products.products;
        state.breadcrumb = products.breadcrumb;
    },
    SET_PRODUCTS_TO_STATE: (state, products) => { // заполняем state данными
        state.products = products.products;
    },
    SET_CATEGORIES_TO_STATE: (state, categories) => {
        state.categories = categories.results;
    },
    SET_CART: (state, {product, quantity, selectedColor, selectedSize}) => {
        if (!(selectedColor === "" || selectedSize === "")){
            let isExist = false;
            state.cart.map(function (item) {
                if (item.article === product.article) {
                    if(item.selectedColor === selectedColor && item.selectedSize === selectedSize){
                        isExist = true;
                        item.quantity += quantity; // update state CART
                    }
                }
            })
            if (!isExist) {
                state.cart.push(product)
                state.cart[state.cart.length - 1].quantity = quantity
                state.cart[state.cart.length - 1].selectedColor = selectedColor
                state.cart[state.cart.length - 1].selectedSize = selectedSize
            }
        }
    },
    SET_FAVORITE: (state, product) => {
        if (state.favorites.includes(product)) {
            state.favorites.splice(state.favorites.indexOf(product),1)
            product.isFavorite = false
        }else {
            product.isFavorite = true
            state.favorites.push(product);
        }
    },
    DEL_FROM_CART: (state, index) => {
        state.cart[index].quantity = 1;
        state.cart.splice(index, 1)
    },
    DEL_ALL_FROM_CART: (state) => {
        state.cart.map(function () {
            state.cart[0].quantity = 1;
        })
        state.cart.splice(0);
    },
    INCREMENT_CART: (state, index) => {
        if (state.cart[index].quantity < 50)
            state.cart[index].quantity++
    },
    DECREMENT_CART: (state, index) => {
        if (state.cart[index].quantity > 1)
            state.cart[index].quantity--
        else
            state.cart.pop(index);
    }
}