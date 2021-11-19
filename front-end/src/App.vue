<template>
  <div id="app">
    <div id="nav">
      <span v-if="isLogin">
        <router-link @click.native="logout" to="#">Logout</router-link> |
        <router-link :to="{ name: 'Movie' }">Movie</router-link> |
        <router-link :to="{ name: 'profile' }">profile</router-link>
        <!-- <router-link :to="{ name: 'MovieDetails' }">MovieDetails</router-link> | -->

      </span>
      <span v-else>
        <router-link :to="{ name: 'Signup' }">Signup</router-link> |
        <router-link :to="{ name: 'Login' }">Login</router-link>
      </span>
    </div>
    <router-view @login="isLogin=true"/>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
    }
  },
  methods: {
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Login' })
    },
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
        url: `${SERVER_URL}/movies/`,
        headers: this.setToken()  // 'JWT token~~~'
      })
        .then(res => {
          // console.log(res)
          // console.log(res.data)
          this.$store.state.communityMovie = res.data
          // console.log( this.$store.state.communityMovie)
        })
        .catch(err => {
          console.log(err)
        })
      }
  },
  created: function () {
    // 1. Vue Instance가 생성된 직후에 호출되어 jwt를 가져오기
    const token = localStorage.getItem('jwt')
    // 2. 토큰이 있으면
    if (token) {
      // 3. true로 변경하고 없으면 유지
      this.isLogin = true
    
    if (localStorage.getItem('jwt')) {
      this.getMovies()
    } else {
      this.$router.push({ name: 'Login' })
    }

    
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
