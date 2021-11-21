<template>
  <div>
    <!-- <h1>{{movie.title}}</h1> -->
    <img :src="imgSrc" alt="#">
    <p>{{movie.like_users.length}}</p>
    <p @click="movieLike" v-if="!like">좋아요</p>
    <p @click="movieLike" v-else>좋아요취소</p>
    <p>{{movie.like_users.length}} 명이 좋아합니다</p>
    <p @click="movieHate" v-if="!hate">싫어요</p>
    <p @click="movieHate" v-else>싫어요취소</p>
    <p>{{hateCount}} 명이 싫어합니다</p>
    <p>{{movie.hate_users.length}}</p>
    <p @click="getDataInfo">확인용</p>
    
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
      likeCount : 0,
      like : null,
      hateCount : 0,
      hate : null
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
            // console.log(res.data.count)
            // console.log(res.data.like)
            this.like = res.data.like
            this.likeCount = res.data.count
          })
          .catch(err => {
            console.log(err)
            console.log('실패')
          })
    },
    movieHate : function () { 
      const movieId = this.movie.id
      const token = localStorage.getItem('jwt')
      const user_id = jwtDecode(token).user_id
      const hateItem = {
        user: user_id
      }
      console.log(movieId)
      axios({
          method: 'post',
          url: `${SERVER_URL}/movies/${movieId}/hate/`,
          data: hateItem,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            console.log('성공')
            // console.log(res.data.count)
            // console.log(res.data.like)
            this.hate = res.data.hate
            this.hateCount = res.data.count
          })
          .catch(err => {
            console.log(err)
            console.log('실패')
          })
    },
    getDataInfo : function () {
      // const movieId = this.movie.id
      const token = localStorage.getItem('jwt')
      const user_id = jwtDecode(token).user_id
      // console.log(user_id)
      // console.log(this.movie.like_users.includes(user_id))
      if (this.movie.like_users.includes(user_id)) {
          // console.log('이미 눌리셨네용')
          this.like = true
          // this.likeCount = this.movie.like_users.length
      } else {
        this.like = false 
      }
    }
  },
  computed: {
    imgSrc : function() {
      const imgsrc = this.movie.poster_path
      this.getDataInfo()
      return imgsrc
    },
  },
  created : function() {
    this.getDataInfo()
    // this.movieHateCount()
  },
  
}
</script>

<style>

</style>