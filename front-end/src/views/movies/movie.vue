<template>
  <div>
    <movie-list></movie-list>
    <hr>
    <movie-list-recent></movie-list-recent>
  </div>
</template>

<script>
import MovieList from '@/views/movies/MovieList.vue'
import MovieListRecent from '@/views/movies/MovieListRecent.vue'
export default {
  components: { MovieList, MovieListRecent },
}
</script>

<style>

</style>