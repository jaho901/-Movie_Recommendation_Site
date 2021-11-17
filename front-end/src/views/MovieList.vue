<template>
  <div>
    {{ movies }}
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'TodoList',
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
    getTodos: function () {
      axios({
        method: 'get',
        url: `${SERVER_URL}/movies/`,
        headers: this.setToken()  // 'JWT token~~~'
      })
        .then(res => {
          console.log(res)
          console.log(res.data)
          this.movies = res.data
        })
        .catch(err => {
          console.log(err)
        })
      },
    }
  // created: function () {
  //   if (localStorage.getItem('jwt')) {
  //     this.getTodos()
  //   } else {
  //     this.$router.push({ name: 'Login' })
  //   }
  // }
}
</script>
<style>

</style>