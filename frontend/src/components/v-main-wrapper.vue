<template>
  <div class="v-main-wrapper" :class="{'sidebar__open': isSidebarOpen}">
    <v-sidebar @isOpenSidebar="isOpenSidebar"/>
    <keep-alive>
      <router-view></router-view>
    </keep-alive>
  </div>

</template>

<script>
import {mapGetters} from "vuex";
import VSidebar from "./sidebar/v-sidebar";

export default {
  name: 'v-main-wrapper',
  components: {VSidebar},
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
  max-width: calc(100% - 100px);
  //padding-left: 80px;

  margin-left: 70px;
  transition: .4s;

}

.sidebar__open {
  margin-left: 350px;
}
</style>