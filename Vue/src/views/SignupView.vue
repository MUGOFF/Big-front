<template>
  <div class="signup">
      <div class="margin" align="left">
          <div class="column is-4 is-offset-4">
              <div class="title"><span style="font-weight:bold; font-size:1.5em;">회원가입 </span><span style="color:red">*</span>는 필수 기입 정보 입니다</div>
              <br><br>
              <form class="needs-validation" novalidate @submit.prevent="submitFrom">
                <div class="mb-3">
                  <label class="form-label" style="font-weight:bold;">이름</label> <span style="color:red">*</span>
                  <input type="text" class="form-control" v-model="username" placeholder="이름 입력" required>
                  <div class="invalid-feedback">이름을 입력하세요.</div>
                </div>
                <div class="mb-3">
                    <label class="form-label" style="font-weight:bold;">이메일 주소(아이디)</label> <span style="color:red">*</span>
                    <input type="email" class="form-control" v-model="email" placeholder="yourname@email.com" required>
                    <div class="invalid-feedback">이메일 형식을 확인하세요.</div>
                </div>
                <div class="mb-3">
                  <label class="form-label" style="font-weight:bold;">휴대폰 번호</label> <span style="color:red">*</span>
                  <input type="tel" class="form-control" v-model="phone" placeholder="01012345678" required>
                  <div class="invalid-feedback">휴대폰 번호를 입력하세요.</div>
                </div>
                <div class="mb-3">
                    <label class="form-label" style="font-weight:bold;">비밀번호</label> <span style="color:red">*</span>
                    <input type="password" class="form-control" minlength="8" pattern="/^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[^a-zA-Z0-9]).+$/" v-model="password" placeholder="Password" required>
                    <p  class="form-text text-muted">특수기호, 문자, 숫자가 각각 1개씩 들어가야 합니다.</p >
                      <div class="invalid-feedback">비밀번호는 최소 8자입니다.</div>
                    <label class="form-label" style="font-weight:bold;">비밀번호 확인</label> <span style="color:red">*</span>
                    <input type="password" class="form-control" minlength="8" pattern="/^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[^a-zA-Z0-9]).+$/" v-model="re_password" placeholder="Password" required>
                </div>
                <div class="mb-3">
                  <label class="form-label" style="font-weight:bold;">주소</label> <span style="color:red">*</span>
                  <button type="button" class="btn btn-light btn-sm" @click="showApi">주소 찾기</button>
                  <div class="d-flex">
                    <div class="col-sm-3">
                      <input class="form-control" :value="zip" placeholder="우편번호" readonly>
                    </div>
                    <div class="col-sm-9">
                      <input class="form-control" :value="addr1" placeholder="도로명/지번 주소" readonly>
                    </div>
                  </div>
                  <input type="text" class="form-control" v-model="address" placeholder="상세 주소 입력" required>
                  <div class="invalid-feedback">주소를 입력하세요.</div>
                </div>
                <div class="mb-3">
                  <label style="font-weight:bold;">품종</label> <span style="color:red">*</span>
                  <select class="form-select" v-model="kind" required>
                    <option value="carrot">당근</option>
                    <option value="radish">무</option>
                    <option value="pear">배</option>
                    <option value="napacabbage">배추</option>
                    <option value="apple">사과</option>
                    <option value="lettuce">상추</option>
                    <option value="watermelon">수박</option>
                    <option value="spinach">시금치</option>
                    <option value="onion">양파</option>
                    <option value="cabbage">양배추</option>
                    <option value="cucumber">오이</option>
                    <option value="tomato">토마토</option>
                    <option value="greenonion">파</option>
                    <option value="grape">포도</option>
                    <option value="pepper">풋고추</option>
                </select>
                <div class="invalid-feedback">품종을 선택하세요.</div>
                </div>
                <div class="mb-3">
                  <label style="font-weight:bold;">직업</label> <span style="color:red">*</span>
                  <select class="form-select" v-model="job" required>
                    <option value="생산업자">농업</option>
                    <option value="유통업자">유통</option>
                </select>
                <div class="invalid-feedback">직업을 선택하세요.</div>
                </div>
                <br>
                <div class="mb-3">
                  <label style="font-weight:bold;">선호 품종</label>
                  <select class="form-select" v-model="kindPre">
                    <option value="none">없음</option>
                    <option value="carrot">당근</option>
                    <option value="radish">무</option>
                    <option value="pear">배</option>
                    <option value="napacabbage">배추</option>
                    <option value="apple">사과</option>
                    <option value="lettuce">상추</option>
                    <option value="watermelon">수박</option>
                    <option value="spinach">시금치</option>
                    <option value="onion">양파</option>
                    <option value="cabbage">양배추</option>
                    <option value="cucumber">오이</option>
                    <option value="tomato">토마토</option>
                    <option value="greenonion">파</option>
                    <option value="pepper">풋고추</option>
                  </select>
                </div>
                <div class="mb-3">
                  <label style="font-weight:bold;">선호 지역</label>
                  <select class="form-select" v-model="region">
                    <option value="none">없음</option>
                    <option value="gwangju">광주</option>
                    <option value="daegu">대구</option>
                    <option value="daejeon">대전</option>
                    <option value="busan">부산</option>
                    <option value="seoul">서울</option>
                  </select> <br/>
                </div>
                <button type="submit" class="btn btn-primary w-100">회원가입</button>
            </form>
            <br>
            <div align="center"><span style="color:gray;">이미 가입하셨습니까? </span><router-link class="navbar-brand" to="/login"><span style="color:green; text-decoration-line: underline; font-weight:bold;">로그인</span></router-link></div>
          </div>
        </div>
        
      </div>
    </template>

<script>
(function() {
            'use strict';
            window.addEventListener('load', function() {
                // Fetch all the forms we want to apply custom Bootstrap validation styles to
                var forms = document.getElementsByClassName('needs-validation');
                
                // Loop over them and prevent submission
                var validation = Array.prototype.filter.call(forms, function(form) { //eslint-disable-line no-unused-vars
                    form.addEventListener('submit', function(event) {
                        if (form.checkValidity() === false) {
                            event.preventDefault();
                            event.stopPropagation();
                        }
                        form.classList.add('was-validated');
                    }, false);
                });
            }, false);
        })();
var reg_email = /^([0-9a-zA-Z_\.-]+)@([0-9a-zA-Z_-]+)(\.[0-9a-zA-Z_-]+){1,2}$/;
var reg_pwd = /^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[^a-zA-Z0-9]).{8,}$/;
import axios from "axios";
export default {
  name: 'SignUp',
  data() {
      return {
          username: '',
          email: '',
          phone: '',
          password: '',
          address: '',
          kind: '',
          kindPre: 'none',
          region: 'none',
          userlist: [],
          token: "",
          zip: '',
          addr1: '',
          addr2: '',
      }
  },
  mounted() {
      this.getNoticeList()
  },
  methods: {
    getNoticeList() {
        axios({
            methods: "GET",
            url: '/user/',
        })
        .then(response => {
            this.userlist = response.data
        })
        .catch(error => {
            console.log(error)
        })
    },
    submitFrom() {
      if (this.username === undefined){
        alert('이름을 입력하세요.')
        return false
      }
      if(!reg_email.test(this.email)) {
        alert('이메일형식이 알맞지 않습니다.')
        return false
      } 
      for (var u_num in this.userlist){
        if (this.email === this.userlist[u_num].email) {
          alert('이 이메일은 이미 존재합니다.')
          return false
        }
      }
      if (this.phone === undefined){
        alert('전화번호를 입력하세요')
        return false
      }
      if (this.password === undefined){
        alert('비밀번호를 입력하세요')
        return false
      }
      if (this.password !== this.re_password){
        alert('비밀번호가 다릅니다.')
        return false
      }
      if(!reg_pwd.test(this.password)){
        alert('비밀번호에는 8자 이상의 최소 1개의 문자. 1개의 숫자, 1개의 특수기호가 들어가야 합니다.')
        return false
      } 
      if (this.address === undefined){
        alert('주소를 입력하세요')
        return false
      }
      if (this.kind === undefined){
        alert('품종을 입력하세요')
        return false
      }
      if (this.job === undefined){
        alert('직업을 입력하세요')
        return false
      }
      axios.post('api/v1/users/', {
          username: this.email,
          password: this.password,
          email: this.email,
      })
      .then(response => {
        console.log(response)
        axios.post('/api/v1/token/login', {
          username: this.email,
          password: this.password,
       })
       .then(response => {
        this.token = response.data.auth_token
        axios.post('user/', {
            username: this.username,
            email: this.email,
            phone: this.phone,
            token: this.token,
            address: this.zip + " " + this.addr1 + " " + this.address,
            kind: this.kind,
            job: this.job,
            kindPre: this.kindPre,
            region: this.region,
        })
        .then(response => {
            this.userList= response.data
            alert('Success')
            this.$router.push('/login')
        })
        .catch(error => {
            console.log(error)
        })
       })
       .catch(error => {
          console.log(error)
       })
      })
      .catch(error => {
        console.log(error)
      })
    },
    showApi() {
        new window.daum.Postcode({
          oncomplete: (data) => {
              // 팝업에서 검색결과 항목을 클릭했을때 실행할 코드를 작성하는 부분.
  
              // 도로명 주소의 노출 규칙에 따라 주소를 조합한다.
              // 내려오는 변수가 값이 없는 경우엔 공백('')값을 가지므로, 이를 참고하여 분기 한다.
              let fullRoadAddr = data.roadAddress; // 도로명 주소 변수
              let extraRoadAddr = ''; // 도로명 조합형 주소 변수
  
              // 법정동명이 있을 경우 추가한다. (법정리는 제외)
              // 법정동의 경우 마지막 문자가 "동/로/가"로 끝난다.
              if(data.bname !== '' && /[동|로|가]$/g.test(data.bname)){
                  extraRoadAddr += data.bname;
              }
              // 건물명이 있고, 공동주택일 경우 추가한다.
              if(data.buildingName !== '' && data.apartment === 'Y'){
                extraRoadAddr += (extraRoadAddr !== '' ? ', ' + data.buildingName : data.buildingName);
              }
              // 도로명, 지번 조합형 주소가 있을 경우, 괄호까지 추가한 최종 문자열을 만든다.
              if(extraRoadAddr !== ''){
                  extraRoadAddr = ' (' + extraRoadAddr + ')';
              }
              // 도로명, 지번 주소의 유무에 따라 해당 조합형 주소를 추가한다.
              if(fullRoadAddr !== ''){
                  fullRoadAddr += extraRoadAddr;
              }
  
              // 우편번호와 주소 정보를 해당 필드에 넣는다.
              this.zip = data.zonecode; //5자리 새우편번호 사용
              this.addr1 = fullRoadAddr;
          }
        }).open()
    },
  },
}
</script>

<style scoped>
  .signup {
    background-image:url('@/assets/signupback.png');
    background-repeat: no-repeat;
  }
  .margin {
    margin-top: 50px;
    margin-left: 100px;
    margin-right: 100px;
    width: 653px;
    height: 1024px;
    left: 787px;
    top: 0px;
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