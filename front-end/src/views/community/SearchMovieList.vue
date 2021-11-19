<template>
  <div 
    @click="selectMovie" 
    :data-movie-title="result.title"
    v-show="result.filterCheck"
    >

    <img :src="imgSrc" alt="#">
    <h1>{{result.title}}</h1>
  </div>
</template>

<script>
export default {
  name: "SearchMovieList",
  props: {
    result : Object,
  },
  data : function () {
    return {
    }
  },
  methods : {
    selectMovie : function (event) {
      // 추후 수정
      console.log(event)
      this.$store.state.selectMovie = this.result
      // console.log(this.$store.state.selectMovie)
      // console.log(event.target.innerText)
      // this.click = true
      // const title = event.target.parentNode.dataset.movieTitle
      this.$emit("changeresult",this.result)
      this.$emit('clickidMovieInfo', this.result)

    }
  },
  computed: {
    imgSrc : function () {
      const imgsrc = this.result.poster_path
      return imgsrc
    },
    // ChangeResults : function () {
    //   if (this.click) {
    //     this.show = true
    //   } else {
    //     this.show = false
    //   } 
    // }
  }
}
</script>

<style>

</style>