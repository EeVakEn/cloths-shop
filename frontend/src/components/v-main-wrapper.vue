<template>

  <div class="v-main-wrapper" :class="{'sidebar__open': isSidebarOpen}">
    <v-navbar/>
    <v-sidebar @isOpenSidebar="isOpenSidebar"/>
    <keep-alive>
      <router-view></router-view>
    </keep-alive>
  </div>

</template>

<script>
import {mapGetters} from "vuex";
import VSidebar from "./sidebar/v-sidebar";
import VNavbar from "./v-navbar";

export default {
  name: 'v-main-wrapper',
  components: {VNavbar, VSidebar},
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
  margin-left: 70px;
  transition: .4s;

}

.sidebar__open {
  margin-left: 350px;
}
</style>