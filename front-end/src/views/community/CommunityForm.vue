<template>
  <div>
    <p>게시글 작성 페이지입니다</p>
    <!-- 영화제목 찾기용 입력 -->
    <input type="text"
      v-model.trim = "search_name"
      @keyup.enter="filtering"
      >
    <!-- 영화정보를 가져와서 선택하게 할 창 -->
    
    <search-movie-list
      v-for="result in clickByResult" :key="result.id"
      :result ="result"
      @changeresult="changeResults"
      >
    </search-movie-list>   
  
    <!-- 게시글 제목  -->
    <hr>
    <p>제목</p>
    <input type="text"
       v-model = "community_title"
      >
    <!-- 게시글 내용 -->
    <p>내용</p>
    <input type="text"
      v-model="content"
      >
    <br>
    <button>작성하기</button>

  </div>
</template>

<script>
import SearchMovieList from './SearchMovieList.vue'

export default {
  name: "CommunityForm",
  components : {
    SearchMovieList
  },
  data: function () {
    return {
      search_name : null,
      movie_title : null,
      community_title : null,
      content :null,
      movie_list : null,
      results: [],
    }
  },
  methods :  {
    getMovie : function () {
      this.movie_list = this.$store.state.communityMovie
      console.log(this.movie)
    },
    filtering : function () {
      // console.log(this.$store.state.communityMovie)
      let results = this.$store.state.communityMovie.filter(movie =>
        movie.title.includes(this.search_name)
        )
      this.results = results.map(result => {
        return {
          ...result,
          filterCheck : true,
          flag : false
        }
        
      })
      console.log(this.results)
    },
    changeResults : function(selectMovie) {
      
      this.results = this.results.map(result => {
        if (selectMovie.flag === false) {
          if (result===selectMovie) {
            return {
              ...selectMovie,
              flag: true
            }
          } else {
            return {
              ...result,
              filterCheck: !result.filterCheck
            }
          }
        } else {
          return {
            ...result,
            flag : false,
            filterCheck : true
          }
        }

      })   
    }
  },
  created : function  () {
    this.getMovie()
    console.log(this.movie_list)
  },
  computed : {
    clickByResult : function () {
      return this.results.filter(result => {
        return result.filterCheck
      });
    }
  }
     // 재 정재
    // 반복해서 hidden이란걸 넣을건데
    // 클릭빼고 전부 false 
  

}
</script>

<style>

</style>