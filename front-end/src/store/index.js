import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    detailMovieInfo : null,
    communityMovie : null,
    selectMovie : null
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
