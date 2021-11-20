<template>
  <div>
    <p> 리뷰들 </p>
      <review-list 
        v-for="(review,idx) in review_list" :key="idx"
        :review = 'review' :movie = "movie"
        @update-review="getReviews"> 

      </review-list>
    <p>----------------------------------</p>
    <p>리뷰폼</p>
    <review-form :movie="movie"
      @update-review="getReviews">
      
    </review-form>
  </div>

</template>

<script>       
import ReviewForm from './ReviewForm.vue'
import ReviewList from './ReviewList.vue'
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name : 'Review',
  components: { 
    ReviewForm ,
    ReviewList
    },
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
      review_list: null,
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
      // console.log( this.movie.id )
      // if (this.movie.id) {
      //   const movieId = this.movie.id
      //   axios({
      //   method: 'get',
      //   url: `${SERVER_URL}/movies/${movieId}/review_create/`,
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
      // } else {
        const movieId =  this.$store.state.movieDetailInfo.id
        console.log(movieId)
        axios({
        method: 'get',
        url: `${SERVER_URL}/movies/${movieId}/review_create/`,
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
  conputed: function () {
    this.getReviews()
  },
  created: function () {
    this.getReviews()
  }
}
</script>

<style>

</style>