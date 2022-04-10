<template>
  <div>
    <div
        class="v-categories-tree"
        :style="{'margin-left':`${depth*20+100}px`}"
    >
      <span v-if="hasChildren" @click="expanded=!expanded">
        <i v-if="!expanded" class="bi bi-caret-right"></i>
        <i v-else class="bi bi-caret-down"></i>
      </span>
      <router-link class="link" :to="{name: 'category', params:{cat_slug:node.slug}}">
        {{ node.name }}
      </router-link>

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
      expanded: true,
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
  font-size: $font-size18;
  text-align: left;
  cursor: pointer;
}

.link {
  display: inline-block;
  padding: 4px 8px;
  color: white !important;
  transition: .5s;
}

.link:hover {
  color: #555;
}
</style>