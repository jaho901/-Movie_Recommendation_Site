<template>
  <div>
    <h1>{{movie.title}}</h1>
    <img :src="imgSrc" alt="#">
    <br>
    <button @click="movieDetailInfo">상세정보</button>
  </div>
</template>

<script>
export default {
  name: "MovieListItem",
  props: {
    movie: Object
  },
  methods:{
    movieDetailInfo: function() {
      // console.log(this.movie)
      const movieInfo = this.movie
      this.$store.dispatch('movieDetailInfo', movieInfo )


      // console.log(this.movie.id)
      this.$router.push(
        { name : 'MovieDetails', 
          params: {
            movieId : this.movie.id,
            movie: this.movie
          } 
      })
    }
  },
  computed: {
    imgSrc : function() {
      const imgsrc = this.movie.poster_path
      return imgsrc
    }
  }
}
</script>

<style>

</style>