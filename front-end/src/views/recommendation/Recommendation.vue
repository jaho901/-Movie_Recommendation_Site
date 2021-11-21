<template>
  <div>
    <reco-week class="bestMovie"></reco-week>
  </div>
</template>

<script>
import RecoWeek from '@/views/recommendation/RecoWeek'

export default {
  name: 'Recommendation',
  components: {
    RecoWeek,
  }
}
</script>

<style scoped>
.bestMovie {
  float: left
}
</style>