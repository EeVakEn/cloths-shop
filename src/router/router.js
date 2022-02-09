import Vue from 'vue'
import Router from "vue-router";
import VCatalog from "../components/catalog/v-catalog";
import VCart from "../components/cart/v-cart";

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
            }
        ]
    }
)


export default router;