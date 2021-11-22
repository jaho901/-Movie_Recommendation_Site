<template>
  <div>
    <!-- {{movie.movie.like_users.length}} -->
    {{movie.movie}}

    <p>리뷰창</p>
    <review-list 
      v-for="review in review_list" :key="review.id"
      :movie="movie.movie" :review="review"
      @like-update="getReviews" @hate-update="getReviews"
        >
    </review-list>

    <review-form :movie="movie.movie"
       @updatereviews="getReviews">

    </review-form>

  </div>

  
</template>

<script>
import axios from 'axios'
import ReviewForm from './ReviewForm.vue'
import ReviewList from './ReviewList.vue'
// import ReviewForm from './ReviewForm.vue'
// import Review from '@/views/movies/Review.vue'
// import Review from './Review.vue'


const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieDetails',
  components:{
    ReviewList,
    ReviewForm,
    },
    data: function () {
      return {
        movie: {},
        review_list: {},
        update : true,
        content : null,
        newReview : null,
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
      const movieId = this.$route.params.movieId
      // console.log(movieId)
      // console.log(typeof(this.$route.params.movieId))
      
      axios({
        method: 'GET',
        url: `${SERVER_URL}/movies/${movieId}`,
        headers: this.setToken()  // 'JWT token~~~'
      })
        .then(res => {
          console.log(res)
          this.movie = res.data
          console.log(this.movie)
        })
        .catch(err => {
          console.log(err)
        })
      },
      getReviews: function () {
        const movieId = this.$route.params.movieId
        console.log(movieId)
        axios({
        method: 'get',
        url: `${SERVER_URL}/movies/${movieId}/review_create/`,
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          this.review_list = res.data
          // console.log('성공')
        })
        .catch(err => {
          console.log(err)
          console.log('실패')
        })
      },
      updateReview: function () {
        this.update = false
      },

    },
  created: function () {
    if (localStorage.getItem('jwt')) {
      // console.log(this.movie)
      this.setToken()
      this.getMovies()
      this.getReviews()
    } else {
      this.$router.push({ name: 'Login' })
    }

  },
}
</script>

<style>

</style>