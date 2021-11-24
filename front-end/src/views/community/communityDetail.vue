<template>
  <div class="diagonal-hero-bg">
    <div class="stars">
      <div class="small"></div>
      <div class="medium"></div>
      <div class="big"></div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import jwtDecode from "jwt-decode"
// import CommunityReivewForm from './CommunityReivewForm.vue'
// import CommunityReview from '@/views/community/CommunityReview'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  // components: { CommunityReivewForm, CommunityReview },
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

<style lang="scss" scoped>
body {
  padding: 0;
  margin: 0 0 0 0;
}

.hero {
  display: inline-block;
  width: 100%;
  height: 400px;
  position: relative;

}
.diagonal-hero-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 550px;
  background: #2b5876;  /* fallback for old browsers */
  background: -webkit-linear-gradient(to right, #4e4376, #2b5876);  /* Chrome 10-25, Safari 5.1-6 */
  background: linear-gradient(to right, #4e4376, #2b5876); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
  
  z-index: -1;
  clip-path: polygon(0 0, 100% 0, 100% 100%, 0 80%);
}

// creates randomized star sizes
@function stars($n) {
  $value: '#{random(2000)}px #{random(2000)}px #767676';
  @for $i from 2 through $n {
    $value: '#{$value} , #{random(2000)}px #{random(2000)}px #767676';
  }
  @return unquote($value);
}

// store random stars
$stars-small: stars(700);
$stars-medium: stars(200);
$stars-big: stars(100);


.stars {
  z-index: -1;
  overflow: hidden;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  transition: opacity 1s ease-in-out;
}

.stars > .small {
  width: 1px;
  height: 1px;
  background: transparent;
  box-shadow: $stars-small;
  animation: starsAnimation 50s linear infinite;

  &:after {
    content: " ";
    position: absolute;
    top: 2000px;
    width: 1px;
    height: 1px;
    background: transparent;
    box-shadow: $stars-small;
  }
}

.stars > .medium {
  width: 2px;
  height: 2px;
  background: transparent;
  box-shadow: $stars-medium;
  animation: starsAnimation 100s linear infinite;

  &:after {
    content: " ";
    position: absolute;
    top: 2000px;
    width: 2px;
    height: 2px;
    background: transparent;
    box-shadow: $stars-medium;
  }
}

.stars > .big {
  width: 3px;
  height: 3px;
  background: transparent;
  box-shadow: $stars-big;
  border-radius: 100%;
  animation: starsAnimation 150s linear infinite;

  &:after {
    content: " ";
    position: absolute;
    top: 2000px;
    width: 3px;
    height: 3px;
    background: transparent;
    box-shadow: $stars-big;
    border-radius: 100%;
  }
}

// swap from/to values to reverse animation
@keyframes starsAnimation {
  from {
    transform: translateY(-2000px);
  }
  to {
    transform: translateY(0px);
  }
}
</style>