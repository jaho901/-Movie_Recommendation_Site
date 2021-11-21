<template>
  <div>
    <p>{{ nickname }}님의 프로필페이지입니다.</p>
    {{userData}}
    <!-- <h1>{{userData.username}}님의 프로필입니다!</h1> -->
    <div v-if="!itsMe" >
      <button @click="follow" v-if="followBoolen">팔로우</button>
      <button @click="follow" v-else>언팔로우</button>
    </div>
    <div v-else>
      <button @click="goToSetting">유저정보 변경</button>
      <button>팔로우한 목록</button>
      <button>팔로잉한 목록</button>
    </div>
  </div> 
</template>


<script>
// import MovieListItem from '@/views/movies/MovieListItem'
import axios from 'axios'
import jwtDecode from "jwt-decode"

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'profile',
  components:{
    
  },
  data: function () {
    return {
      userData : null,
      itsMe : null,
      userId : null,
      nickname : null,
      followBoolen: false,
      follower: null,
      following:null
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
    getUserProfile: function () {
      const token = localStorage.getItem('jwt')
      const user_id = jwtDecode(token).user_id
      const userId = this.$route.params.user_id
      // console.log(userId)
      axios({
          method: 'GET',
          url: `${SERVER_URL}/accounts/profile/${userId}/`,
          headers: this.setToken()
        })
          .then(res => {
            // console.log(res)
            // console.log('성공이여')
            this.userData = res.data
            this.nickname = res.data.nickname
              if (userId === user_id) {
                this.itsMe = true
                // console.log('나다')
              } else {
                this.itsME = false
              }
          })
          .catch(err => {
            console.log(err)
            console.log('실패')
          })

    },
    goToSetting: function() {
      this.$router.push({name:'Setting'})
    },
    follow : function() {
      const token = localStorage.getItem('jwt')
      const user_id = jwtDecode(token).user_id
      // console.log(this.$route.params.user_id)
      const profile_id = this.$route.params.user_id
      console.log(profile_id)
      const movieItem = {
        user : user_id,
        // movie: this.movieInfo.id,
        // community_title: this.community_title,
        // movie_title : this.movieInfo.title,
        // content : this.content,
        // poster_path: this.movieInfo.poster_path
        // image: this.image
        }
        axios({
          method: 'post',
          url: `${SERVER_URL}/accounts/${profile_id}/follow/`,
          data: movieItem,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            console.log('성공했슴다')
            this.followBoolen= res.data.follow
            this.follower= res.data.followes
            this.following= res.data.following
          })
          .catch(err => {
            console.log(err)
            console.log('실패')
          })

      },
      getData : function () {
         const token = localStorage.getItem('jwt')
          const user_id = jwtDecode(token).user_id
          // console.log(this.$route.params.user_id)
          const profile_id = this.$route.params.user_id
          console.log(profile_id)
          const movieItem = {
            user : user_id,
            // movie: this.movieInfo.id,
            // community_title: this.community_title,
            // movie_title : this.movieInfo.title,
            // content : this.content,
            // poster_path: this.movieInfo.poster_path
            // image: this.image
        }
        axios({
          method: 'get',
          url: `${SERVER_URL}/accounts/${profile_id}/follow/`,
          data: movieItem,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            console.log('성공했슴다')
            this.followBoolen= res.data.follow
            this.follower= res.data.followes
            this.following= res.data.following
          })
          .catch(err => {
            console.log(err)
            console.log('실패')
          })
      }
    },
  
 created: function () {
    if (localStorage.getItem('jwt')) {
      this.getUserProfile()
      this.getData()
      // console.log('로그인은됨')
    } else {
      this.$router.push({ name: 'Login' })
    }
  },
  computed: function() {
      // this.getData()
  }
  
}
</script>

<style>

</style>