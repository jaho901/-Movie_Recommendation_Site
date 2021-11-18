import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
// import MovieList from '@/views/movies/MovieList'
import Movie from '@/views/movies/Movie'
import MovieDetails from '@/views/movies/MovieDetails'
import profile from '@/views/accounts/profile'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/movies',
    name: 'Movie',
    component: Movie,
  },
  {
    path: '/movies/:movieId',
    name: 'MovieDetails',
    component: MovieDetails,
  },
  {
    path: '/accounts/profile',
    name: 'profile',
    component: profile,
  },


]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
