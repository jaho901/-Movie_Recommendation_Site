<template>
  <div>
    <button @click="writeContent">게시글 작성</button>
    <button>게시글 정보</button>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: "Community",
  components: {
  },
  data: function () {
    return {

    }
  },
  methods: {
    writeContent: function() {
       this.$router.push({ name : 'CommunityForm'})
       },
    getMovies: function () {
      axios({
        method: 'get',
        url: `${SERVER_URL}/community/`,
        headers: this.setToken()  // 'JWT token~~~'
      })
        .then(res => {
          // console.log(res)
          // console.log(res.data)
          this.$store.state.communityMovie = res.data
          console.log( this.$store.state.communityMovie)
        })
        .catch(err => {
          console.log(err)
        })
      }
    
    

  }
}
// 뭐 해리  --> 해리포터 라는걸 포함하고있는
// 해리 in movies 

// 인풋창 입력을 받아요

// 바로 밑에 입력에 대한 결과가 보이게
// 입력값 없으면 안보이게
// 있으면 그 안에 영화 제목들이 나오게 하기 위해서는
// 입력된 글자를 포함하는 조건으로  store state 에서 검색
// 반환값을 가져와서 입력되게 input tag 밑에 보이도록
// 드랍박스처럼 보일려면 기존 구조를 안뭉개게

// 영화제목 목록들 앱솔! 


// 검색할때 영화에 대한 정보를 가져올려면 axios 를 사용해야하기
// 때문에 store가 훨씬 효율적입니다.

// 직접 선택해서 영화 pk를 movie_id에 넣어서 넘겨주면
// 검색 // store 모드여ㅑㅇ화정보
// 선택 --django -- > model table  바로 저장
// 넘길때는 pk값 1:N 
// pk 저장 -- > 새 테이블에 저장되니까

</script>

<style>

</style>