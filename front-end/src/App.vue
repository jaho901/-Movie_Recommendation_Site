<template>
  <div id="app">
    <div id="nav">
      <input type="checkbox" id="burger-toggle">
      <label for="burger-toggle" class="burger-menu">
        <!-- <p>MENU</p> -->
        <div class="line"></div>
        <div class="line"></div>
        <div class="line"></div>
      </label>
      <span id="nav-item">
        Profile
      </span>
      <div class="menu">
        <div class="menu-inner">
          <div v-if="isLogin">
            <ul class="menu-nav">
              <li class="menu-nav-item"><router-link class="menu-nav-link" :to="{ name: 'Movie' }"><span>
                    <div>Home</div>
                  </span></router-link></li>
              <li class="menu-nav-item"><router-link class="menu-nav-link" :to="{ name: 'Community' }"><span>
                    <div>Community</div>
                  </span></router-link></li>
              <li class="menu-nav-item"><router-link class="menu-nav-link" :to="{ name: '#' }"><span>
                    <div>Favorite</div>
                  </span></router-link></li>
              <li class="menu-nav-item"><router-link class="menu-nav-link" :to="{ name: 'Recommendation' }"><span>
                    <div>Recommend</div>
                  </span></router-link></li>
            </ul>
          </div>
          <div v-else>
            <h1>저희 홈페이지에 처음이신가요?</h1>
          </div>
          <div class="gallery">
            <div class="title">
              <p>Sora Gallery</p>
            </div>
            <div class="images">
              <router-link class="image-link" :to="{ name: 'Signup' }">
                <div class="image" data-label="Signup"><img src="https://i.loli.net/2019/11/23/cnKl1Ykd5rZCVwm.jpg" alt=""></div>
              </router-link>
              <router-link class="image-link" :to="{ name: 'Login' }">
                <div class="image" data-label="Login"><img src="https://i.loli.net/2019/11/16/FLnzi5Kq4tkRZSm.jpg" alt=""></div>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
    <router-view @login="isLogin=true" :key="$route.fullPath"/>
  </div>
</template>


<script>
import jwtDecode from "jwt-decode"
import axios from 'axios'
// import './style/style.scss'

const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
      useridid : null
    }
  },
  methods: {
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Login' })
    },
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getMovies: function () {
      axios({
        method: 'get',
        url: `${SERVER_URL}/movies/`,
        headers: this.setToken()  // 'JWT token~~~'
      })
        .then(res => {
          // console.log(res)
          // console.log(res.data)
          this.$store.state.communityMovie = res.data
          // console.log( this.$store.state.communityMovie)
        })
        .catch(err => {
          console.log(err)
        })
      },
      myProfile : function() {
        const token = localStorage.getItem('jwt')
        const user_id = jwtDecode(token).user_id
        // this.$store.state.loginUserID = user_id//
      
        // const path = `/accounts/profile/${user_id}`
          console.log(this.$route.path)
          this.$router.push({name: "profile", params: {user_id:user_id }}).catch(()=>{})
          // if (this.$route.path !== path){
          //   this.$router.push({name: "profile", params: {user_id:user_id }})
          // }
        // this.$router.push({name: "profile", params: {user_id:user_id }})
      },
      otherProfile : function() {
        this.$router.push({name: "profile", params: {user_id: 5}})
      },
  },
  created: function () {
    // 1. Vue Instance가 생성된 직후에 호출되어 jwt를 가져오기
    const token = localStorage.getItem('jwt')
    // 2. 토큰이 있으면
    if (token) {
      // 3. true로 변경하고 없으면 유지
      this.isLogin = true
    
    if (localStorage.getItem('jwt')) {
      this.getMovies()
    } else {
      this.$router.push({ name: 'Login' })
    }

    
    }
  }
}
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css?family=Lora:400,400i,700");

body {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  margin: 0;
  font-family: Lora, sans-serif;
}

p {
  margin: 0;
}

#burger-toggle {
  position: absolute;
  appearance: none;
  opacity: 0;

  &:checked {
    & ~ .menu {
      opacity: 1;
      visibility: visible;

      .menu-nav-link span div,
      img,
      .title p {
        transform: translateY(0);
        transition: 1.2s 0.1s cubic-bezier(0.35, 0, 0.07, 1);
        font-size: 1.5rem;
      }

      .image-link {
        @for $i from 1 through 4 {
          &:nth-child(#{$i}) img {
            transition-delay: 0.1s + 0.08s * $i;
          }
        }
      }
    }

    & ~ .burger-menu {
      .line {
        &::after {
          transform: translateX(0);
        }

        &:nth-child(1) {
          transform: translateY(calc(var(--burger-menu-radius) / 5))
            rotate(45deg);
        }

        &:nth-child(2) {
          transform: scaleX(0);
        }

        &:nth-child(3) {
          transform: translateY(calc(var(--burger-menu-radius) / -5))
            rotate(-45deg);
        }
      }
    }
  }
}

.burger-menu {
  --burger-menu-radius: 4em;

  position: fixed;
  top: 1vh;
  left: 2vw;
  z-index: 100;
  display: block;
  width: var(--burger-menu-radius);
  height: var(--burger-menu-radius);
  outline: none;
  cursor: pointer;

  .line {
    position: absolute;
    left: 25%;
    width: 50%;
    height: 3px;
    background: hsla(210, 29%, 24%, 0.3);
    border-radius: 10px;
    overflow: hidden;
    transition: 0.5s;

    &:nth-child(1) {
      top: 30%;
    }

    &:nth-child(2) {
      top: 50%;
    }

    &:nth-child(3) {
      top: 70%;
    }

    &::after {
      position: absolute;
      content: "";
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: var(--primary-color-darker);
      transform: translateX(-100%);
      transition: 0.25s;
    }

    @for $i from 2 through 3 {
      &:nth-child(#{$i})::after {
        transition-delay: 0.1s * ($i - 1);
      }
    }
  }

  &:hover {
    .line::after {
      transform: translateX(0);
    }
  }
}

.menu {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background: #1a1e23;
  opacity: 0;
  overflow-x: hidden;
  visibility: hidden;
  transition: 0.3s;

  &-nav {
    display: flex;
    flex-wrap: wrap;
    margin: 12px 12px;
    padding: 0;
    text-align: center;
    list-style-type: none;

    &-item {
      margin: 36px 60px 36px 60px;
      flex: 1;
    }

    &-link {
      position: relative;
      display: inline-flex;
      font-size: 2rem;
      color: white;
      text-decoration: none;

      span {
        overflow: hidden;

        div {
          transform: translateY(102%);
        }
      }

      &::after {
        position: absolute;
        content: "";
        top: 100%;
        left: 0;
        width: 100%;
        height: 3px;
        background: var(--primary-color);
        transform: scaleX(0);
        transform-origin: right;
        transition: transform 0.5s;
      }

      &:hover::after {
        transform: scaleX(1);
        transform-origin: left;
      }
    }
  }

  .gallery {
    margin-top: 60px;
    margin-bottom: 300px;
    text-align: center;
  }

  h1 {
    font-size: 30px;
    color: white;
  }

  .title {
    font-size: 24px;
    color: white;
    overflow: hidden;

    p {
      font-size: 12px;
      letter-spacing: 2px;
      text-transform: uppercase;
      transform: translateY(102%);
    }
  }

  .images {
    margin-top: 36px;
    margin-left: 36px;
    margin-right: 36px;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-evenly;

    .image-link {
      width: 15vw;
      margin: 36px 36px;
      overflow: hidden;

      .image {
        position: relative;
        transition: 0.6s;

        &::before {
          position: absolute;
          content: attr(data-label);
          top: 0;
          left: 0;
          z-index: 1;
          display: flex;
          justify-content: center;
          align-items: center;
          width: 100%;
          height: 100%;
          color: white;
          background: rgba(0, 0, 0, 0.6);
          opacity: 0;
          transition: 0.4s;
        }
      }

      &:hover .image {
        transform: scale(1.2);

        &::before {
          opacity: 1;
        }
      }
    }

    img {
      height: 250px;
      transform: translateY(102%);
    }
  }
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  width: 100%;
  padding: 40px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

.nav-item {
  position: fixed;
  top: 1vh;
  right: 2vw;
}
</style>
