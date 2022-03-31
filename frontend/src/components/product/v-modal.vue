<template>
  <div class="modal_wrapper" ref="modal_wrapper">
    <span tabindex="0"></span>
    <div class='v-modal'>
      <div class="v-modal__close">
        <span class="v-modal__close-btn" @mouseover="hover=true" @mouseleave="hover=false" @click="closeModal">
          <b-icon class="v-modal__close-btn" v-if="!hover" icon="x"/>
          <b-icon class="v-modal__close-btn" v-else icon="x-square-fill"/>
        </span>
      </div>
      <div>
        <slot class="v-modal__content"></slot>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "v-modal",
  props: {
    submitAction: {
      type: String,
      default: 'Ok'
    }
  },
  data() {
    return {
      hover: false,
    };
  },
  methods: {
    subAction() {
      this.$emit('subAction')
    },
    closeModal() {
      this.$emit('closeModal')
    },
  },
  mounted() {
    let vm = this
    document.addEventListener('click', function (item) {
      if (item.target === vm.$refs['modal_wrapper']) {
        vm.closeModal()
      }
    })
  }
}
</script>

<style lang="scss">
.modal_wrapper {
  overflow-y: auto;
  position: fixed;
  display: flex;
  justify-content: center;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 20000;
  background: rgba(0, 0, 0, 0.38);
}

.v-modal {
  border-radius: 5px;
  position: relative;
  top: 100px;
  margin-left: 85px;
  padding: $padding;
  width: 900px;
  background-color: white;
  z-index: 20030;

  &__close {
    display: inline-block;
    position: absolute;
    top: $margin;
    right: $margin;
    font-size: 22px;
  }

  &__close-btn {
    color: $dark-color;
    width: 30px;
    height: 30px;
    transition: .5s;
  }

  &__content {
    display: flex;
    flex-flow: row wrap;
  }
}
</style>