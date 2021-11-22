<template>
  <div>
    <reco-today class="bestMovie"></reco-today>
    <hr>
    <reco-week class="bestMovie"></reco-week>
    <hr>
    <hr>
    <reco-korea></reco-korea>
  </div>
</template>

<script>
import RecoToday from '@/views/recommendation/RecoToday'
import RecoWeek from '@/views/recommendation/RecoWeek'
import RecoKorea from '@/views/recommendation/RecoKorea'

export default {
  name: 'Recommendation',
  components: {
    RecoToday,
    RecoWeek,
    RecoKorea,
  }
}
</script>

<style scoped>
.bestMovie {
  float: left
}
</style>