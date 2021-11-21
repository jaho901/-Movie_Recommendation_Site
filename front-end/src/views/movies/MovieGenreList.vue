<template>
  <div>

    {{gmovie}}
  </div>
</template>

<script>
export default {
  name: "MovieGenreList",
  props: {
    gmovie : Object,
    genreName : String,
  }
}
</script>

<style>

</style>