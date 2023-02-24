<template>
  <div id="product">
    <div id="left">
      <div id="left-top col-md-5">
        <div style="font-weight: 700; font-size: 35px;">{{article.title}}</div>
        <img :src="article.profile"/>
      </div>
      <div id="left-bottom col-md-5 mt-2" style="width:100%;height:100%;">
        <div id="left-title">
          <div style="font-weight: 700; font-size: 30px;">상품명</div>
          <div align="right" style="color:gray;">납품일 : {{ article.g_date }}</div>
        </div>
        <table class="table table-borderless">
          <tbody>
            <tr>
              <td width="150"><div id="list">판매자</div></td>
              <td id="listTable">{{ article.seller_name }}</td>
              <button type="button" class="btn btn-light btn-sm" data-bs-toggle="modal" data-bs-target="#myModal" @click="showProfile">프로필보기</button>
            </tr>
            <tr>
              <td width="150"><div id="list">품종</div></td>
              <td id="listTable">{{ article.items_kor }}</td>
            </tr>
            <tr>
              <td width="150"><div id="list">지역</div></td>
              <td id="listTable">{{ article.regions_kor }}</td>
            </tr>
            <tr>
              <td width="150"><div id="list">품질</div></td>
              <td id="listTable">{{ article.quality }}</td>
            </tr>
            <tr>
              <td width="150"><div id="list">면적</div></td>
              <td id="listTable">{{ article.area }} 평</td>
            </tr>
            <tr>
              <td width="150"><div id="list">판매가격</div></td>
              <td id="listTable">{{ article.price }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div id="right">
      <div id="right-top col-md-5" style="width:90%;height:60vh;margin:20px;">
        <div class="spinner-border" role="status" v-show="this.$store.state.isLoading" style="width:10vh;height:10vh;">
            <span class="visually-hidden">Loading...</span>
        </div>
        <div v-show="chartData.loaded">
          <LineChart v-if="chartData.loaded" v-bind="chartData" />
        </div>
        <div style="height:10%;margin-bottom: 20px;">
          <table class="table table-borderless" style="width:100%">
            <tr>
              <td style="width:45%;"><button type="button" class="btn btn-outline-danger w-75" @click="BacktoList"><span id="button-text">취소하기</span></button></td>
              <!-- <td style="width:30%"><button type="button" class="btn btn-primary w-100"><span id="button-text">제안하기</span></button></td> -->
              <td style="width:45%;"><button type="button" class="btn btn-success w-75" @click="contractDocu"><span id="button-text" style="color:black">계약하기</span></button></td>
            </tr>
          </table>
        </div>
      </div>
      <div id="right-bottom col-md-5 mt-2" style="width:100%;height:50vh">
        <!-- <table class="table table-borderless">
          <tbody>
            <tr>
              <td width="150"><div id="list">구매자</div></td>
              <td id="listTable">{{ buyer }} <button type="button" class="btn btn-light btn-sm">프로필보기</button></td>
            </tr>
            <tr>
              <td width="150"><div id="list">메시지</div></td>
              <td id="listTable"> {{ message }} </td>
            </tr>
            <tr>
              <td width="150"><div id="list">제안가</div></td>
              <td id="listTable"> {{ proposalprice }}</td>
            </tr>
          </tbody>
        </table> -->
        <div id="bottom" style="height:100%;margin:20px">
          <div id="title" style="height:70px">상세 정보</div>
          <div id="detail">{{ article.description }}</div>
        </div>  
      </div>
    </div>
  </div>
  <!-- 모달창 -->
  <div class="modal" role="dialog" id="myModal" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-lg modal-dialog-centered" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">{{ seller_profile.username }}</h5>
          <button type="button" class="close" data-bs-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body d-flex">
          <div class="col-md-4">
            <img :src="seller_profile.profile" />
          </div>
          <div class="col-md-4">
            <p> <span>한 줄 소개</span> <br>
            <span>{{ seller_profile.intro }}</span></p>
            <p> <span>재배 작물</span> <br>
            <span> {{ seller_profile.kind_kor}} </span></p>
            <p> <span>전화 번호</span> <br>
            <span> {{ seller_profile.phone}} </span></p>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
// import LineChart from '@/components/BarChart.vue'
import LineChart from '@/components/LineChartThreeLine.vue'

export default {
  name: 'ProposalBuyer',
  components: { LineChart },
  data() {
    return {
      profile_img:"",
      article: "",
      seller_profile:[],
      chartData : {
        xlabel: [],
        datas: [[],[],[]],
        legend: [],
        item: "",
        loaded: false,
      },
    }
  },
  mounted(){
    this.get_article_info()
  },
  methods: {
    showProfile() {
      var items_kor = ["당근","무","배","배추","상추","수박","시금치","양배추","오이","토마토",'풋고추']
      var items = ["carrot","radish","pear","napacabbage","lettuce","watermelon","spinach","cabbage","cucumber","tomato",'pepper']
      axios.get('UserPreview/?email='+this.article.seller_email)
      .then(response => {
        console.log(response)
        this.seller_profile = response.data[0]
        this.seller_profile.kind_kor =  items_kor[items.indexOf(this.seller_profile.kind)]
        // let url = URL.createObjectURL(this.seller_profile.profile)
        this.profile_img = this.seller_profile.profile
        console.log(this.seller_profile)
      })
      .catch(error => {
        console.log(error)
      })
    },
    BacktoList(){
      this.$router.push({name:'SearchDetail'})
    },
    contractDocu(){
      console.log(this.article.seller_email)
      this.$router.push({ 
        name: "contract",
        params: { 
          c_id: this.article.id,
        } 
      });
    },
    get_article_info(){
      var items_kor = ["당근","무","배","배추","상추","수박","시금치","양배추","오이","토마토",'풋고추']
      var items = ["carrot","radish","pear","napacabbage","lettuce","watermelon","spinach","cabbage","cucumber","tomato",'pepper']
      var regions_kor = ['서울','부산','대구','광주','대전']
      var regions = ['seoul','pusan','daegu','gwanju','daejun']
      let AxiosHeaders = {
            headers: {
                "content-type": "multipart/form-data",
            }
        }
      axios.get('api/v1/article_detail/?id='+Number(this.$route.params.contentId),AxiosHeaders)
      .then(response => {
        // console.log(response.data[0].profile)
        // response.headers["content-type"] ="multipart/form-data"
        // console.log(decodeURIComponent(response.data[0].profile))
        // var file = window.URL.createObjectURL(new Blob([response.data[0].profile], {type: response.headers['content-type']}))
        // console.log(file)
              // let url = URL.createObjectURL(response.data[0].profile)
        // console.log(response.data)
        this.article = response.data[0]
        // console.log(response)
        // this.article.profile=file
        this.article["items_kor"] = items_kor[items.indexOf(this.article.item)]
        this.article["regions_kor"] = regions_kor[regions.indexOf(this.article.region)]
        // console.log(this.article)
        this.get_graph()
      })
      .catch(error => {
        console.log(error)
      })
    },
    async get_graph() {
      this.$store.commit('setIsLoading', true);
      // console.log(this.chartDataGroup)
      // this.chartDataGroup=[]
      // console.log(this.chartDataGroup)
      
      // var urls = []
      // // var items_kor = ["당근","무","배","배추","상추","수박","시금치","양배추","오이","토마토",'풋고추']
      // // // var unit = ["20kg","20kg","15kg","10kg","4kg","1개","4kg","8kg","50개","5kg",'10kg']
      // // var items = ["carrot","radish","pear","napacabbage","lettuce","watermelon","spinach","cabbage","cucumber","tomato",'pepper']
      // // this.item_select.forEach( item => {
      // // })
      // // console.log(urls)
      // var url='/api/v1/' +this.article.region + '_price_api/?item=' +this.article.item + '&expand=True&period='+90+'&past='+0
      // urls.push(url) // url 저장
      // var resultData = new Array(urls.length) //배열 크기 생성

      await axios
      .get('/api/v1/' +this.article.region + '_price_api/?item=' +this.article.item + '&expand=True&period='+90+'&past='+0) // 가변적 get
      .then(resultData => { // 가변적 데이터 할당
            // const _ = require("lodash") //deepcopy js 모듈 임포트
            // console.log(resultData)
              for (var step=0;step<resultData.data.length;step++) {
                this.chartData.xlabel[step]=(resultData.data[step].ds)
                  this.chartData.item=(resultData.data[step].item)//범례명
                  // if (resultData[num].data[step].price === 0) {
                  this.chartData.datas[0][step]=(resultData.data[step].ythat)
                  this.chartData.datas[1][step]=(resultData.data[step].yhat_lower)
                  this.chartData.datas[2][step]=(resultData.data[step].yhat_upper)
                    
                  // } else {
                    // this.chartData.datas[0][step]=(resultData[num].data[step].price)
                  // }
                }
              // this.chartData.item_kor=(items_kor[items.indexOf(this.chartData.item)])
              // this.chartData.unit=(unit[items.indexOf(this.chartData.item)])
              // this.chartData.img=require("@/assets/"+this.chartData.item_kor+'1.jpg')
              // console.log(this.chartData.img)
              this.chartData.legend = ['기댓값','최소 기댓값', "최대 기댓값"]//범례명
              this.chartData.loaded=true
              // console.log(this.chartData)
              // const clone6 = _.cloneDeep(this.chartData) // deepcopy
              // this.chartDataGroup[num]=(clone6)
            // console.log(this.chartData)
            // this.search_show=false
            // console.log(this.chartDataGroup)
          })
      .catch(error => {
        console.log(error)
      })
      this.$store.commit('setIsLoading', false);
    },
  },
}
</script>
<style scoped>
img {
  width: 80%;
  object-fit: cover;
}
#product {
  margin-left: 100px;
  margin-right: 100px;
  padding-top: 10px;
  overflow: hidden;
}
#left {
  padding-top: 10px;
  float:left;
  width: 50%;
  height: 120vh;
  padding-bottom: 50px;
  padding-right: 10px;
}
#left-top {
  padding-top: 10px;
  height: 60vh;
}
#left-bottom {
  border-top: 3px solid #9ac486;
  /* border-bottom: 3px solid #9ac486; */
  height: 50vh;
  margin-top: 20px;
  padding-top: 10px;
}
#left-title {
  border-bottom: 1px solid #9ac486;
  margin-bottom:25px;
}
#right {
  padding-top: 10px;
  float:right;
  width: 50%;
  height: 120vh;
  padding-bottom: 50px;
  padding-left: 20px;
}
#list {
  background: #9ac486;
  width: 120px;
  height: 42px;
  border-top-left-radius: 20px;
  border-top-right-radius: 20px;
  border-bottom-left-radius: 20px;
  border-bottom-right-radius: 20px;
  
  color: #FFFFFF;
  font-size: 20px;
  text-align: center;
  padding: 8px;
  font-weight: 500;
}
#bottom {
  padding-top: 25px;
  border-top: 3px solid #9ac486;
  /* border-bottom: 3px solid #9ac486; */
  /* clear:both; */
}
#title {
  border-bottom: 1px solid #9ac486;
  font-weight: 700;
  font-size: 35px;
  line-height: 20px;
}
#detail {
  font-weight: 450;
  font-size: 20px;
  margin : 30px;
}
#listTable {
  text-align: left;
  padding-top: 15px;
  font-weight: 500;
  font-size: 20px;
}
.w-100 {
  padding: 20px;
}
#button-text {
  font-size:20px; 
  font-weight:700;
}
</style>
 