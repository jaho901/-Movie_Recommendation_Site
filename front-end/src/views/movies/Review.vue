<template>
  <div>
    <p>리뷰폼</p>
    <review-form :movie="movie">
      

    </review-form>
  </div>

</template>

<script>       
import ReviewForm from './ReviewForm.vue'
export default {
  components: { ReviewForm },
  name : 'Review',
  props: {
    movie : Object
  },
  component: {
    ReviewForm
  },
  // data: function () {
  //     return: 
  // }

}
</script>

<style>

</style>