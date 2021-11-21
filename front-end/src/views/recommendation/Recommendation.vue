<template>
  <div>
    <reco-today class="bestMovie"></reco-today>
    <hr>
    <reco-week class="bestMovie"></reco-week>
  </div>
</template>

<script>
import RecoToday from '@/views/recommendation/RecoToday'
import RecoWeek from '@/views/recommendation/RecoWeek'

export default {
  name: 'Recommendation',
  components: {
    RecoToday,
    RecoWeek
  }
}
</script>

<style scoped>
.bestMovie {
  float: left
}
</style>