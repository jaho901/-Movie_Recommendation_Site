<template>
    <div class="table-wrapper">
    <h2>Community</h2>
      <div class="overflow-auto">
        <center>
          <b-button style="width: 80%;" block variant="secondary" @click="writeContent">Create Community</b-button>
          <br>
          <pagi-list
            :list-array="communityList"
          >
          </pagi-list>
        </center>
      </div>
    <pre>


    </pre>
  </div>
</template>

<script>
import PagiList from '@/views/community/PagiList'

export default {
  name: "Community",
  components: {
    PagiList
  },
  data: function () {
    return {
      pageNum: 0
    }
  },
  methods: {
    writeContent: function() {
       this.$router.push({ name : 'CommunityForm'})
    },
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
    }
    return config
    },
  },
  computed: {
    communityList: function () {
      return this.$store.state.communityList
    },
    rows() {
      console.log(this.communityList.length)
      return this.communityList.length
    }
  },
  created : function() {
    this.$store.dispatch("communityList", this.setToken())
  }
}

</script>

<style>

</style>