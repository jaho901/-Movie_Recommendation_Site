<template>
  <div>
    <p>{{review.rank}}</p>
    <p>{{review}}</p>

    <p v-if="update">{{review.content}}</p>
    <input v-else type="text" value="content" v-model="newReview">

    <button @click="deleteReview(review)">삭제</button>
    <button @click="updateReview" v-if="update">수정</button>
    <button @click="pushReview" v-else>업데이트</button>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL


export default {
  name: 'ReviewList',
  props: {
    review: Object,
    movie: Object
  },
  data: function () {
    return {
      update : true,
      content : this.review.content,
      newReview : null
    }
  },
  methods:{
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    deleteReview: function (review) {
      const movieId = this.movie.id
      // console.log(this.review.id)
       axios({
        method: 'delete',
        url: `${SERVER_URL}/movies/${movieId}/review/${review.id}/delete`,
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          console.log('성공했다요')
          this.$emit('update-review')
        })
        .catch(err => {
          console.log(err)
          console.log('실패했다요')
        })
    },
    updateReview: function () {
      this.update = false
    },
    pushReview: function() {
      this.review.content = this.newReview
      this.update = true
    }
  }
}
</script>

<style>

</style>