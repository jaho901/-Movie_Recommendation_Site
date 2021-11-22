<template>
  <div>
    <movie-list class="bestMovie"></movie-list>
    <hr>
    <movie-list-recent class="bestMovie"></movie-list-recent>
  </div>
</template>

<script>
import MovieList from '@/views/movies/MovieList.vue'
import MovieListRecent from '@/views/movies/MovieListRecent.vue'
export default {
  name: 'Movie',
  components: { MovieList, MovieListRecent },
}
</script>

<style scoped>
.bestMovie {
  float: left
}
</style>