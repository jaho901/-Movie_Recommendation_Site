<template>
  <div style="background: #1a1e23">
    <img :src="imgSrc" alt="#">
    <p>{{this.movie}}</p>
    <p @click="movieLike" v-if="!like">좋아요</p>
    <p @click="movieLike" v-else>좋아요취소</p>
    <p> {{this.likeCount}}명이 좋아합니다</p>
    <p @click="movieHate" v-if="!hate">싫어요</p>
    <p @click="movieHate" v-else>싫어요취소</p>
    <p>{{this.hateCount}} 명이 싫어합니다</p>
    <p @click="movieFavorit" v-if="!favorite">찜뽕</p>
    <p @click="movieFavorit" v-else>찜뽕취소ㅠ</p>
    
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
      likeCount : null,
      like : null,
      hateCount : 0,
      hate : null,
      favorite : null
      // itemData : this.movie
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
      // console.log(movieId)
      axios({
          method: 'post',
          url: `${SERVER_URL}/movies/${movieId}/like/`,
          data: likeItem,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            console.log('리센트무비')
            this.like = res.data.like
            this.likeCount  = res.data.count
            this.$emit('like-change')
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
      const likeItem = {
        user: user_id
      }
      // console.log(movieId)
      axios({
          method: 'post',
          url: `${SERVER_URL}/movies/${movieId}/hate/`,
          data: likeItem,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            console.log('리센트무비')
            this.hate = res.data.like
            this.hateCount  = res.data.count
            this.$emit('like-change')
          })
          .catch(err => {
            console.log(err)
            console.log('실패')
          })
    },
    movieFavorit : function () { 
      const movieId = this.movie.id
      const token = localStorage.getItem('jwt')
      const user_id = jwtDecode(token).user_id
      const likeItem = {
        user: user_id
      }
      // console.log(movieId)
      axios({
          method: 'post',
          url: `${SERVER_URL}/movies/${movieId}/favorite/`,
          data: likeItem,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            console.log('리센트무비')
            this.favorite = res.data.favorit
  
            this.$emit('like-change')
          })
          .catch(err => {
            console.log(err)
            console.log('실패')
          })
    },
    getData : function () {
      const token = localStorage.getItem('jwt')
      const user_id = jwtDecode(token).user_id
      if (this.movie.like_users.includes(user_id)) { 
        this.like = true
      } else {
        this.like = false
      }
      if (this.movie.hate_users.includes(user_id)) { 
        this.hate = true
      } else {
        this.hate = false
      }
      if (this.movie.favorite_users.includes(user_id)) { 
        this.favorite = true
      } else {
        this.favorite = false
      }
      this.likeCount = this.movie.like_users.length
      this.hateCount = this.movie.hate_users.length
      
    }

    
  },
  computed: {
    imgSrc : function() {
      const imgsrc = this.movie.poster_path
      return imgsrc
    },
  },
  created: function () {
    this.getData()
  }
  // watch : {
  //   movieLike : function () {
  //     this.movie = this.getMovies()
  //   }
  // }
  
}
</script>

<style>

</style>