<template>
  <div class="pt-3">
    <carousel-3d
      height="480"
      border="5"
      :autoplay="true"
      :count="movie13.length"
    >
      <slide style="border-color: #9d7809;" v-for="(movie, idx) in movie13" :index="idx" :key="idx">
        <template slot-scope="{ index, isCurrent, leftIndex, rightIndex }">
          <img 
            @click="movieDetailInfo(movie.id)" :data-index="index" 
            :class="{ current: isCurrent, onLeft: (leftIndex >= 0), onRight: (rightIndex >= 0) }" :src="movie.poster_path">
        </template>
      </slide>
    </carousel-3d>
  </div>
</template>

<script>
// import MovieListItem from '@/components/MovieListItem'
import { Carousel3d, Slide } from 'vue-carousel-3d'

export default {
  name: 'MovieList',
  components:{
    // MovieListItem
    Carousel3d,
    Slide
  },
  data: function () {
    return {
      movies: [],
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    movieDetailInfo: function(movie_id) {
      this.$router.push(
        { name : 'MovieDetails', 
          params: {
            movieId : movie_id,
          }
      })
    }
  },
  computed: {
    movie13: function () {
      return this.$store.state.movie13
    }
  }
}
</script>
<style>

</style>