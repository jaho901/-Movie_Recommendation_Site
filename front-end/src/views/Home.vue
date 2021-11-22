<template>
  <div class="home">
   <p>저희 홈페이지에 처음이신가요?</p>
    <button @click="gotoSignup">넹!</button>
    <br>
    <button @click="gotoLogin">아니오</button>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
// import movie from '@/views/movies/Movie.vue'
// import axios from 'axios'

// const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  name: 'Home',
  components: {
    // movie
  },
  methods : {
    gotoSignup : function () {
      this.$router.push({name:'Signup'})
    },
    gotoLogin :function () {
      this.$router.push({name:'Login'})
    },
  }
}
</script>
