<template>
  <div>
    <hr>
    <img :src="imgSrc" alt="#">
    <h2 @click="goToUserProfile">{{communityContents.user.username}}</h2>
    <!-- <h2>{{communityContents}}</h2/> -->
    <p>{{communityContents.community_title}}</p>
    <p>{{communityContents.movie_title}}</p>

    <button @click="communityDetail">gotoDetail</button>
    <hr>
  </div>
</template>

<script>

export default {
  name : 'CommunityList',
  props: {
    communityContents : Object
  },
  data: function () {
    return {
      userInfo: null
    }
  },
  methods: {
    goToUserProfile: function () {
      console.log(this.communityContents.user.pk)
      this.$router.push({
        name: 'profile',
        params: {
          user_id: this.communityContents.user.pk
        }
      })
    },
    communityDetail : function () {
      // console.log(this.communityContents.id)
      const community_id = this.communityContents.id
      console.log(community_id)
      this.$router.push({name:"communityDetail",params:{community_id : community_id}})

    }
      
  },
  computed : {
    imgSrc : function () {
      const imgsrc = this.communityContents.poster_path
      return imgsrc
    }
  },
  
}

</script>

<style>

</style>