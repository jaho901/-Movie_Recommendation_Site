<template>
  <div style="background:#1a1e23">
    <movie-list></movie-list>
    <hr>
    <movie-list-recent></movie-list-recent>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList.vue'
import MovieListRecent from '@/components/MovieListRecent.vue'
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