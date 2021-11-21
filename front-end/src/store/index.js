import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    detailMovieInfo : null,
    communityMovie : null,
    selectMovie : null,
    loginUserID : null,
    movieDetailInfo: null,
  },
  mutations: {
    // DETAIL_MOVIE_INFO : function (state, movieInfo) {
    //     state.detailMovieInfo = movieInfo
    // }
  },
  actions: {
    // movieDetailInfo : function ({commit}, movieInfo) {
    //   commit('DETAIL_MOVIE_INFO', movieInfo)
    // }
  },
  modules: {

  }
})
