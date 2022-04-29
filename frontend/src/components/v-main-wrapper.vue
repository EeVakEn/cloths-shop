<template>

  <div class="v-main-wrapper" :class="{'sidebar__open': isSidebarOpen}">
    <v-navbar/>
<!--    <v-sidebar @isOpenSidebar="isOpenSidebar"/>-->

    <router-view></router-view>
    <v-is-loading></v-is-loading>
  </div>

</template>

<script>
import {mapGetters} from "vuex";
// import VSidebar from "./sidebar/v-sidebar";
import VNavbar from "./v-navbar";
import VIsLoading from "@/components/v-is-loading";

export default {
  name: 'v-main-wrapper',
  components: {VIsLoading, VNavbar, /*VSidebar*/},
  data() {
    return {
      isSidebarOpen: false,
    };
  },
  computed: {
    ...mapGetters([
      'CART',
    ])
  },
  methods: {
    isOpenSidebar(a) {
      this.isSidebarOpen = a;
    }
  },
}
</script>

<style lang="scss">
.v-main-wrapper {
  transition: .4s;

}

.sidebar__open {
  margin-left: 350px;
}
</style>