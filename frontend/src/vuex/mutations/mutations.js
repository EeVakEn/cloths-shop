export default {
    INIT_CART: (state) => {
        if (localStorage.getItem('cart'))
            state.cart = JSON.parse(localStorage.getItem('cart'))
        else
            localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    INIT_FAVORITES: (state) => {
        if (localStorage.getItem('favorites'))
            state.favorites = JSON.parse(localStorage.getItem('favorites'))
        else
            localStorage.setItem('favorites', JSON.stringify(state.favorites))
    },
    INIT_STORE: (state) => {
        if (localStorage.getItem('token')){
            state.token = localStorage.getItem('token')
            state.isAuthenticated = true
        } else {
            state.token = ''
            state.isAuthenticated = false
        }
    },
    SET_IS_LOADING: (state, status) => {
        state.isLoading = status;
    },
    SET_TOKEN: (state, token) => {
        state.token = token
        state.isAuthenticated = true
    },
    REMOVE_TOKEN : (state) => {
        state.token = ''
        state.isAuthenticated = false
    },
    SET_PRODUCTS_TO_STATE: (state, products) => { // заполняем state данными
        state.products = products.results;
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
        let exists = false
        state.favorites.forEach(fav => {
            if (fav.article === product.article) {
                state.favorites.splice(state.favorites.indexOf(product), 1)
                product.isFavorite = false
                exists = true
            }
        })
        if (!exists) {
            product.isFavorite = true
            state.favorites.push(product);
        }
        localStorage.setItem('favorites', JSON.stringify(state.favorites))
    },
    SET_PRODUCT: (state, product) => {
        state.currentProduct = product
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
    },
    SET_CAT_DROP_VIS: (state) => {
        state.isVisibleCategoryDropdown = false
    },
}