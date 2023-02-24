<template>
  <form class="w-75 mt-5 m-auto border" @submit.prevent="submitform">
      <div class="d-flex my-3">
        <div class="form-check mx-3">
          <input class="form-check-input" type="radio" value="seoul" v-model="region_select" name="region">
          <label class="form-check-label">서울</label>
        </div>
        <div class="form-check mx-3">
          <input class="form-check-input" type="radio" value="daejun" v-model="region_select" name="region">
          <label class="form-check-label">대전</label>
        </div>
        <div class="form-check mx-3">
          <input class="form-check-input" type="radio" value="daegu" v-model="region_select" name="region">
          <label class="form-check-label">대구</label>
        </div>
        <div class="form-check mx-3">
          <input class="form-check-input" type="radio" value="pusan" v-model="region_select" name="region">
          <label class="form-check-label">부산</label>
        </div>
        <div class="form-check mx-3">
          <input class="form-check-input" type="radio" value="gwanju" v-model="region_select" name="region">
          <label class="form-check-label">광주</label>
        </div>
      </div>

      <div class="d-flex my-3">

        <div class="form-check mx-3">
          <input class="form-check-input" type="checkbox" value="carrot" v-model="item_select">
          <label class="form-check-label">당근</label>
        </div>

        <div class="form-check mx-3">
          <input class="form-check-input" type="checkbox" value="radish" v-model="item_select">
          <label class="form-check-label">무</label>
        </div>
        
        <div class="form-check mx-3">
          <input class="form-check-input" type="checkbox" value="pear" v-model="item_select" >
          <label class="form-check-label">배</label>
        </div>

        <div class="form-check mx-3">
          <input class="form-check-input" type="checkbox" value="napacabbage" v-model="item_select">
          <label class="form-check-label">배추</label>
        </div>

        <div class="form-check mx-3">
          <input class="form-check-input" type="checkbox" value="lettuce" v-model="item_select">
          <label class="form-check-label">상추</label>
        </div>

        <div class="form-check mx-3">
          <input class="form-check-input" type="checkbox" value="watermelon" v-model="item_select">
          <label class="form-check-label">수박</label>
        </div>

        <div class="form-check mx-3">
          <input class="form-check-input" type="checkbox" value="spinach" v-model="item_select">
          <label class="form-check-label">시금치</label>
        </div>

        <div class="form-check mx-3">
          <input class="form-check-input" type="checkbox" value="cabbage" v-model="item_select">
          <label class="form-check-label">양배추</label>
        </div>

        <div class="form-check mx-3">
          <input class="form-check-input" type="checkbox" value="cucumber" v-model="item_select">
          <label class="form-check-label">오이</label>
        </div>

        <div class="form-check mx-3">
          <input class="form-check-input" type="checkbox" value="tomato" v-model="item_select">
          <label class="form-check-label">토마토</label>
        </div>

        <div class="form-check mx-3">
          <input class="form-check-input" type="checkbox" value="pepper" v-model="item_select" id="pepper" >
          <label class="form-check-label">풋고추</label>
        </div>
      </div>
      <div class="d-flex my-3">

        <div class="form-check mx-3">
          <input class="form-check-input" type="radio" value="30" v-model="day_select" name="day">
          <label class="form-check-label">1개월</label>
        </div>

        <div class="form-check mx-3">
          <input class="form-check-input" type="radio" value="90" v-model="day_select" name="day">
          <label class="form-check-label">3개월</label>
        </div>

        <div class="form-check mx-3">
          <input class="form-check-input" type="radio" value="180" v-model="day_select" name="day">
          <label class="form-check-label">6개월</label>
        </div>

        <div class="form-check mx-3">
          <input class="form-check-input" type="radio" value="365" v-model="day_select" name="day">
          <label class="form-check-label">12개월</label>
        </div>
      </div>
      <button class="btn btn-outline-success" type="button" v-show="!search_show" @click="refreshForm($event)">
        초기화
      </button>
      <button class="btn btn-outline-success" type="submit" v-show="search_show">
        <i class="fa-solid fa-magnifying-glass"></i>
      </button>
      <!-- <div class="w-75 d-flex mt-3 mb-3 m-auto" role="search">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">
          <i class="fa-solid fa-magnifying-glass"></i>
        </button>
      </div> -->
    </form>
    <div class="spinner-border" role="status" v-show="this.$store.state.isLoading" style="width:10vh;height:10vh">
        <span class="visually-hidden">Loading...</span>
    </div>
  <!-- 사진이랑 같이 넣기 -->
<div v-for="Data in chartDataGroup" :key="Data" >
  <section v-show="Data.loaded">
    <div class="container my-5"> 
      <div class="row p-4 pb-0 pe-lg-0 pt-lg-0 align-items-center rounded-3 border">
        <div class="container col-xxl-20 px-10 py-0">
          <div class="row align-items-center g-5 py-5">
            
            <div class="col-8 col-sm-5 col-lg-3">
              <img :src="Data.img" class="card-img-top" alt="...">
              <!-- <img :src="require('@/assets/logo.png')" class="d-block mx-lg-auto img-fluid" alt="Bootstrap Themes" width="437" height="642" loading="lazy"> -->
              <div class="mt-3">
                <span class="h3">단위 : {{Data.unit}}</span>
              </div>
            </div>

            <div class="col-20 col-sm-8 col-lg-8" style="height:50vh;" >
              <LineChart v-if="Data.loaded" v-bind="Data" />
            </div>

          </div>
        </div>
      </div>
    </div>
  </section>
</div>

<!-- <div v-html="ShowCharts"></div> -->
<!-- 사진이랑 같이 넣기 끝------------------------------------------------------------------------- -->


<!-- 
  혹시 모르니까 멀쩡한 그래프 하나 키핑

  <div style="height:200px;display: flex;">
  <div style="width:200px;height:200px;margin:20px;">
  </div>
  <LineChart/>
</div> 
-->
</template>

<script>
import axios from 'axios';
import LineChart from '@/components/LineChartThreeLine.vue'

export default {
  name: 'PriceCatgory',
  components: { LineChart},
  data() {
    return {
      chartDataGroup:[],
      chartData : {
        xlabel: [],
        datas: [[],[],[]],
        legend: [],
        item: "",
        item_kor: "",
        region: "",
        img: "",
        unit: "",
        loaded: false,
      },
      region_select:"seoul",
      item_select:['carrot'],
      day_select:"30",
      search_show:true,
    }
  },
  computed: {
  },
  mounted(){
  },
  methods: {
    async submitform(){
      this.$store.commit('setIsLoading', true);
      // console.log(this.chartDataGroup)
      this.chartDataGroup=[]
      // console.log(this.chartDataGroup)
      
      var urls = []
      var items_kor = ["당근","무","배","배추","상추","수박","시금치","양배추","오이","토마토",'풋고추']
      var unit = ["20kg","20kg","15kg","10kg","4kg","1개","4kg","8kg","50개","5kg",'10kg']
      var items = ["carrot","radish","pear","napacabbage","lettuce","watermelon","spinach","cabbage","cucumber","tomato",'pepper']
      this.item_select.forEach( item => {
        var url='/api/v1/' +this.region_select+ '_price_api/?item=' +item + '&expand=True&period='+this.day_select+'&past='+0
        urls.push(url) // url 저장
      })
      // console.log(urls)
      var resultData = new Array(urls.length) //배열 크기 생성
      await axios
      .all(urls.map((url) => axios.get(url))) // 가변적 get
      .then(axios.spread((...resultData) => { // 가변적 데이터 할당
            const _ = require("lodash") //deepcopy js 모듈 임포트
            // console.log(resultData)
            for (var num=0;num<resultData.length;num++) {
              for (var step=0;step<this.day_select;step++) {
                this.chartData.xlabel[step]=(resultData[num].data[step].ds)
                  this.chartData.item=(resultData[num].data[step].item)//범례명
                  if (resultData[num].data[step].price === 0) {
                    this.chartData.datas[0][step]=(resultData[num].data[step].ythat)
                    this.chartData.datas[1][step]=(resultData[num].data[step].yhat_lower)
                    this.chartData.datas[2][step]=(resultData[num].data[step].yhat_upper)
                    
                  } else {
                    this.chartData.datas[0][step]=(resultData[num].data[step].price)
                  }
                }
              this.chartData.item_kor=(items_kor[items.indexOf(this.chartData.item)])
              this.chartData.unit=(unit[items.indexOf(this.chartData.item)])
              this.chartData.img=require("@/assets/"+this.chartData.item_kor+'1.jpg')
              // console.log(this.chartData.img)
              this.chartData.legend = ['기댓값','최소 기댓값', "최대 기댓값"]//범례명
              this.chartData.loaded=true
              // console.log(this.chartData)
              const clone6 = _.cloneDeep(this.chartData) // deepcopy
              this.chartDataGroup[num]=(clone6)
            }
            // console.log(this.chartDataGroup)
            this.search_show=false
            console.log(this.chartDataGroup)
          }))
      .catch(error => {
        console.log(error)
      })
      this.$store.commit('setIsLoading', false);
    },
    refreshForm(event) {
      window.location.reload()
    }
  }
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
</style>

<!-- 원본도 키핑
<template>
<div style="height:200px;display: flex;">
  <div style="width:200px;height:200px;margin:20px;">
  </div>
  <LineChart/>
</div>
</template>

<script>
import LineChart from '@/components/BarChart.vue'

export default {
  name: 'PriceCatgory',
  components: { LineChart }
}

</script>
-->