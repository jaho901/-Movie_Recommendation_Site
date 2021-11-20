<template>
  <div>
    <hr>
    <h2>{{communityContents.user}}</h2>
    <p>{{communityContents.community_title}}</p>
    <p>{{communityContents.movie_title}}</p>
    <p>{{communityContents}}</p>

  </div>
</template>

<script>
export default {
  name : 'CommunityDetail',
  props: {
    communityContents : Object
  }
}

</script>

<style>

</style>