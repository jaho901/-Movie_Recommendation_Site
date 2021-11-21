<template>
  <div>
    {{ movies }}
  </div>
</template>

<script>
// import RecoMovieList from '@/views/recommendation/RecoMovieList'
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: "RecoWeek",
  components:{
    // RecoMovieList
  },
  data: function () {
    return {
      movies: null,
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
      console.log('hi')      
      axios({
        method: 'GET',
        url: `${SERVER_URL}/recommendation/recommend_by_day_of_week/`,
        headers: this.setToken()  // 'JWT token~~~'
      })
        .then(res => {
          this.movies = res.data
          console.log(res)
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