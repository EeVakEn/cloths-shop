import Vue from 'vue'
import Router from "vue-router";
import VCatalog from "../components/catalog/v-catalog";
import VCart from "../components/cart/v-cart";
import VFavorites from "../components/favorites/v-favorites";
import VProduct from "../components/product/v-product";

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
                path: '/:cat_slug',
                name: 'category',
                component: VCatalog,
            },
            {
                path: '/product/:product_id',
                name: 'product',
                component: VProduct,
            }
        ]
    }
)

export default router;