<template>
  <div>
    <p>리뷰내용</p>
    <input type="text" v-model="reviewContent">
    <button @click="createReview">작성하기</button>
  </div>
</template>

<script>
import axios from 'axios'
import jwtDecode from "jwt-decode"
const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  name: "CommunityReviewForm",
  data: function () {
    return {
      reviewContent: null,
    }
  },
  props: {
    community_id: Number
  },
  methods : {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    createReview: function () {
      const token = localStorage.getItem('jwt')
      const user_id = jwtDecode(token).user_id
      const ReviewItem = {
        user : user_id,
        community: this.community_id,
        rank: this.ratingValue,
        content : this.reviewContent
      }
      // console.log(this.reviewContent)
      // console.log(this.movie)
      if (ReviewItem.content) {
        axios({
          method: 'post',
          url: `${SERVER_URL}/community/${this.community_id}/review_create/`,
          data: ReviewItem,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res,'폼')
            // console.log('성공')
            this.$emit('update-reviews')
          })
          .catch(err => {
            console.log(err)
            // console.log('실패')
          })
        }
    },

    }

}
</script>

<style>

</style>