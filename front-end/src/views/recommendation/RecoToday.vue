<template style="background-color: #1a1e23;">
  <div id="mod">
    <h1 style="color: white;">오늘의 블로거 {{ TodayUser.nickname }}의 영화 리스트!!!</h1>
    <pre>

    </pre>
    <vue-glide
      v-if="movieToday"
      :startAt="3"
      :focusAt="2"
      :perView="5"
      :autoplay="2500"
      class="demo"
    >
      <vue-glide-slide style="width: 100%;" v-for="(movie, idx) in movieToday" :key="idx">
        <img @click="movieDetailInfo(movie.id)" style="height: 400px;" :src="movie.poster_path" />
      </vue-glide-slide>
    </vue-glide>
  </div>
</template>

<script>
// import MovieListItem from '@/components/MovieListItem'
import { Glide, GlideSlide } from 'vue-glide-js'

export default {
  name: 'RecoToday',
  components:{
    // MovieListItem
    [Glide.name]: Glide,
    [GlideSlide.name]: GlideSlide
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    movieDetailInfo: function(movie_id) {
      window.scrollTo(0,0)
      this.$router.push(
        { name : 'MovieDetails', 
          params: {
            movieId : movie_id,
          }
      })
    }
  },
  computed: {
    movieToday: function () {
      return this.$store.state.movieToday
    },
    TodayUser: function () {
      return this.$store.state.TodayUser
    }
  }
}
</script>
<style scoped lang="scss">
#mod {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  .demo {
    .glide {
      &__slide {
        display: flex;
        border: none;
        height: 410px;
        align-items: center;
        justify-content: center;
        color: #aaa;
        font-size: 36px;
        font-weight: 600;
        border-radius: 5px;
        transition: all .3s;
        opacity: .3;
        &--active {
          border: none;
          color: #fff;
           opacity: 1;
          background: #1a1e23;
        }
      }
    }
  }
}
</style>