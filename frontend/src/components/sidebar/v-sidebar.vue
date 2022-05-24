<template>
  <div>
    <div :class="{'v-sidebar__visible':isOpen, 'v-sidebar__invisible':!isOpen}" class="v-sidebar">
      <div class="hamburger-button" @click="close_open_sidebar">
        <i v-if="!isOpen" class="bi bi-list"/>
        <i v-else class="bi bi-x"/>
      </div>
      <div v-if="isOpen">
        <div class="sidebar_content">
          <p class="v-sidebar_catalog_link link" @click=" $router.push('/').catch(()=>{})">
            Каталог
          </p>
          <v-categories-tree
              class="v-sidebar_tree"
              v-for="node in CATEGORIES"
              :key="node.name"
              :node="node"
              :isSidebarOpen="isOpen"
              :expanded="true"
          />

        </div>
        <div class="sidebar_layout" @click="isOpen=false"></div>
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
  watch: {
    '$route'(to, from) {
      if (to !== from) {
        this.isOpen = false;
      }
    }
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
  width: 60px;
  cursor: pointer;
  transition: .5s;
}

.hamburger-button:hover {
  background-color: $black
}

.v-sidebar {
  height: 100%;
  position: fixed;
  display: block;
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
  box-shadow: 16px 0 21px -6px rgba(0, 0, 0, 0.5);
}

.sidebar_content {
  padding-left: 70px;
  z-index: 5000 !important;
}

.v-sidebar__invisible {
  width: 60px;
}

.v-sidebar_catalog_link {

  font-size: 24px;
  color: white !important;
}
.sidebar_layout{
  position: fixed; /* Stay in place */
  left: 350px;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  background-color: rgb(0,0,0); /* Fallback color */
  background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
}
</style>