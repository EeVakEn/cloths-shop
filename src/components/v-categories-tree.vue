<template>
  <div>
    <div
        class="v-categories-tree"
        :style="{'margin-left':`${depth*20+100}px`}"
    >
      <span v-if="hasChildren" @click="expanded=!expanded">
        <b-icon v-if="!expanded" icon="arrow-down-short" ></b-icon>
        <b-icon v-else icon="dash"></b-icon>
      </span>
      <span class="link">{{ node.name }}</span>

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
  data(){
    return{
      expanded: false,
    }
  },
  computed:{
    hasChildren(){
      return this.node.children.length
    }
  },
}
</script>

<style scoped lang="scss">
.v-categories-tree{
  font-size: $font-size18;
  text-align: left;
  cursor: pointer;
}
.link{
  display: inline-block;
  padding: 4px 8px;
  color: white;
  transition: .5s;
}
.link:hover{
  color: #555;
}
</style>