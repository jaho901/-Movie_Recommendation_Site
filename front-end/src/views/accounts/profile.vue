<template>
  <div>
    <p>프로필페이지입니다.</p>
    <h1>{{userData.username}}님의 프로필입니다!</h1>
  </div>
</template>


<script>
// import MovieListItem from '@/views/movies/MovieListItem'
import axios from 'axios'

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
    getMovies: function () {
      axios({
        method: 'get',
        url: `${SERVER_URL}/accounts/1`,
        headers: this.setToken()  // 'JWT token~~~'
      })
        .then(res => {
          // console.log(res)
          // console.log(res.data)
          this.userData = res.data
        })
        .catch(err => {
          console.log(err)
        })
      },
    },
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.getMovies()
    } else {
      this.$router.push({ name: 'Login' })
    }
  }
}
</script>

<style>

</style>