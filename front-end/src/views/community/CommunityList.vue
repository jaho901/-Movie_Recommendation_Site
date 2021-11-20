<template>
  <div>
    <hr>
    <img :src="imgSrc" alt="#">
    <h2>{{communityContents.user.username}}</h2>
    <h2>{{communityContents}}</h2>
    <p>{{communityContents.community_title}}</p>
    <p>{{communityContents.movie_title}}</p>
    <hr>

  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name : 'CommunityList',
  props: {
    communityContents : Object
  },
  data: function () {
    return {
      userInfo: null
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
      const user_id = this.communityContents.user
      console.log(user_id)
      axios({
        method: 'GET',
        url: `${SERVER_URL}/accounts/${user_id}/`,
        headers: this.setToken()  // 'JWT token~~~'
      })
        .then(res => {
          // console.log(res)
          // console.log(res.data[0].username)
          this.userInfo = res.data
        })
        .catch(err => {
          console.log(err)
        
        })
      },
    },
  computed : {
    imgSrc : function () {
      const imgsrc = this.communityContents.poster_path
      return imgsrc
    }
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