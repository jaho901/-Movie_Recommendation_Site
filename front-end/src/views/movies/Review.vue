<template>
  <div>
    <p> 리뷰들 </p>
      <div >
        {{Reviews}}
      </div>

    <p>리뷰폼</p>
    <review-form :movie="movie">
      

    </review-form>
  </div>

</template>

<script>       
import ReviewForm from './ReviewForm.vue'
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  components: { ReviewForm },
  name : 'Review',
  props: {
    movie : Object,
  },
  component: {
    ReviewForm
  },
  data: function() {
    return {
      Reviews: null
      }
  },
  methods : {
     setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getMovies: function () {
      const movieId = this.movie.id
      // console.log(typeof(movieId))
      axios({
        method: 'GET',
        url: `${SERVER_URL}/movies/${movieId}/review`,
        headers: this.setToken(),  // 'JWT token~~~'
        // params: {movie_id: this.movie.id}
      })
        .then(res => {
          console.log(res)
          this.Reviews = res.data
        })
        .catch(err => {
          console.log(err)
        })
      }
  },
  created: function () {
    this.getMovies()
  }
  

  

}
</script>

<style>

</style>