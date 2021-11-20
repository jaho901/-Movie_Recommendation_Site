<template>
  <div>
    <p> 리뷰들 </p>
      <div >
        {{movie}}
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
    movie:{ 
      type: Object,
    }
  },
  component: {
    ReviewForm
  },
  data: function() {
    return {
      Reviews: []
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
      console.log(movieId )

      axios({
        method: 'GET',
        url: `${SERVER_URL}/movies/${movieId}/review`,
        headers: this.setToken(),
      })
        .then(res => {
          console.log(res)
          this.Reviews = res.data
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