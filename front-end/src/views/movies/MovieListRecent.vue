<template>
  <div>
    <movie-list-recent-item
       v-for="(movie, idx) in movies" :key="idx"
        :movie="movie">
    </movie-list-recent-item>
    {{genreMovie}}
  </div>
</template>

<script>
// import MovieListItem from '@/views/movies/MovieListItem'
import axios from 'axios'
import MovieListRecentItem from '@/views/movies/MovieListRecentItem.vue'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieList',
  components:{
    MovieListRecentItem
    
  },
  data: function () {
    return {
      movies: [],
      genreMovie: null
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
    getMovies: function () {
      axios({
        method: 'get',
        url: `${SERVER_URL}/movies/recent/`,
        headers: this.setToken()  // 'JWT token~~~'
      })
        .then(res => {
          // console.log(res)
          // console.log(res.data)
          this.movies = res.data
        })
        .catch(err => {
          console.log(err)
        })
      },
      getGenre : function () {
        axios({
        method: 'get',
        url: `${SERVER_URL}/movies/movie_by_genre/`,
        headers: this.setToken()  // 'JWT token~~~'
      })
        .then(res => {
          console.log(res.data)
          // console.log(res.data)
          // this.movies = res.data
          console.log('앙 기모띵')
          this.genreMovie = res.data
        })
        .catch(err => {
          console.log(err)
        })
      }
    },
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.getMovies()
      this.getGenre()
    } else {
      this.$router.push({ name: 'Login' })
    }
  }
}
</script>

<style>

</style>