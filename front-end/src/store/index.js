import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    detailMovieInfo : null,
    communityMovie : null,
    selectMovie : null,
    loginUserID : null,
    movieDetailInfo: null,
    youtubeVideos: [],
    all : null,
    communityList : null,
    movieToday: null,
    TodayUser: null,
    movieWeek: null,
    movieKorea: null,
    movie13: null,
    movieFavorite: null,
  },
  mutations: {
    MOVIE_13(state, res) {
      state.movie13 = res
    },
    MOVIE_TODAY(state, res) {
      state.movieToday = res.movies
      state.TodayUser = res.user
    },
    MOVIE_WEEK(state, res) {
      state.movieWeek = res
    },
    MOVIE_KOREA(state, res) {
      state.movieKorea = res
    },
  },
  actions: {
    movie13({ commit }, token) {
      axios({
        method: 'get',
        url: `${SERVER_URL}/movies/movie_list/`,
        headers: token,
      })
      .then(res => {
        console.log('gpgp')
        commit('MOVIE_13', res.data)
      })
      .catch(err => console.log(err))
    },
    movieToday({ commit }, token) {
      axios({
        method: 'get',
        url: `${SERVER_URL}/recommendation/today_user_list/`,
        headers: token,
      })
      .then(res => {
        commit('MOVIE_TODAY', res.data)
      })
      .catch(err => console.log(err))
    },
    movieWeek({ commit }, token) {
      axios({
        method: 'get',
        url: `${SERVER_URL}/recommendation/recommend_by_day_of_week/`,
        headers: token,
      })
      .then(res => {
        commit('MOVIE_WEEK', res.data)
      })
      .catch(err => console.log(err))
    },
    movieKorea({ commit }, token) {
      axios({
        method: 'get',
        url: `${SERVER_URL}/recommendation/recommend_by_korea/`,
        headers: token,
      })
      .then(res => {
        commit('MOVIE_KOREA', res.data)
      })
      .catch(err => console.log(err))
    },
  },
  modules: {

  }
})
