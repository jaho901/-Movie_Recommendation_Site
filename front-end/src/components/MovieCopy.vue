<template>
  <div id="mod">
    <vue-glide
      :perView="3"
      :autoplay="3000"
      :hoverpause="true"
      :bound="true"
    >
      <vue-glide-slide style="width: auto;" v-for="(movie, idx) in testMovies" :key="idx">
        <img style="margin: 50px;" :src="movie.poster_path" />
      </vue-glide-slide>
      <template slot="control">
          <div data-glide-dir="<" class="box-11">
            <b-button>prev</b-button>
          </div>
          <div data-glide-dir=">" class="box-11-1">
            <b-button>next</b-button>
          </div>
        </template>
    </vue-glide>
  </div>
</template>

<script>
// import MovieListItem from '@/components/MovieListItem'
import axios from 'axios'
import { Glide, GlideSlide } from 'vue-glide-js'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieList',
  components:{
    // MovieListItem
    [Glide.name]: Glide,
    [GlideSlide.name]: GlideSlide
  },
  data: function () {
    return {
      movies: [],
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
        url: `${SERVER_URL}/movies/movie_list/`,
        headers: this.setToken()  // 'JWT token~~~'
      })
        .then(res => {
          // console.log(res)
          // console.log(res.data)
          this.movies = res.data
          
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  computed: {
    testMovies: function() {
      return this.movies
    }
  },
  mounted: function () {
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