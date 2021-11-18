<template>
  <div>
    <p>게시글 작성 페이지입니다</p>
    <!-- 영화제목 찾기용 입력 -->
    <input type="text"
      v-model.trim = "search_name"
      >
    <!-- 영화정보를 가져와서 선택하게 할 창 -->
    <ul>
      <p>리스트가 들어올 자리입니다.</p>
    </ul>
    <!-- 게시글 제목  -->

    <input type="text"
       v-model = "community_title"
      >
    <!-- 게시글 내용 -->
    <input type="text"
      v-model="content"
      >

    {{movie_list}}
    {{this.result}}

  </div>
</template>

<script>
export default {
  name: "CommunityForm",
  data: function () {
    return {
      search_name : null,
      movie_title : null,
      community_title : null,
      content :null,
      movie_list : null,
      result: null
    }
  },
  methods :  {
    getMovie : function () {
      this.movie_list = this.$store.state.communityMovie
      console.log(this.movie)
    }
  },
  created : function  () {
      this.getMovie()
    },
  computed: {
    filtering : function () {
      const result = this.movie_list.filter(movie =>
        this.search_name in movie.title
        )
      return result
    }
  }

}
</script>

<style>

</style>