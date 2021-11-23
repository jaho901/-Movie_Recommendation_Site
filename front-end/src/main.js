import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import Carousel3d from 'vue-carousel-3d'
import VueGlide from 'vue-glide-js'
import 'vue-glide-js/dist/vue-glide.css'


Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(Carousel3d)
Vue.use(VueGlide)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
