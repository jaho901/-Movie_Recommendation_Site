<template>
  <div>
    <youtube-list v-for="(video,idx) in youtubeList"
     :key="idx"
      :video="video"
      />
    {{movieTitle}}
    {{content}}
    {{imgsrc}}
    <hr>
    <!-- {{this.movie.similar_movies}} -->
    <!-- {{simmilarMovie}} -->
    <simmilar
      v-for="smovie in simmilarMovie" :key="smovie.idx"
      :smovie="smovie"
      >
    </simmilar>
    <hr>
    <p>리뷰창</p>
    
    <review-list 
      v-for="review in review_list" :key="review.pk"
      :movie="movie.movie" :review="review"
      @like-update="getReviews" @hate-update="getReviews"
      @update-review="getReviews"
        >
    </review-list>

    <review-form :movie="movie.movie"
       @updatereviews="getReviews">

    </review-form>

  </div>
</template>

<script>
import axios from 'axios'
import ReviewForm from './ReviewForm.vue'
import ReviewList from './ReviewList.vue'
import youtubeList from './youtubeList.vue'
import simmilar from '@/views/movies/simmilar.vue'
// import ReviewForm from './ReviewForm.vue'
// import Review from '@/views/movies/Review.vue'
// import Review from './Review.vue'


const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieDetails',
  components:{
    ReviewList,
    ReviewForm,
    youtubeList,
    simmilar
    },
    data: function () {
      return {
        movie: {},
        review_list: {},
        update : true,
        content : null,
        newReview : null,
        movieTitle : "",
        youtubeList : [],
        simmilarMovie: [],
        imgsrc: ""
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
          this.content = res.data.movie.content
          this.imgsrc = res.data.movie.poster_path
          console.log(this.simmilarMovie,'여기')
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
          console.log(res,'겟리뷰')
          this.review_list = res.data
          // console.log('성공')
        })
        .catch(err => {
          console.log(err)
          console.log('실패')
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
            console.log(res.data.items,'디테일')
            this.youtubeList = res.data.items
          })
          .catch(err => console.log(err,'에러'))
        },
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

<style>

</style>