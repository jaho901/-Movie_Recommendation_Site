<template>
  <div>
    {{this.communityInfo}}
    <button @click="gotoBack">back</button>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name:"communityDetail",
  data: function() {
    return {
      community_id: this.$route.params.community_id,
      communityInfo: null
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
      axios({
        method: 'get',
        url: `${SERVER_URL}/community/${this.community_id}`,
        headers: this.setToken()  // 'JWT token~~~'
      })
        .then(res => {
          // console.log(res)
          console.log(res.data)
          this.communityInfo = res.data
        })
        .catch(err => {
          console.log(err)
        })

    },
    gotoBack: function() {
      this.$router.push({name:"Community"})
    }


  },
  created: function() {
    // console.log(this.$route.params.community_id)
    this.getCommunityDetail()
  }
}
</script>

<style>

</style>