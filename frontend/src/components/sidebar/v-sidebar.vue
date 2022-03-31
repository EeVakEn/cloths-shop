<template>
  <div>
    <div :class="{'v-sidebar__visible':isOpen, 'v-sidebar__invisible':!isOpen}" class="v-sidebar">
      <div class="hamburger-button" @click="close_open_sidebar">
        <b-icon v-if="!isOpen" icon="arrow-bar-right"/>
        <b-icon v-else icon="arrow-bar-left"/>
      </div>
      <div v-if="isOpen">
        <div class="v-sidebar_catalog_link"
             @click="$router.push({name: 'catalog'}), $router.go()">
          Каталог
        </div>
        <v-categories-tree
            v-for="node in CATEGORIES"
            :key="node.name"
            :node="node"
            :isSidebarOpen="isOpen"
        />
      </div>
    </div>
  </div>

</template>

<script>
import {mapActions, mapGetters} from "vuex";
import VCategoriesTree from "./v-categories-tree";

export default {
  name: "v-sidebar",
  components: {VCategoriesTree},
  data() {
    return {
      isOpen: false,
    };
  },
  methods: {
    ...mapActions([
      'GET_CATEGORIES_FROM_API'
    ]),
    close_open_sidebar() {
      this.isOpen = !this.isOpen
      this.$emit('isOpenSidebar', this.isOpen)
    }
  },
  mounted() {
    this.GET_CATEGORIES_FROM_API()
  },
  computed: {
    ...mapGetters([
      'CATEGORIES',
    ])
  },
}
</script>

<style lang="scss">
.category {
  list-style-type: none;
}

.hamburger-button {
  display: flex;
  background-color: $dark-color;
  position: absolute;
  font-size: 40px;
  align-items: center;
  justify-content: center;
  top: 0;
  left: 0;
  height: 100%;
  width: 70px;
  cursor: pointer;
  transition: .5s;
}

.hamburger-button:hover {
  background-color: $black
}

.v-sidebar {
  height: 100%;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  background-color: $dark-color;
  color: white;
  overflow-x: hidden;
  transition: 0.2s;
  padding-top: 60px;

}

.v-sidebar__visible {
  width: 350px;
}

.v-sidebar__invisible {
  width: 70px;
}

.v-sidebar_catalog_link {
  text-align: left;
  margin-left: 100px;
  font-size: 24px;
  color: white !important;
  cursor: pointer;
}
</style>