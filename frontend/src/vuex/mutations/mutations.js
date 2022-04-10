export default {
    INIT_STORE: (state) => {
        if (localStorage.getItem('cart'))
            state.cart = JSON.parse(localStorage.getItem('cart'))
        else
            localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    SET_PRODUCTS_TO_STATE: (state, products) => { // заполняем state данными
        state.products = products.results;
        state.breadcrumb = []
    },
    SET_PRODUCTS_TO_STATE_WITH_CATEGORY: (state, products) => { // заполняем state данными
        state.products = products.results;
    },
    SET_BREADCRUMB: (state) => {
        state.breadcrumb = []
    },
    SET_CAT_BREADCRUMB: (state, breadcrumb) => {
        state.breadcrumb = breadcrumb.results;
    },
    SET_CATEGORIES_TO_STATE: (state, categories) => {
        state.categories = categories.results;
    },
    SET_CART: (state, item) => {
        const exists = state.cart.filter(i => i.variant_id === item.variant_id)
        if (exists.length !== 0) {
            exists[0].quantity = parseInt(exists[0].quantity) + parseInt(item.quantity)
        } else {
            state.cart.push(item)
        }
        localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    SET_FAVORITE: (state, product) => {
        if (state.favorites.includes(product)) {
            state.favorites.splice(state.favorites.indexOf(product), 1)
            product.isFavorite = false
        } else {
            product.isFavorite = true
            state.favorites.push(product);
        }
    },
    DEL_FROM_CART: (state, index) => {
        state.cart[index].quantity = 1;
        state.cart.splice(index, 1)
        localStorage.setItem('cart', JSON.stringify(state.cart))

    },
    DEL_ALL_FROM_CART: (state) => {
        state.cart.map(function () {
            state.cart[0].quantity = 1;
        })
        state.cart.splice(0);
        localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    INCREMENT_CART: (state, index) => {
        if (state.cart[index].quantity < 50)
            state.cart[index].quantity++
        localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    DECREMENT_CART: (state, index) => {
        if (state.cart[index].quantity > 1)
            state.cart[index].quantity--
        else
            state.cart.pop(index);
        localStorage.setItem('cart', JSON.stringify(state.cart))
    }
}