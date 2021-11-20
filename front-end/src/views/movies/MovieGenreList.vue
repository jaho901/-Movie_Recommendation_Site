<template>
  <div>
    <p>{{genreName}} 영화 목록</p>
    {{gmovie}}
  </div>
</template>

<script>
export default {
  name: "MovieGenreList",
  props: {
    gmovie : Object,
    genreName : String
  }
}
</script>

<style>

</style>