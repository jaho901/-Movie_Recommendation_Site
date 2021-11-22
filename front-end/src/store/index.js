import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'

const YOUTUBE_URL = 'https://www.googleapis.com/youtube/v3/search'
const YOUTUBE_KEY = process.env.VUE_APP_YOUTUBE_API

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
        q: searchText+'예고편',
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
        // console.log(res.data.items)
        commit('SEARCH_YOUTUBE', res)
      })
      .catch(err => console.log(err))
    },
  },
  modules: {

  }
})
