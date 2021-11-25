<template>
  <div id="topp">
    <!-- <p style="color:red">{{this.passwordLength}}</p> -->
    <div id="LSform">
    <div class="container">
      <div class="row">
        <div class="col-md-6">
          <div class="card">
            <form onsubmit="event.preventDefault()" class="box">
                <h1>Sign-up</h1>
                <p class="text-muted"> Please enter your Information and Signup!</p> 
                <input type="text" name="" placeholder="Email" v-model="credentials.username">
                <input type="text" name="" placeholder="Nickname" v-model="credentials.nickname">
                <input type="password" name="" placeholder="Password" v-model="credentials.password" @keyup.enter="signup"> 
                <input type="password" name="" placeholder="PasswordCheck" v-model="credentials.passwordConfirmation" @keyup.enter="signup">
                <div v-if="this.credentials.passwordConfirmation.length > 2">
                  <p v-if = 'credentials.password === credentials.passwordConfirmation ' style="color : green">비밀번호가 일치합니다</p>
                  <p v-else-if = "credentials.password !== credentials.passwordConfirmation" style="color : red">비밀번호가 일치하지 않습니다!!!</p>
                </div>
                <input type="submit" name="" value="Signup" @click="signup">
                <div class="col-md-12">
                    <ul class="social-network social-circle">
                        <li><a href="#" class="icoFacebook" title="Facebook"><i class="fab fa-facebook-f"></i></a></li>
                        <li><a href="#" class="icoTwitter" title="Twitter"><i class="fab fa-twitter"></i></a></li>
                        <li><a href="#" class="icoGoogle" title="Google +"><i class="fab fa-google-plus"></i></a></li>
                    </ul>
                </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: null,
        nickname: null,
        password: "", 
        passwordConfirmation: "",
      },
      passwordToggle: false,
      passworLength : null
    }
  },
  methods: {
    signup: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials
      })
        .then(res => {
          console.log(res)
          this.$router.push({ name: 'Login' })
        })
        .catch(err => {
          console.log(err)
          this.passwordToggle = true
          console.log(this.credentials.passwordConfirmation.length)
        })
    }
  },
}
</script>

<style scoped>

@keyframes fadeInDown {
      0% {
          opacity: 0;
          transform: translate3d(0, -100%, 0);
      }
      to {
          opacity: 1;
          transform: translateZ(0);
      }
  }

#topp::before{
  position: fixed; 
  top: 0; 
  left: 0; 
  right: 0; 
  bottom: 0;
  background-image: url("https://phoneky.co.uk/thumbs/wallpapers/p2ls/movies/40/0951109d12731614.jpg");
  background-size: 100% 100%;
  /* filter: blur(2px);  */
  z-index: -1; 
  content: "";
}

.card {
    margin-bottom: 20px;
    border: none;
    /* transform:scale(1.1); */
    animation: fadeInDown 2s;
    
}

.box {
    width: 500px;
    padding: 40px;
    position: absolute;
    top: 50%;
    left: 50%;
    background: rgba(0,0,0,0.7);
    text-align: center;
    transition: 0.25s;
    margin-top: 100px;
    border-radius: 30px;
}

.box input[type="text"],
.box input[type="password"] {
    border: 0;
    background: none;
    display: block;
    margin: 20px auto;
    text-align: center;
    border: 2px solid #3498db;
    padding: 10px 10px;
    width: 250px;
    outline: none;
    color: white;
    border-radius: 24px;
    transition: 0.25s
}

.box h1 {
    color: white;
    text-transform: uppercase;
    font-weight: 500
}

.box input[type="text"]:focus,
.box input[type="password"]:focus {
    width: 300px;
    border-color: #2ecc71
}

.box input[type="submit"] {
    border: 0;
    background: none;
    display: block;
    margin: 20px auto;
    text-align: center;
    border: 2px solid #2ecc71;
    padding: 14px 40px;
    outline: none;
    color: white;
    border-radius: 24px;
    transition: 0.25s;
    cursor: pointer
}

.box input[type="submit"]:hover {
    background: #2ecc71
}

.forgot {
    text-decoration: underline
}

ul.social-network {
    list-style: none;
    display: inline;
    margin-left: 0 !important;
    padding: 0
}

ul.social-network li {
    display: inline;
    margin: 0 5px
}

.social-network a.icoFacebook:hover {
    background-color: #3B5998
}

.social-network a.icoTwitter:hover {
    background-color: #33ccff
}

.social-network a.icoGoogle:hover {
    background-color: #BD3518
}

.social-network a.icoFacebook:hover i,
.social-network a.icoTwitter:hover i,
.social-network a.icoGoogle:hover i {
    color: #fff
}

a.socialIcon:hover,
.socialHoverClass {
    color: #44BCDD
}

.social-circle li a {
    display: inline-block;
    position: relative;
    margin: 0 auto 0 auto;
    border-radius: 50%;
    text-align: center;
    width: 50px;
    height: 50px;
    font-size: 20px
}

.social-circle li i {
    margin: 0;
    line-height: 50px;
    text-align: center
}

.social-circle li a:hover i,
.triggeredHover {
    transform: rotate(360deg);
    transition: all 0.2s
}

.social-circle i {
    color: #fff;
    transition: all 0.8s;
    transition: all 0.8s
}


</style>