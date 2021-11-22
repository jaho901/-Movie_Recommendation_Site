import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'

const YOUTUBE_URL = 'https://www.googleapis.com/youtube/v3/search'
const YOUTUBE_KEY = "AIzaSyAl95MuzIshQD-mpyN5iNvM6oRcOE154Ag"
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
    communityList : null
  },
  mutations: {
    // DETAIL_MOVIE_INFO : function (state, movieInfo) {
    //     state.detailMovieInfo = movieInfo
    // }
    SEARCH_YOUTUBE: function (state, res) {
      state.youtubeVideos = res.data.items
    },
  },
  actions: {
    // movieDetailInfo : function ({commit}, movieInfo) {
    //   commit('DETAIL_MOVIE_INFO', movieInfo)
    // }
    searchYoutube: function ({ commit }, searchText) {
      const params = {
        q: searchText,
        key: YOUTUBE_KEY,
        part: 'snippet',
        type: 'video'
      }
      axios({
        method: 'get',
        url: YOUTUBE_URL,
        params,
      })
      .then(res => {
        console.log(res.data.items,'스토어')
        commit('SEARCH_YOUTUBE', res)
      })
      .catch(err => console.log(err,'에러'))
    },
  },
  modules: {

  }
})
