<template>
    <div class="cards">
      <b-row>
        <b-col cols="4">
          <div v-if="movieInfo" class="my-3"> 
            <b-card
              title="Card Title"
              :img-src="imgSrc"
              img-alt="Image"
              img-top
              img-width="280px"
              tag="article"
              class="mb-2"
              >
            </b-card>

            <b-card>
              {{this.movieInfoContent}}
            </b-card>
          </div>


          <div v-else>
            <b-card>
            <h3>아직 영화 선택을안했어요ㅠㅠ</h3>
            <h5>영화를 선택하시면 영화내용이 뜰거에용 쀼</h5>
            </b-card>
          </div>

        </b-col>
        <b-col cols="8">
          <b-card>
          <hr>
          <p style="color :white;">제목</p>
          <!-- <b-form-textarea
            id="textarea-state"
            :state="community_title.length >= 0"
            placeholder="Enter at least 10 characters"
            
            v-model = "community_title"
          ></b-form-textarea>
           -->
          <br>
          <!-- 게시글 내용 -->
          <p style="color: white;">내용</p>
          <br>
          <b-form-textarea
            id="textarea-rows"
            placeholder="Tall textarea"
            rows="20"
            v-model="content"
          ></b-form-textarea>

          <b-btn
            @click="createCommunity"
            style="margin-top: 20px;"
          >
          작성하기
          </b-btn>
          </b-card>
        </b-col>
      </b-row>
    </div>
</template>

<script>
// import SearchMovieList from './SearchMovieList.vue'
import axios from 'axios'
import jwtDecode from "jwt-decode"
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: "CommunityForm",
  components : {
    // SearchMovieList
  },
  data: function () {
    return {
      search_name : null,
      community_title : null,
      content :null,
      movie_list : null,
      results: [],
      movieInfo : null,
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
    },
    movieInfosave: function (movieInfo) {
      if (this.movieInfo == null) {
        this.movieInfo = movieInfo
        console.log(this.movieInfo)
      } else {
        this.movieInfo = null
        // console.log(this.movieInfo)
      }
    },
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    gotoCommunity: function () {
      this.$router.push({name:'Community'})
    },
    createCommunity: function () {
      const token = localStorage.getItem('jwt')
      const user_id = jwtDecode(token).user_id
      const movieItem = {
        user : user_id,
        movie: this.movieInfo.id,
        community_title: this.community_title,
        movie_title : this.movieInfo.title,
        content : this.content,
        poster_path: this.movieInfo.poster_path,
        // image: this.image
      }
      console.log(movieItem)
      if (movieItem.community_title && movieItem.movie_title && movieItem.content) 
      {
        axios({
          method: 'post',
          url: `${SERVER_URL}/community/community_create/`,
          data: movieItem,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            console.log('성공')
            this.gotoCommunity()
          })
          .catch(err => {
            console.log(err)
            console.log('실패')
          })


        }
    },
    // EditImage(){
    //   this.image = this.$refs.serveyImage.files
    //   console.log(this.image)
    // }
  
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

.cards {
   width: 100%;
   max-width: 300px;
   min-width: 200px;
   height: 400px;
   background-color: rgba(white,0.75);
   margin: 10px;
   border-radius: 10px;
   box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.24);
   border: 2px solid rgba(7, 7, 7, 0.12);
   font-size: 16px;   
   transition: all 0.3s ease;
   position: relative;
   display: flex;
   justify-content: center;
   align-items: center;
   flex-direction: column;
   cursor: pointer;
   transition: all 0.3s ease;
}

</style>