import Vue from 'vue'
import Router from "vue-router";
import VCatalog from "../components/catalog/v-catalog";
import VCart from "../components/cart/v-cart";
import VFavorites from "../components/favorites/v-favorites";

Vue.use(Router)

let router = new Router(
    {
        routes: [
            {
                path: '/',
                name: 'catalog',
                component: VCatalog
            },
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
            }
        ]
    }
)


export default router;