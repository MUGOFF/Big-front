<template>
    <div class="login">
      <div class="title"><span style="font-weight:bold; font-size:1.5em;">비밀번호 재확인</span></div>
      <form class="needs-validation" novalidate @submit.prevent="recofirmForm" align="left">
        <br><br><br><br>
        <div class="mb-3">
          <label class="form-label" style="font-weight:bold;">비밀번호</label>
          <input type="password" class="form-control" v-model="userPassword" placeholder="password" required>
        </div>
        <button type="submit" class="btn btn-primary w-100">확인</button>
      </form> <br/>
      <br><br><br><br><br><br><br><br>
    
    </div>
    
  </template>
  
  <script>
  import axios from 'axios';
  export default {
    data() {
      return {
        userId: null,
        userPassword: null,
      };
    },
    mounted() {
      this.get_username()
    },
    methods: {
    get_username() {
      axios
      .get('user/'+ this.$store.state.token)
      .then(response => {
        this.userId = response.data;
      })
      .catch(error => {
        console.log(error);
      })
    },
    recofirmForm(e) {
      // console.log(this.userId)
      // console.log(this.userPassword)
      axios.post('/api/v1/token/login', {
        username: this.userId.email,
        password: this.userPassword,
      })
      .then(response =>{
        this.$router.push('/mypage')
      })
      .catch(error => {
        alert(error.request.response)
      })
    }
  },
  };
  </script>
  <style scoped>
  .login {
    width: 700px;
    margin: auto;
    padding-top: 100px;
  }
  
  
  .btn{
    /* color: #000; */
    background-color: #9ac486;
    border: none;
  }
  
  .btn:hover{
      /* color: #000; */
      background-color: #799b6a;
      border: none;
    }
  
  </style>