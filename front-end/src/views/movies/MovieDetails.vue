<template>

  <div class="top" style="background-color: #1a1e23;">
      <div class="is-full featured_wrapper p-0">
        <img id="topId" src="https://mblogthumb-phinf.pstatic.net/20150903_161/kwwoolim_1441229176941Lfdyl_JPEG/32.jpg?type=w2" class="featured">
        <div class="title_wrapper">
            <h1 class="has-text-white">{{ movieTitle }}</h1>
            <br>
            <span style="font-size: 1.3rem;">관람객 평점: <b-icon icon="star-fill"></b-icon> {{ vote }}점</span>
            <br><br>
            <div>출연: {{ actors }}</div>
            <div>장르: {{ genres }}</div>
            <br>
            <div>{{ openDate }}  |  {{ runTime }}</div>
            <div>{{ grade }}</div>
            <div>국가: {{ country }}</div>
            <br>
            <div style="width: 50%"><span class="title is-1 has-text-white">{{ content }}</span></div>
        </div>
    </div>
    <div>
      <br>
      <h3 style="color: white; text-align: left; margin-left: 60px;">추천 영화 리스트</h3>
      <b-container class="bv-example-row">
        <b-row class="text-center">
          <b-col v-for="(smovie, idx) in simmilarMovie" :key="idx">
            <img @click="movieDetailInfo(smovie.id)" style="margin-bottom: 100px;" :src="smovie.poster_path" alt="" />
          </b-col>
        </b-row>
      </b-container>
    </div>
  </div>

</template>

<script>
import axios from 'axios'
// import ReviewForm from './ReviewForm.vue'
// import ReviewList from './ReviewList.vue'
// import youtubeList from './youtubeList.vue'
// import simmilar from '@/views/movies/simmilar.vue'
// import ReviewForm from './ReviewForm.vue'
// import Review from '@/views/movies/Review.vue'
// import Review from './Review.vue'
import _ from 'lodash'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieDetails',
  components:{
    // ReviewList,
    // ReviewForm,
    // youtubeList,
    // simmilar
    },
    data: function () {
      return {
        movie: null,
        review_list: {},
        update : true,
        content : null,
        newReview : null,
        movieTitle : "",
        youtubeList : [],
        simmilarMovie: [],
        imgsrc: "",
        actors: "",
        genres: "",
        openDate: "",
        runTime: "",
        country: "",
        grade: "",
        vote: "",
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
      const movieId = this.$route.params.movieId

      axios({
        method: 'GET',
        url: `${SERVER_URL}/movies/${movieId}`,
        headers: this.setToken()  // 'JWT token~~~'
      })
        .then(res => {
          console.log(res)
          this.movie = res.data
          // console.log(this.movie,'여기')
          this.movieTitle =res.data.movie.title
          this.simmilarMovie = res.data.similar_movies
          this.content = _.replace(res.data.movie.content, "[", "")
          this.content = _.replace(this.content, "]", "")
          this.imgsrc = res.data.movie.poster_path
          this.actors = res.data.movie.actor_1 + ',' + res.data.movie.actor_2 + ',' + res.data.movie.actor_3
          for (var genre of res.data.movie.genre) {
            this.genres = this.genres + genre.name + ','
          }
          this.openDate = res.data.movie.year + '년 ' + res.data.movie.month + '월 '
          this.runTime = res.data.movie.time
          this.country = res.data.movie.country
          this.grade = res.data.movie.grade[0].rating
          this.vote = res.data.movie.vote
        })
        .catch(err => {
          console.log(err)
        })
      },
      getReviews: function () {
        const movieId = this.$route.params.movieId
         axios({
          method: 'get',
          url: `${SERVER_URL}/movies/${movieId}/review_create/`,
          headers: this.setToken()
        })
        .then(res => {
          console.log(res)
          this.review_list = res.data
          // console.log('성공')
        })
        .catch(err => {
          console.log(err)
        })
      },
      updateReview: function () {
        this.update = false
      },
      getYoutubeList : function() {
        const YOUTUBE_URL = 'https://www.googleapis.com/youtube/v3/search'
        const YOUTUBE_KEY = "AIzaSyAl95MuzIshQD-mpyN5iNvM6oRcOE154Ag"
        let movie = this.$route.params.movieId
        let movieId = parseInt(movie)
        this.movieTitle = this.$store.state.communityMovie[movieId].title
        const params = {
          q: this.movieTitle,
          key: YOUTUBE_KEY,
          part: 'snippet',
          type: 'video',
          maxResults : 2
        }
          axios({
            method: 'get',
            url: YOUTUBE_URL,
            params,
          })
          .then(res => {
            console.log(res)
            this.youtubeList = res.data.items
          })
          .catch(err => console.log(err))
        },
      movieDetailInfo: function(movie_id) {
        this.$router.push(
          { name : 'MovieDetails', 
            params: {
              movieId : movie_id,
            }
        })
      }
    },
  
    created: function () {
      if (localStorage.getItem('jwt')) {
        let movie = this.$route.params.movieId
        let movieId = parseInt(movie)
        console.log(movieId)
        this.movieTitle = this.$store.state.communityMovie[movieId].title
        this.movie = this.$store.state.communityMovie[movieId]
        this.getYoutubeList()
        this.setToken()
        this.getMovies()
        this.getReviews()
      } else {
        this.$router.push({ name: 'Login' })
      }

    },
    watch :{
      getYoutubeList : function() {
        this.youtubeList = this.getYoutubeList()
      }
    },
    computed: {

    }
  }
</script>

<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@100;400;800&display=swap");

body,
html {
	background: #000000;
	padding: 0;
	margin: 0;
	padding-bottom: 6rem;
	font-family: "Montserrat", sans-serif;
	width: 100%;
}

img {
	-webkit-box-reflect: below 5px
		linear-gradient(transparent, transparent, rgba(0, 0, 0, 0.4));
	-webkit-transition: all 0.5s ease;
	-o-transition: all 0.5s ease;
	transition: all 0.5s ease;
}

.container img:hover {
	-webkit-transform: scale(1.1);
	-ms-transform: scale(1.1);
	transform: scale(1.1);
}

.featured_wrapper {
	position: relative;
}
#topId {
	width: 100%;
	width: 100%;
	height: 600px;
	-o-object-fit: cover;
	object-fit: cover;
	-o-object-position: top;
	object-position: top;
}


.title_wrapper {
  font-weight: bold;
	position: absolute;
	width: 120%;
	left: 2rem;
	bottom: 5rem;
	padding: 20px 40px;
	-webkit-box-sizing: border-box;
	box-sizing: border-box;
  text-align: left;
  color: white;
}
.title_wrapper h1 {
  font-size: 3rem;
	width: 70%;
}

@media (max-width: 768px) {
	.title_wrapper {
		text-align: center;
		left: 0;
	}
	.title_wrapper h1 {
		font-size: 32px !important;
		width: 100%;
	}
}

</style>