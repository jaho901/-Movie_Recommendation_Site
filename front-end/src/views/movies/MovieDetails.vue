<template>
  <div>
    {{movie}}
    <p>리뷰창</p>
    <review :movie="movie">
        
    </review>
  </div>

  
</template>

<script>
import axios from 'axios'
import Review from '@/views/movies/Review.vue'
// import Review from './Review.vue'


const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieDetails',
  components:{
    Review
  },
  data: function () {
    return {
      movie: this.$route.params.movie,
      review_list: null
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
      const {movieId} = this.$route.params
      // console.log(movieId)
      // console.log(typeof(this.$route.params.movieId))
      
      axios({
        method: 'GET',
        url: `${SERVER_URL}/movies/${movieId}`,
        headers: this.setToken()  // 'JWT token~~~'
      })
        .then(res => {
          this.movie = res.data
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
      },
      // getReviews: function () {
      // // const movieId = this.movie.id
      // console.log( this.movie.id )

      // axios({
      //   method: 'get',
      //   url: `${SERVER_URL}/movies/${this.movie.id}/review_create/`,
      //   headers: this.setToken()
      // })
      //   .then(res => {
      //     console.log(res)
      //     this.review_list = res.data
      //     console.log('성공')
      //   })
      //   .catch(err => {
      //     console.log(err)
      //     console.log('실패')
      //   })
      // }
    },
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.getMovies()
      // this.getReviews()
    } else {
      this.$router.push({ name: 'Login' })
    }
    // console.log(this.$store.state.detailMovieInfo)
    // this.movie = this.$store.state.detailMovieInfo
  },
  
}
</script>

<style>

</style>