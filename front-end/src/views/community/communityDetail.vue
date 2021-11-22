<template>
  <div>
    <button @click="gotoBack">back</button>
    <hr>
      {{this.communityInfo}}
    <hr>
    <h3>게시글 좋아요</h3>
    <span>
      <p @click="movieLike" v-if="!like">좋아요</p>
      <p @click="movieLike" v-else>좋아요취소</p>
      <p> {{this.likeCount}}명이 좋아합니다</p>
      <p @click="movieHate" v-if="!hate">싫어요</p>
      <p @click="movieHate" v-else>싫어요취소</p>
      <p>{{this.hateCount}} 명이 싫어합니다</p>
    </span>


    
    <!-- 여기는 리뷰창 -->
    <community-review
      v-for="review in review_list" :key="review.pk"
      :community="communityInfo" :review="review"
      @update="getCommunityDetail"
        >
    </community-review>

    <!-- 리뷰작성 -->
    <community-reivew-form
      :community_id="community_id"
      @update-reviews="getReviews"
    />


  </div>
</template>

<script>
import axios from 'axios'
import jwtDecode from "jwt-decode"
import CommunityReivewForm from './CommunityReivewForm.vue'
import CommunityReview from '@/views/community/CommunityReview'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  components: { CommunityReivewForm, CommunityReview },
  name:"communityDetail",
  data: function() {
    return {
      community_id: "",
      communityInfo: {},
      likeCount : 0,
      like : null,
      hateCount : 0,
      hate : null,
      review_list: {},
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
    getCommunityDetail: function () {
      
      const communityId = this.community_id
      console.log(communityId,"커뮤아이디")
      const token = localStorage.getItem('jwt')
      const user_id = jwtDecode(token).user_id
      axios({
        method: 'get',
        url: `${SERVER_URL}/community/${communityId}`,
        headers: this.setToken()  // 'JWT token~~~'
      })
        .then(res => {
          // console.log(res)
          console.log(res.data)
          this.communityInfo = res.data
          if (this.communityInfo.like_users.includes(user_id)) { 
              this.like = true
            } else {
              this.like = false
            }
            if (this.communityInfo.hate_users.includes(user_id)) { 
              this.hate = true
            } else {
              this.hate = false
            }
           this.likeCount = this.communityInfo.like_users.length
           this.hateCount = this.communityInfo.hate_users.length
          
        })
        .catch(err => {
          console.log(err)
        })
      
    },
    gotoBack: function() {
      this.$router.push({name:"Community"})
    },
    movieLike : function () { 
      const communityId = this.community_id
      const token = localStorage.getItem('jwt')
      const user_id = jwtDecode(token).user_id
      const likeItem = {
        user: user_id
      }
      // console.log(movieId)
      axios({
          method: 'post',
          url: `${SERVER_URL}/community/${communityId}/like/`,
          data: likeItem,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            console.log('리센트무비')
            this.like = res.data.like
            this.likeCount  = res.data.count
            this.getCommunityDetail()
          })
          .catch(err => {
            console.log(err)
            console.log('실패')
          })
    },
    movieHate : function () { 
      const communityId = this.community_id
      const token = localStorage.getItem('jwt')
      const user_id = jwtDecode(token).user_id
      const likeItem = {
        user: user_id
      }
      // console.log(movieId)
      axios({
          method: 'post',
          url: `${SERVER_URL}/community/${communityId}/hate/`,
          data: likeItem,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            console.log('리센트무비')
            this.hate = res.data.like
            this.hateCount  = res.data.count
            this.getCommunityDetail()
          })
          .catch(err => {
            console.log(err)
            console.log('실패')
          })
    },
    getReviews: function () {
        // const movieId = this.$route.params.movieId
      
        axios({
          method: 'get',
          url: `${SERVER_URL}/community/${this.community_id}/review_create/`,
          headers: this.setToken()
        })
        .then(res => {
          console.log(res,'겟리뷰')
          this.review_list = res.data
          // console.log('성공')
        })
        .catch(err => {
          console.log(err)
          console.log('실패')
        })
      
      },



  },
  created: function() {
    if (localStorage.getItem('jwt')) {
       
        let community = this.$route.params.community_id
        let communityId = parseInt(community)
        console.log(this.$store.state.communityList,'리뷰리스트')
        const wantCommunity = this.$store.state.communityList.filter(
          community => community.id === communityId
        )
        console.log(wantCommunity, '짜잔')
        this.communityInfo = wantCommunity[0]
        this.community_id = wantCommunity[0].id
        // console.log(typeof(communityId))
        this.setToken()
        this.getCommunityDetail()
        this.getReviews()
      } else {
        this.$router.push({ name: 'Login' })
      }
    
  }
}
</script>

<style>

</style>