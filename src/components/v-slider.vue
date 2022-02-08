<template>
  <div class="v-slider">
    <b-carousel
        id="carousel-1"
        v-model="slide"
        :interval="4000"
        controls
        indicators
        background="#ababab"
        img-width="1024"
        img-height="480"
        style="text-shadow: 1px 1px 2px #333;"
    >
      <b-carousel-slide
          caption="First slide"
          text="Nulla vitae elit libero, a pharetra augue mollis interdum."
          img-src="https://avatars.mds.yandex.net/get-zen_doc/3512693/pub_601b560f9117d423edcd00e0_601b7f9b9117d423ede63a2a/scale_1200"
      ></b-carousel-slide>

      <b-carousel-slide
          caption="Second slide"
          text="Nulla vitae elit libero, a pharetra augue mollis interdum."
          img-src="https://i.ytimg.com/vi/EiG7WM0zo0s/maxresdefault.jpg">
      </b-carousel-slide>

      <b-carousel-slide
          caption="Third slide"
          text="Nulla vitae elit libero, a pharetra augue mollis interdum."
          img-src="https://avatars.mds.yandex.net/i?id=1f1cb232d0e7ddab7d2b42430590f8d4-5307135-images-thumbs&n=13&exp=1">
      </b-carousel-slide>

      <b-carousel-slide
          caption="Forth slide"
          text="Nulla vitae elit libero, a pharetra augue mollis interdum."
          img-src="https://miro.medium.com/max/5120/1*2WysPd9LQiQ0vVBNw6R3ow.jpeg">
      </b-carousel-slide>
    </b-carousel>
  </div>
</template>

<script>
export default {
  name: "v-slider",
  data() {
    return {
    }
  },
  methods: {
  }
}

</script>

<style scoped>

</style>