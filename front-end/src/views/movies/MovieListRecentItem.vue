<template>
  <div>
    <img :src="imgSrc" alt="#">
    <p>{{itemData}}</p>
    <p @click="movieLike" v-if="!like">좋아요</p>
    <p @click="movieLike" v-else>좋아요취소</p>
    <p>{{likeCount}} 명이 좋아합니다</p>
    <!-- <p @click="movieHate" v-if="!hate">싫어요</p>
    <p @click="movieHate" v-else>싫어요취소</p>
    <p>{{hateCount}} 명이 싫어합니다</p>
    <p>{{movie.hate_users.length}}</p> -->
    <!-- <p @click="getDataInfo">확인용</p> -->
  </div>
  
</template>

<script>
import axios from 'axios'
import jwtDecode from "jwt-decode"
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name : 'MovieListRecentItem',
  props: {
    movie: Object
  },
  data : function () {
    return {
      likeCount : this.movie.like_users.length,
      like : null,
      hateCount : 0,
      hate : null,
      itemData : this.movie
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
    movieLike : function () { 
      const movieId = this.movie.id
      const token = localStorage.getItem('jwt')
      const user_id = jwtDecode(token).user_id
      const likeItem = {
        user: user_id
      }
      console.log(movieId)
      axios({
          method: 'post',
          url: `${SERVER_URL}/movies/${movieId}/like/`,
          data: likeItem,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            console.log('성공')
            this.like = res.data.like
            this.getData()

          })
          .catch(err => {
            console.log(err)
            console.log('실패')
          })
    },

    
  },
  computed: {
    imgSrc : function() {
      const imgsrc = this.movie.poster_path
      return imgsrc
    },
  },
  created : function() {
    // this.getDataInfo()
    // this.movieHateCount()
  },
  
}
</script>

<style>

</style>