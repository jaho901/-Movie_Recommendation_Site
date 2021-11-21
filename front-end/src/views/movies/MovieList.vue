<template>
  <div>
    <ul>
      <movie-list-item v-for="(movie, idx) in movies" :key="idx"
        :movie="movie" class="bestMovie">
        </movie-list-item>
    </ul>
  </div>
</template>

<script>
import MovieListItem from '@/views/movies/MovieListItem'
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieList',
  components:{
    MovieListItem
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
    getMovies: function () {
      axios({
        method: 'get',
        url: `${SERVER_URL}/movies/movie_list/`,
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
    },
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.getMovies()
    } else {
      this.$router.push({ name: 'Login' })
    }
  }
}
</script>
<style>
.bestMovie {
  float: left
}

</style>