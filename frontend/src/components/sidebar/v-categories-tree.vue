<template>
  <div>
    <div
        class="container-fluid v-categories-tree"
        @click="expanded=!expanded"
    >

      <span
          class="link"
          @click="$router.push(`/category/${node.slug}`).catch(()=>{})"
          :style="{'margin-left':`${depth*20}px`}"
      >
        {{ node.name }}
      </span>
      <span v-if="hasChildren" >
        <i v-if="!expanded" class="bi bi-caret-right link"></i>
        <i v-else class="bi bi-caret-down link"></i>
      </span>
    </div>
    <div v-if="expanded">
      <v-categories-tree
          v-for="child in node.children"
          :key="child.name"
          :node="child"
          :depth="depth+1"
      />
    </div>

  </div>


</template>

<script>

export default {
  name: "v-categories-tree",
  props: {
    node: Object,
    depth: {
      type: Number,
      default: 0,
    }
  },
  data() {
    return {
      expanded: false,
    }
  },
  computed: {
    hasChildren() {
      return this.node.children.length
    }
  },
}
</script>

<style scoped lang="scss">
.v-categories-tree {
  text-align: left;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  border-bottom: solid 1px grey;
  z-index: 0;
}
.link{
  color: $second-color !important;
  z-index: 200;
}
</style>