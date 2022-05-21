import Vue from 'vue'
import Router from "vue-router";
import VCatalog from "../components/catalog/v-catalog";
import VCart from "../components/cart/v-cart";
import VFavorites from "../components/favorites/v-favorites";
import VProduct from "../components/product/v-product";
import VSignUp from "../components/user/v-sign-up";
import VLogin from "../components/user/v-login";
import VAccount from "../components/user/v-account";
import store from "../vuex/store";
import Contacts from "@/components/page/contacts";
import About from "@/components/page/about";

Vue.use(Router)

let router = new Router(
    {
        mode: 'history',
        routes: [
            {
                path: '/cart',
                name: 'cart',
                component: VCart,
                props: true,
            },
            {
                path: '/favorites',
                name: 'favorites',
                component: VFavorites,
                props: true,
            },
            {
                path: '/',
                name: 'catalog',
                component: VCatalog,
            },
            {
                path: '/category/:cat_slug',
                name: 'category',
                component: VCatalog,
            },
            {
                path: '/product/:product_id',
                name: 'product',
                component: VProduct,
            },
            {
                path: '/sign-up',
                name: 'sign-up',
                component: VSignUp,
            },
            {
                path: '/log-in',
                name: 'login',
                component: VLogin,
            },
            {
                path: '/account',
                name: 'account',
                component: VAccount,
                meta: {
                    requireLogin: true
                }
            },
            {
                path: '/contacts',
                name: 'contacts',
                component: Contacts,
            },
            {
                path: '/about',
                name: 'about',
                component: About,
            }
        ]
    }
)

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
        next('/log-in')
    } else {
        next()
    }
})


export default router;