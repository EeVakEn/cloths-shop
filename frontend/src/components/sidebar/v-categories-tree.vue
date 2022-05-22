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
    <Transition>
      <div v-if="expanded">
        <v-categories-tree
            v-for="child in node.children"
            :key="child.name"
            :node="child"
            :depth="depth+1"
            :expanded="expanded"
        />
      </div>
    </Transition>


  </div>


</template>

<script>

export default {
  name: "v-categories-tree",
  props: {
    expanded: Boolean,
    node: Object,
    depth: {
      type: Number,
      default: 0,
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
  line-height: 3;
}
.link{
  color: $second-color !important;
}
.v-enter-active,
.v-leave-active {
  transition: opacity 0.2s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}
</style>