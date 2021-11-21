<template>
  <div>
    <p>{{ userData.nickname }}님의 프로필페이지입니다.</p>
    <!-- <h1>{{userData.username}}님의 프로필입니다!</h1> -->
      <button>팔로우</button>
      <button>언팔로우</button>
  </div>
</template>


<script>
// import MovieListItem from '@/views/movies/MovieListItem'
import axios from 'axios'
// import jwtDecode from "jwt-decode"

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'profile',
  components:{
    
  },
  data: function () {
    return {
      userData : null,
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
      // const token = localStorage.getItem('jwt')
      // const user_id = jwtDecode(token).user_id
      const userId = this.$route.params.user_id
      console.log(userId)
      axios({
          method: 'GET',
          url: `${SERVER_URL}/accounts/profile/${userId}/`,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            console.log('성공')
            this.userData = res.data
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
      console.log('로그인은됨')
    } else {
      this.$router.push({ name: 'Login' })
    }
  }
}
</script>

<style>

</style>