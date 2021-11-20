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
    getReviews: function () {
      // const movieId = this.movie.id
      console.log( this.movie.id )

      axios({
        method: 'get',
        url: `${SERVER_URL}/movies/${this.movie.id}/review_create/`,
        headers: this.setToken()
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
    this.getReviews()
  }
}
</script>

<style>

</style>