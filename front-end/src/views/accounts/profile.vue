<template>
  <div>
    <p>{{ nickname }}님의 프로필페이지입니다.</p>
    {{userData}}
    <br>
    {{allData}}
    <!-- <h1>{{userData.username}}님의 프로필입니다!</h1> -->
    <div v-if="!itsMe" >
      <button @click="follow" v-if="followBoolen">팔로우</button>
      <button @click="follow" v-else>언팔로우</button>
    </div>
    <div v-else>
      <button @click="goToSetting">유저정보 변경</button>
    </div>
      <button @click="owChange">팔로우한 목록</button>
      <p v-if="owList">{{followerList}}</p>
      <button @clikc="ingChange">팔로잉한 목록</button>
      <p v-if="ingList">{{followingList}}</p>
    
    <p>팔로워 수  {{this.follower}}</p>
    <p>팔로잉 수  {{this.following}}</p>

    <hr>
    <h3>좋아요 눌린 영화</h3>
    <p>{{userLikeMovies}}</p>
    <h3>리뷰를 남긴 영화</h3>
    <p>{{reviewInMovies}}</p>
    <h3>작성 한 게시글</h3>
    <p>{{userCreateCommunity}}</p>
    <h3>좋아요눌린 게시글</h3>
    <p>{{userLikeCommunity}}</p>
    
  </div> 
</template>


<script>
// import MovieListItem from '@/views/movies/MovieListItem'
import axios from 'axios'
import jwtDecode from "jwt-decode"

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'profile',
  components:{
    
  },
  data: function () {
    return {
      userData : null,
      itsMe : null,
      userId : null,
      nickname : null,
      followBoolen: false,
      follower: 0,
      following: 0,
      allData : null,
      followerList : null,
      followingList : null,
      owList : true,
      ingList : true,
      userLikeMovies : [],
      reviewInMovies : [],
      userCreateCommunity : [],
      userLikeCommunity : []
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
    getUserProfile: function () {
      const token = localStorage.getItem('jwt')
      const user_id = jwtDecode(token).user_id
      const userId = this.$route.params.user_id
      // console.log(userId)
      axios({
          method: 'GET',
          url: `${SERVER_URL}/accounts/profile/${userId}/`,
          headers: this.setToken()
        })
          .then(res => {
            // console.log(res)
            // console.log('성공이여')
            // console.log(res.data,'여기염')
            this.allData = res.data
            this.userData = res.data.userInfo
            this.nickname = res.data.userInfo.nickname
            this.userLikeMovies = res.data.userLikeMovies
            this.reviewInMovies = res.data.reviewInMovies
            this.userCreateCommunity = res.data.userCreateCommunity
            this.userLikeCommunity = res.data.userLikeCommunity
            console.log(this.userLikeMovies)
            console.log(res.data,'유저데이터')
              if (userId === user_id) {
                this.itsMe = true
                // console.log('나다')
              } else {
                this.itsME = false
              }
              this.getData()
          })
          .catch(err => {
            console.log(err)
            console.log('실패')
          })

    },
    goToSetting: function() {
      this.$router.push({name:'Setting'})
    },
    follow : function() {
      const profile_id = this.$route.params.user_id
      console.log(profile_id)
      const movieItem = {
        user : profile_id,
        }
        axios({
          method: 'post',
          url: `${SERVER_URL}/accounts/${profile_id}/follow/`,
          data: movieItem,
          headers: this.setToken()
        })
          .then(res => {
            // console.log(res)
            console.log('성공했슴다')
            this.followBoolen= res.data.follow
            // console.log(res.data.followers)
            this.follower= res.data.followers
            this.following= res.data.followings
            // this.getData()
          })
          .catch(err => {
            console.log(err)
            console.log('실패')
          })

      },
      getData : function () {
        // const token = localStorage.getItem('jwt')
        // const user_id = jwtDecode(token).user_id
        const profile_id = this.$route.params.user_id
        // console.log(profile_id)
        axios({
          method: 'get',
          url: `${SERVER_URL}/accounts/${profile_id}/follow_list/`,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            console.log('성공했슴다1')
            if (res.data.followings.includes(profile_id)) {
              this.followBoolen = true
            } else {
              this.followBoolen = false
            }
              console.log(res.data.followers.length)
              this.follower = res.data.followers.length
              this.following = res.data.followings.length
              this.followerList = res.data.followers
              this.followingList = res.data.followings
          })
          .catch(err => {
            console.log(err)
            console.log('실패')
          })
        },
        owChange : function () {
        if (this.owChange === true) {
          this.owChange = false
        } else {
          this.owChange = true
        }
      },
      ingChange : function () {
        if (this.ingChange === true) {
          this.ingChange = false
        } else {
          this.ingChange = true
        }
      },
    },
  
    created: function () {
      if (localStorage.getItem('jwt')) {
        this.getUserProfile()
        this.getData()
        // this.getData()
        console.log('로그인은됨')
      } else {
        this.$router.push({ name: 'Login' })
      }
    },
  // computed: function() {
  //     // this.getData()
  // }
  
}
</script>

<style>

</style>