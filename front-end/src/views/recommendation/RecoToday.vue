<template>
  <div>
    {{ user_movies }}
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: "RecoToday",
  data: function () {
    return {
      user_movies: null,
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
        method: 'GET',
        url: `${SERVER_URL}/recommendation/today_user_list/`,
        headers: this.setToken()  // 'JWT token~~~'
      })
        .then(res => {
          this.user_movies = res.data
          console.log(res)
          console.log('성공')
        })
        .catch(err => {
          console.log(err)
        })
      },
  },
  created : function() {
    this.getMovies()
  }
}
</script>

<style>

</style>