<template>
  <div>
    <h1>{{movie.title}}</h1>
    <img :src="imgSrc" alt="#">
    
  </div>
  
</template>

<script>
export default {
  name : 'MovieListRecentItem',
  props: {
    movie: Object
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