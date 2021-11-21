<template>
  <div>
    
    <div>
      <button @click="valueChange" value="최신">최신</button>
      <button @click="valueChange" value="adventureMovies">모험</button>
      <button @click="valueChange" value="warMovies">전쟁</button>
      <button @click="valueChange" value="actionMovies">액션</button>
      <button @click="valueChange" value="musicalMovies">뮤지컬</button>
      <button @click="valueChange" value="animationMovies">애니메이션</button>
      <button @click="valueChange" value="criminalMovies">범죄</button>
      <button @click="valueChange" value="comedyMovies">코미디</button>
      <button @click="valueChange" value="dramaMovies">드라마</button>
      <button @click="valueChange" value="suspenseMovies">서스펜스</button>
      <button @click="valueChange" value="fantasyMovies">판타지</button>
      <button @click="valueChange" value="romanceMovies">멜로/로맨스</button>
      <button @click="valueChange" value="thrillerMovies">스릴러</button>
      <button @click="valueChange" value="mysteryMovies">미스터리</button>
      <button @click="valueChange" value="sfMovies">SF</button>
      <button @click="valueChange" value="horrorMovies">공포</button>
      <button @click="valueChange" value="documentaryMovies">다큐멘터리</button>
      <button @click="valueChange" value="familyMovies">가족</button>
      <button @click="valueChange" value="concertMovies">콘서트</button>
    </div>
    <div>
      연령별
      <button @click="ageChange">전체관람가능</button>
      <button>12세이상 관람가능</button>
      <button>15세이상 관람가능</button>
      <button>19세이상 관람가능</button>

    </div>
    <br>
      <div v-if="genreId==='최신'">
        <movie-list-recent-item
          v-for="(movie, idx) in movies" :key="idx"
            :movie="movie" class="bestMovie">
        </movie-list-recent-item >
      </div>
      <div v-else>
        <movie-genre-list v-for="gmovie in changeList" :key="gmovie.idx"
          :gmovie="gmovie" :genreName="genreName">
          
        </movie-genre-list>
      </div>
    <br>
    
  </div>
</template>

<script>
// import MovieListItem from '@/views/movies/MovieListItem'
import axios from 'axios'
import MovieListRecentItem from '@/views/movies/MovieListRecentItem.vue'
import MovieGenreList from '@/views/movies/MovieGenreList.vue'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieList',
  components:{
    MovieListRecentItem,
    MovieGenreList
  },
  data: function () {
    return {
      movies: [],
      genreMovie: null,
      genreId : "최신",
      changeList: null,
      genreName: null,
      age: null
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
        url: `${SERVER_URL}/movies/recent/`,
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
      getGenre : function () {
        axios({
        method: 'get',
        url: `${SERVER_URL}/movies/movie_by_genre/`,
        headers: this.setToken()  // 'JWT token~~~'
      })
        .then(res => {
          console.log(res.data)
          // console.log(res.data)
          // this.movies = res.data
          console.log('앙 기모띵')
          this.genreMovie = res.data
        })
        .catch(err => {
          console.log(err)
        })
      },
      valueChange : function (event) {
        console.log(event.target.innerText)
        this.genreName = event.target.innerText
        this.genreId = event.target.value
        const genreId = this.genreId
        for (const genre in this.genreMovie) {
          if (genre === genreId) {
            this.changeList = this.genreMovie[genre]
          }
        }
        console.log(this.changeList)
      },
      ageChange : function (event) {
        console.log(event)
      }
    },
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.getMovies()
      this.getGenre()
    } else {
      this.$router.push({ name: 'Login' })
    }
  },
}
</script>

<style>
.bestMovie {
  float: left
}

</style>