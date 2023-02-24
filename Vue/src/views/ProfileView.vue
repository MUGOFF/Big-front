<template>
  <div id="profile">
    <div id="wallpaper"></div>
    <div id="profile-left">
      <div id="profile-img"></div>
      <div id="left-detail">
        <p> <span class="detail-top">이름</span> <br>
        <span class="detail-bottom">{{ name }}</span></p>
        <p> <span class="detail-top">한 줄 소개</span> <br>
        <span class="detail-bottom">{{ intro }}</span></p>
        <p> <span class="detail-top">재배 작물</span> <br>
        <span class="detail-bottom"> {{ kind.join(', ') }} </span></p>
        <p> <span class="detail-top">지역</span> <br>
        <span class="detail-bottom">{{ region }}</span></p>
      </div>
    </div>
    <div id="profile-right">
      <div id="title">{{ title }}</div>
      <div class="right-detail">
        <div class="parent">
          <div class="child chart">
            재거래희망률
            <DoughnutChart style="width:100%; height:150px; margin-top: 10px;"/>
            <span style="font-size:8px; color: gray;">{{total}}명 중 {{yes}}명이 만족</span>
          </div>
          <div class="child history">
            최근거래목록
            <table class="table">
              <thead>
                <tr>
                  <th scope="col">id</th>
                  <th scope="col">품목</th>
                  <th scope="col">날짜</th>
                  <th scope="col">뭐적지</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <th scope="row">1</th>
                  <td>당근</td>
                  <td>2022.00.00</td>
                  <td>......</td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="child">
            <div class="price">
              {{price}}<br>
              <span style="font-size:10px; font-weight:100;">농민 희망 인수비용</span>
            </div>
            <div class="price">
              {{predict}}<br>
              <span style="font-size:10px; font-weight:100;">AI모델 예측 인수비용</span>
            </div>
          </div>
        </div>
        <table class="table table-borderless" style="margin-top: 70px; width:350px;">
          <tr>
            <td style="width: 50%"><button type="button" class="btn btn-success w-100"><span id="button-text">관심목록 추가</span></button></td>
            <td><button type="button" class="btn btn-success w-100"><span id="button-text">계약서 작성</span></button></td>
          </tr>
        </table>
      </div>
    </div>
  </div>
</template>
<script>
import DoughnutChart from '@/components/DoughnutChart.vue'
import axios from 'axios'

export default {
  name: 'ProfileView',
  components: { DoughnutChart },
  data() {
    return {
      "name": "김농부",
      "intro": "나는 농부",
      "kind": ["대파", "배추"],
      "region": "전남 진해",
      "title": "대파 팝니다.", 
      "price": "1,500,000원",
      "predict": "1,300,000원",
      "total": 12,
      "yes": 6,
      // userInfo: {
      //   username:"",
      //   email:"",
      //   job:"",
      //   phone:"",
      //   address:"",
      //   kind:"",
      //   kindPre:"",
      //   region:"",
      // },
    }
  },
  // mounted() {
  //   this.get_personal_info()
  //   console.log(this.userInfo)
  // },
  // methods: {
  //   get_personal_info() {
  //     axios
  //     .get('user/'+ this.$store.state.token)
  //     .then(response => {
  //       this.userInfo = response.data
  //       console.log(response.data)
  //     })
  //     .catch(error => {
  //       console.log(error);
  //     })
  //   }, 
  //   get_personal_contract_list() {
  //     axios
  //     .get({})
  //     .then(response => {

  //     })
  //     .catch(error => {
  //       console.log(error);
  //     })
  //   }, 
  // }
}
</script>
<style scoped>
#profile {
  width: 1000px;
  height: 700px;
  margin: auto;
  margin-bottom: 20px;
  border-top-left-radius: 24px;
  border-top-right-radius: 24px;
  border-bottom-left-radius: 24px;
  border-bottom-right-radius: 24px;
  box-shadow: 0px 4px 40px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}
#wallpaper {
  width: 100%;
  height: 150px;
  background-image:url('@/assets/profile/profileback.png');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center center;
  opacity: 1;
  top: 0px;
  left: 0px;
  overflow: hidden;
}
#profile-left {
  padding-left: 50px;
  float:left;
  width: 30%;
}
#profile-right {
  float:right;
  width: 70%;
}
#profile-img {
  width: 200px;
  height: 200px;
  background-image:url('@/assets/profile/profile.jpg');
  background-size: cover;
  opacity: 1;
  margin-top: -70px;
  background-position: center center;
  border: 7px solid white;
  border-top-left-radius: 30px;
  border-top-right-radius: 30px;
  border-bottom-left-radius: 30px;
  border-bottom-right-radius: 30px;
}
#left-detail {
  margin-top: 20px;
  text-align: left;
}
.detail-top {
  color:#9ac486;
  font-size: 20px;
  font-weight: 700;
}
.detail-bottom {
  color:#000000;
  font-size: 25px;
  font-weight: 500;
}
#title {
  height: 100px;
  text-align: left;
  margin-top: 30px;
  font-size: 35px;
  font-weight: 700;
}
.right-detail {
  height: 400px;
  margin-right: 30px;
  margin-bottom: 20px;
  padding: 20px;
  border-top-left-radius: 24px;
  border-top-right-radius: 24px;
  border-bottom-left-radius: 24px;
  border-bottom-right-radius: 24px;
  box-shadow: 0px 1px 10px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}
.parent {
  display: flex;
}
.parent .child {
  flex: 1;
  text-align: center;
  font-size: 20px;
  font-weight: 550;
  padding: 10px;
  height: 230px;
}
.chart {
  height:230px;
}
.table {
  font-size: 10px;
  margin-top: 20px;
  margin: auto;
}
.price {
  color: #FFFFFF;
  height: 80px;
  margin-top: 40px;
  padding-top: 20px;
  background-color: #9ac486;
  border-top-left-radius: 24px;
  border-top-right-radius: 24px;
  border-bottom-left-radius: 24px;
  border-bottom-right-radius: 24px;
  box-shadow: 0px 1px 10px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}
#button-text {
  font-size:15px; 
  font-weight:500;
}
.w-100 {
  padding: 15px;
}
</style>
