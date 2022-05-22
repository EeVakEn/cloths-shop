<template>

  <div class="v-main-wrapper" :class="{'sidebar__open': isSidebarOpen}">
    <div style="flex: 1 0 auto">
      <v-navbar/>
      <router-view></router-view>
      <v-is-loading></v-is-loading>
    </div>

    <v-footer style="flex: 0 0 auto"/>
  </div>

</template>

<script>
import {mapGetters} from "vuex";
// import VSidebar from "./sidebar/v-sidebar";
import VNavbar from "./v-navbar";
import VIsLoading from "@/components/v-is-loading";
import VFooter from "@/components/v-footer";

export default {
  name: 'v-main-wrapper',
  components: {VFooter, VIsLoading, VNavbar, /*VSidebar*/},
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
html,
body {
  height: 100%;
}
.v-main-wrapper {
  min-height: 100%;
  display: flex;
  flex-direction: column;
  transition: .4s;
}
@media (min-width: 768px){
  .v-main-wrapper {
    margin-left: 60px;
  }
}
.sidebar__open {
  margin-left: 350px;
}
</style>