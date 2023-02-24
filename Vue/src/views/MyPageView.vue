<template>
    <div id="profile">
      <div id="wallpaper" :style="`background-image:url(${back_img})`"></div>
      <div id="profile-left">
        <div id="profile-img" :style="`background-image:url(${profile_img})`"></div>
        <div id="left-detail">
          <p> <span class="detail-top">이름</span> <br>
          <span class="detail-bottom">{{ userInfo.username }}</span></p>
          <!-- <p> <span class="detail-top">한 줄 소개</span> <br>
          <span class="detail-bottom">{{ userInfo.intro }}</span></p> -->
          <p> <span class="detail-top">이메일(ID)</span> <br>
          <span class="detail-bottom">{{ userInfo.email }}</span></p>
          <p> <span class="detail-top">전화번호</span> <br>
          <span class="detail-bottom">{{ userInfo.phone }}</span></p>
           <!-- <p> <span class="detail-top">주소</span> <br>
          <span class="detail-bottom">{{ userInfo.address }}</span></p> -->
          <p> <span class="detail-top">직업</span> <br>
          <span class="detail-bottom">{{ userInfo.job }}</span></p>
          <!--<p> <span class="detail-top">품종</span> <br>
          <span class="detail-bottom">{{ userInfo.kind }}</span></p>
          <p> <span class="detail-top">선호 품종</span> <br>
          <span class="detail-bottom">{{ userInfo.kindPre }}</span></p>
          <p> <span class="detail-top">선호 지역</span> <br>
          <span class="detail-bottom">{{ userInfo.region }}</span></p> -->
        </div>
      </div>
      <!-- 세부사항 -->
      <div id="profile-right mr-3">
        <div id="title">
            <span>마이페이지</span> &nbsp;
            <label class="file-label" for="chooseImg">사진변경</label>
            <input class="file" id="chooseImg" type="file" @change="fileChange" accept="image/*"> &nbsp;
            <!-- <label class="file-label" for="chooseBack">배경변경</label>
            <input class="file" id="chooseBack" type="file" @change="backChange" accept="image/*"> -->
        </div>
        <div class='row g-5 '>
          <!-- 왼쪽 -->
          <div class='col-sm-5'>
            
            <form class="row g-3" @submit.prevent="profileUpdate">
              <label>한 줄 소개</label>
              <div>
                  <input type="text" class="form-control" v-model="intro">
              </div>
              <label>전화번호</label>
              <div>
                  <input type="text" class="form-control" v-model="phone">
              </div>
              <label>주소</label>
              <button type="button" class="btn btn-light btn-sm" @click="showApi">주소 찾기</button>
              <div>
                  <textarea type="text" class="form-control" v-model="address"></textarea>
              </div>
              <label>품종</label>
              <div>
                <select class="form-select" v-model="kind">
                  <option value="carrot">당근</option>
                  <option value="radish">무</option>
                  <option value="pear">배</option>
                  <option value="napacabbage">배추</option>
                  <option value="lettuce">상추</option>
                  <option value="watermelon">수박</option>
                  <option value="spinach">시금치</option>
                  <option value="cabbage">양배추</option>
                  <option value="cucumber">오이</option>
                  <option value="tomato">토마토</option>
                  <option value="pepper">풋고추</option>
                </select>
              </div>
              <label>선호 품종</label>
              <div>
                <select class="form-select" v-model="kindPre">
                  <option value="none">없음</option>
                  <option value="carrot">당근</option>
                  <option value="radish">무</option>
                  <option value="pear">배</option>
                  <option value="napacabbage">배추</option>
                  <option value="lettuce">상추</option>
                  <option value="watermelon">수박</option>
                  <option value="spinach">시금치</option>
                  <option value="cabbage">양배추</option>
                  <option value="cucumber">오이</option>
                  <option value="tomato">토마토</option>
                  <option value="pepper">풋고추</option>
                </select>
              </div>
              <label>선호 지역</label>
              <div>
                <select class="form-select" v-model="region">
                  <option value="none">없음</option>
                  <option value="서울">서울</option>
                  <option value="부산">부산</option>
                  <option value="대구">대구</option>
                  <option value="광주">광주</option>
                  <option value="대전">대전</option>
                </select>
              </div>
              <button class="btn btn-outline-success w-100" type="submit">변경</button>
            </form>
          </div>
            <!-- 오른쪽 -->
            <div class='col-sm-6'>
              <div class="right-detail">최근거래목록
                  <div class="parent"> 
                        <!-- <div class="child chart">재거래희망률
                            <DoughnutChart style="width:100%; height:150px; margin-top: 10px;"/>
                            <span style="font-size:8px; color: gray;">{{total}}명 중 {{yes}}명이 만족</span>
                        </div> -->
                        <!-- <div class="child history">  -->
                            <table class="table">
                                <thead>
                                    <tr>
                                        <th scope="col">id</th>
                                        <th scope="col">품목</th>
                                        <th scope="col">날짜</th>
                                        <th scope="col">거래상대</th>
                                        <th scope="col">비고</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="contract in CoInSu" :key="contract" @click="download_contract(contract.id)">
                                        <th scope="row" >{{ contract.id }}</th>
                                        <td>{{contract.item}}</td>
                                        <td>{{contract.date }}</td>
                                        <td>{{contract.name }}</td>
                                        <td><button class="btn btn-primary btn-sm" type="button" data-bs-toggle="modal" data-bs-target="#PDFModal">다운로드</button></td>
                                    </tr>
                                </tbody>
                            </table>
                        <!-- </div> -->
                    </div>
                  </div>
                  <div class="right-detail" >
                    <div  id="carouselContractProgress" class="carousel slide" data-bs-ride="carousel">
                      <div class="carousel-inner">
                        <div class="carousel-item active">
                          <span class="h3">미체결 계약</span>
                          <small class="text-muted">-진행중인 계약</small>
                          <table class="table">
                            <thead>
                              <tr>
                                <th scope="col">id</th>
                                <th scope="col">품목</th>
                                <th scope="col">날짜</th>
                                <th scope="col">거래상대</th>
                              </tr>
                            </thead>
                            <tbody>
                              <tr v-for="contract in CoInPr" :key="contract" @click="finish_contract(contract.id)">
                                <th scope="row">{{ contract.id }}</th>
                                <td>{{contract.item}}</td>
                                <td>{{contract.date }}</td>
                                <td>{{contract.name }}</td>
                              </tr>
                            </tbody>
                          </table>
                        </div>
                        <div class="carousel-item">
                          <small class="text-muted">미체결 계약-</small>
                          <span class="h3">진행중인 계약</span>
                          <table class="table">
                              <thead>
                                  <tr>
                                      <th scope="col">id</th>
                                      <th scope="col">품목</th>
                                      <th scope="col">날짜</th>
                                      <th scope="col">거래상대</th>
                                  </tr>
                              </thead>
                              <tbody>
                                  <tr v-for="contract in CoUnPr" :key="contract">
                                      <th scope="row">{{ contract.id }}</th>
                                      <td>{{contract.item}}</td>
                                      <td>{{contract.date }}</td>
                                      <td>{{contract.name }}</td>
                                  </tr>
                              </tbody>
                          </table>
                        </div>
                      </div>
                      <button class="carousel-control-prev" type="button" data-bs-target="#carouselContractProgress" data-bs-slide="prev">
                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Previous</span>
                      </button>
                      <button class="carousel-control-next" type="button" data-bs-target="#carouselContractProgress" data-bs-slide="next">
                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Next</span>
                      </button>
                    </div> <!--carousel slide-->
                  </div> <!--right-detail-->
            </div>
        </div>
      </div>
      <!-- 모달창 -->
      <div class="modal" role="dialog" id="PDFModal" aria-labelledby="pdfModal" aria-hidden="true">
      <div class="modal-dialog modal-xl modal-dialog-centered" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="pdfModal">{{contract_info.seller_name + " " + contract_info.buyer_name + " " + contract_info.item}}</h5>
            <button type="button" class="close" data-bs-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body" ref="pdfArea" :key="pdfKey">
            <div class="col-md-12 d-flex">
              <div class="col-md-6">
                <span class="fs-3 fw-bold">매도자(갑) : {{contract_info.seller_name}}</span><br>
                <span class="fs-3">생년월일 : {{contract_info.seller_birth}}</span><br>
                <span class="fs-3">전화번호 : {{contract_info.seller_phone}}</span><br>
                <span class="fs-3">주소 : {{contract_info.seller_address}}</span><br>
              </div>
              <div class="col-md-6">
                <span class="fs-3 fw-bold">매수자(을) : {{contract_info.buyer_name}}</span><br>
                <span class="fs-3">생년월일 : {{contract_info.buyer_birth}}</span><br>
                <span class="fs-3">전화번호 : {{contract_info.buyer_phone}}</span><br>
                <span class="fs-3"> 주소 : {{contract_info.buyer_address}}</span><br>
              </div>
            </div><br>
            <div class="col-md-12">
              <span class="fs-3">위치 : {{contract_info.farm_address}}</span><br>  
              <span class="fs-3">상품 : {{contract_info.item}}</span><br>   
              <span class="fs-3">면적 : {{contract_info.farm_area}} m2</span>,
              <span class="fs-3 fw-bold">파종일 : {{contract_info.farm_date}}</span>  
            </div><br>
            <div class="col-md-12 d-flex">
              <div class="col-md-6">
                <span class="fs-3 fw-bold">총매입금 : {{contract_info.payment}}</span><br>
                <span class="fs-3">계약금: {{contract_info.advance}}</span><br>
                <span class="fs-3">중도금 : {{contract_info.interpay}}</span><br>
                <span class="fs-3">잔금 : {{contract_info.balance}}</span><br>
              </div>
              <div class="col-md-6">
                <span class="fs-3 fw-bold">총매입금 지급일 : {{contract_info.payment_date}}</span><br>
                <span class="fs-3">계약금 지급일: {{contract_info.advance_date}}</span><br>
                <span class="fs-3">중도금 지급일 : {{contract_info.interpay_date}}</span><br>
                <span class="fs-3">잔금 지급일 : {{contract_info.balance_date}}</span><br>
              </div>
            </div><br>
            <div class="col-md-12">
              <span class="fs-3 fw-bold">반출일 : {{contract_info.goods_date}}</span><br><br>
            </div><br>
            <div class="col-md-12">
              <span class="fs-3 fw-bolder">특약사항 : {{contract_info.special_contract}}</span><br>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">닫기</button>
            <button type="button" class="btn btn-primary" @click="htmlToPdf(this.$refs.pdfArea , '계약서')">다운로드</button>
          </div>
        </div>
      </div>
      </div>
    </div>
  </template>
  <script>
    // import DoughnutChart from '@/components/DoughnutChart.vue'
    import html2pdf from 'html2pdf.js';
    import Name from '@/components/ContractName.vue'
    import Right from '@/components/ContractRight.vue'
    import Left from '@/components/ContractLeft.vue'
    import axios from 'axios'
    export default {
      name: 'ProfileView',
      components: {},
      data() {
        return {
          profile_img: '',
          userInfo: {
            username:"",
            intro:"",
            email:"",
            job:"",
            phone:"",
            address:"",
            kind:"",
            kindPre:"",
            region:"",
          },
          contract_info: {},
          address:"",
          job_loaded:false,
          CoInSu:[],
          CoInPr:[],
          CoUnPr:[],
        }
      },Name,Right,Left,
      mounted() {
        this.get_personal_info()
      },
      methods: {
        fileChange: function(e) {
              // console.log(e.target.files)//files는 배열로 들어온다.
              let url = URL.createObjectURL(e.target.files[0]);
              // console.log(url);
              this.profile_img = url;
              let AxiosConfig = {
                headers: {
                    "Content-Type": "multipart/form-data",
                }
              }
              axios.put('updateuser/?token='+this.$store.state.token, {
                profile: e.target.files[0]
              },AxiosConfig)
              .then(response => {
                  alert("프로필 수정 완료")
              })
              .catch(error => {
                  console.log(error)
              })
          },
        backChange: function(e) {
          // console.log('hello')
          // console.log(e.target.files)//files는 배열로 들어온다.
          let url = URL.createObjectURL(e.target.files[0]);
          // console.log(url);
          this.back_img = url;
          let AxiosConfig = {
            headers: {
                "Content-Type": "multipart/form-data",
            }
          }
          axios.put('updateuser/?token='+this.$store.state.token, {
            back: e.target.files[0]
          },AxiosConfig)
          .then(response => {
              alert("배경 수정 완료")
          })
          .catch(error => {
              console.log(error)
          })
        },
        htmlToPdf: (location, fileName) => {
          html2pdf()
            .set({
              margin: [15, 10, 15, 10],
              // filename에서 IE11은 .pdf를 자동으로 넣어주지 않아 .pdf를 파일 명에 넣어줘야 한다.
              filename: navigator.userAgent.indexOf('MSIE') !== -1 || navigator.appVersion.indexOf('Trident/') > -1 ? `${fileName}.pdf` : fileName,
              pagebreak: { mode: 'avoid-all' },
              image: { type: 'jpeg', quality: 1 },
              html2canvas: {
                useCORS: true,
                scrollY: 0,
                scale: 1,
                dpi: 300,
                letterRendering: true,
                allowTaint: false, //useCORS를 true로 설정 시 반드시 allowTaint를 false처리 해주어야함
              },
              jsPDF: { orientation: 'portrait', unit: 'mm', format: 'a4' },
            })
            .from(location)
            .save();
        },
        download_contract(contract_id) {
          axios.get('Contract_sign/?id='+Number(contract_id))
          .then(response => {
            this.contract_info=response.data[0]
            console.log(this.contract_info)        
          })
          .catch(error => {
            console.log(error)
          })
        },
        get_personal_info() {
          axios
          .get('user/'+ this.$store.state.token)
          .then(response => {
            this.userInfo = response.data
            this.profile_img = response.data.profile
            if(this.userInfo.job==='생산업자') {
              this.job_loaded=true
            }
            axios
            .get('Contract_list/?email='+this.userInfo.email+'&job='+this.userInfo.job,{
            })
            .then(response => {
              const _ = require("lodash")
              for(var step in response.data) {
                var array = []
                array['id']=response.data[step].id
                array['date']=response.data[step].document_date
                array['item']=response.data[step].item.split(" ")[1]
                if (response.data[step].seller_name===undefined) {
                  array['name']=response.data[step].buyer_name
                } else {
                  array['name']=response.data[step].seller_name
                }
                this.CoInSu.push(array)
              }
              console.log(this.CoInSu)
            })
            .catch(error => {
              console.log(error);
            })
            //미체결 계약
            axios
            .get('Contract_inprogress/?email='+this.userInfo.email+'&position=seller',{
            })
            .then(response => {
              console.log(response.data)
              const _ = require("lodash")
              for(var step in response.data) {
                var array = []
                array['id']=response.data[step].id
                array['date']=response.data[step].document_date
                array['item']=response.data[step].item.split(" ")[1]
                if (response.data[step].seller_name===this.userInfo.username) {
                  array['name']=response.data[step].buyer_name
                } else {
                  array['name']=response.data[step].seller_name
                }
                this.CoInPr.push(array)
              }
              // console.log(this.CoInPr)
            })
            .catch(error => {
              console.log(error);
            })
            //진행중인 계약
            axios
            .get('Contract_inprogress/?email='+this.userInfo.email+'&position=buyer',{
            })
            .then(response => {
              console.log(response.data)
              const _ = require("lodash")
              for(var step in response.data) {
                var array = []
                array['id']=response.data[step].id
                array['date']=response.data[step].document_date
                array['item']=response.data[step].item.split(" ")[1]
                if (response.data[step].seller_name===this.userInfo.username) {
                  array['name']=response.data[step].buyer_name
                } else {
                  array['name']=response.data[step].seller_name
                }
                this.CoUnPr.push(array)
              }
              // console.log(this.CoUnPr)
            })
            .catch(error => {
              console.log(error);
            })
          })
          .catch(error => {
            console.log(error);
          })
        },
        finish_contract(c_id) {
          this.$router.push({
                name: 'contract_final', 
                params: {
                  c_id: c_id
                }
            })
        },
        profileUpdate() {
          if (this.address===undefined || this.address=== '')  {
            this.address=this.userInfo.address
          }
          if (this.phone===undefined || this.phone=== '')  {
            this.phone=this.userInfo.phone
          }
          if (this.kind===undefined || this.kind=== '')  {
            this.kind=this.userInfo.kind
          }
          if (this.kindPre===undefined || this.kindPre=== '')  {
            this.kindPre=this.userInfo.kindPre
          }
          if (this.region===undefined || this.region=== '')  {
            this.region=this.userInfo.region
          }
          if (this.intro===undefined || this.intro=== '')  {
            this.intro=this.userInfo.intro
          }
          axios.put('updateuser/?token='+this.$store.state.token, {
            intro: this.intro,
            phone: this.phone,
            address: this.address,
            kind: this.kind,
            kindPre: this.kindPre,
            region: this.region,
          })
          .then(response => {
              alert("프로필 수정 완료")
              window.location.reload()
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
                this.base_address = fullRoadAddr;
                this.address = this.base_address
            }
            }).open()
        },
      }
    }
  </script>
    <style scoped>
    #profile {
      width: 1300px;
      height: 1300px;
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
      width: 20%;
    }
    #profile-right {
      float:right;
      width: 80%;
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
      text-align: center;
      font-size: 20px;
      font-weight: 550;
      padding: 10px;
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
    .file-label {
      font-size: 18px;
      font-weight: 500;
      margin-top: 30px;
      background-color: #9ac486;
      color: #fff;
      text-align: center;
      padding: 10px;
      border-radius: 6px;
      cursor: pointer;
    }
    .file {
      display: none;
    }
    .btn-outline-success {
      background: #9ac486;
      color: white;
      border: none;
      }
      .btn-outline-success:hover {
      background: #799b6a;
      border: none;
      } 
    </style>
  