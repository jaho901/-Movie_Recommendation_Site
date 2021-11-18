<template>
  <div>
    {{movie}}
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieDetails',
  components:{
    
  },
  data: function () {
    return {
      movie: null,
    }
  },
  // methods :  {
  //   getMovie: function () {
  //     this.movie = this.$store.state.detailMovieInfo
  //   }

  // }
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getMovies: function () {
      const {movieId} = this.$route.params
      console.log(movieId)
      console.log(typeof(this.$route.params.movieId))
      
      axios({
        method: 'GET',
        url: `${SERVER_URL}/movies/${movieId}`,
        headers: this.setToken()  // 'JWT token~~~'
      })
        .then(res => {
          this.movie = res.data
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
    // console.log(this.$store.state.detailMovieInfo)
    // this.movie = this.$store.state.detailMovieInfo
  }
}
</script>

<style>

</style>