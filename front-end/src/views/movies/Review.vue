<template>
  <div>
    <p> 리뷰들 </p>
      <div >
        {{ review_list }}
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
  name : 'Review',
  components: { ReviewForm },
  props: {
    movie:{ 
      type: Object,
    }
  },
  component: {
    ReviewForm
  },
  data: function() {
    return {
      review_list: null
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
      // const movieId = this.movie.id
      console.log( this.movie.id )

      axios({
        method: 'GET',
        url: `${SERVER_URL}/movies/${this.movie}/review`,
        headers: this.setToken(),
        params: { movieId: this.movie.id }
      })
        .then(res => {
          console.log(res)
          this.review_list = res.data
          console.log('성공')
        })
        .catch(err => {
          console.log(err)
          console.log('실패')
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