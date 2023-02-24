<template>
  <!-- 농산물가격 카드 -->
  <div class="row row-cols-1 row-cols-md-4 g-4">
      <div class="col">
        <div class="card h-100">
          <img src="@/assets/당근1.jpg" class="card-img-top" alt="Card image cap" style="height:200px;">
            <div class="card-body">
              <h5 class="card-title">당근/20kg</h5>
              <div class="col-20 col-sm-8 col-lg-8" >
              <div class="spinner-border" role="status" v-show="this.$store.state.isLoading" style="width:10vh;height:10vh">
                <span class="visually-hidden">Loading...</span>
              </div>
              <div style="width:20vw;height:200px;" v-show="!(this.$store.state.isLoading)">
                <LineChart v-if="chartData.loaded" v-bind="chartDataGroup['carrot']"/>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <div class="col">
        <div class="card h-100">
          <img src="@/assets/무1.jpg" class="card-img-top" alt="..." style="height:200px;">
          <div class="card-body">
            <h5 class="card-title">무/20kg</h5>
            <div class="col-20 col-sm-8 col-lg-8" >
              <div class="spinner-border" role="status" v-show="this.$store.state.isLoading" style="width:10vh;height:10vh">
                <span class="visually-hidden">Loading...</span>
              </div>
              <div style="width:20vw;height:200px;" v-show="!(this.$store.state.isLoading)">
                <LineChart v-if="chartData.loaded" v-bind="chartDataGroup['cabbage']"/>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <div class="col">
        <div class="card h-100">
          <img src="@/assets/배1.jpg" class="card-img-top" alt="..." style="height:200px;">
          <div class="card-body">
            <h5 class="card-title">배/15kg</h5>
            <div class="col-20 col-sm-8 col-lg-8" >
              <div class="spinner-border" role="status" v-show="this.$store.state.isLoading" style="width:10vh;height:10vh">
                <span class="visually-hidden">Loading...</span>
              </div>
              <div style="width:20vw;height:200px;" v-show="!(this.$store.state.isLoading)">
                <LineChart v-if="chartData.loaded" v-bind="chartDataGroup['pear']"/>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <div class="col">
        <div class="card h-100">
          <img src="@/assets/배추1.jpg" class="card-img-top" alt="..." style="height:200px;">
          <div class="card-body">
            <h5 class="card-title">배추/10kg</h5>
            <div class="col-20 col-sm-8 col-lg-8" >
              <div class="spinner-border" role="status" v-show="this.$store.state.isLoading" style="width:10vh;height:10vh">
                <span class="visually-hidden">Loading...</span>
              </div>
              <div style="width:20vw;height:200px;" v-show="!(this.$store.state.isLoading)">
                <LineChart v-if="chartData.loaded" v-bind="chartDataGroup['napacabbage']"/>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <div class="col">
        <div class="card h-100">
          <img src="@/assets/상추1.jpg" class="card-img-top" alt="..." style="height:200px;">
          <div class="card-body">
            <h5 class="card-title">상추/4kg</h5>
            <div class="col-20 col-sm-8 col-lg-8" >
              <div class="spinner-border" role="status" v-show="this.$store.state.isLoading" style="width:10vh;height:10vh">
                <span class="visually-hidden">Loading...</span>
              </div>
              <div style="width:20vw;height:200px;" v-show="!(this.$store.state.isLoading)">
                <LineChart v-if="chartData.loaded" v-bind="chartDataGroup['lettuce']"/>
              </div>
            </div>
          </div>
        </div>
      </div>    
      
      <div class="col">
        <div class="card h-100">
          <img src="@/assets/수박1.jpg" class="card-img-top" alt="..." style="height:200px;">
          <div class="card-body">
            <h5 class="card-title">수박/1개당</h5>
            <div class="col-20 col-sm-8 col-lg-8" >
              <div class="spinner-border" role="status" v-show="this.$store.state.isLoading" style="width:10vh;height:10vh">
                <span class="visually-hidden">Loading...</span>
              </div>
              <div style="width:20vw;height:200px;" v-show="!(this.$store.state.isLoading)">
                <LineChart v-if="chartData.loaded" v-bind="chartDataGroup['watermelon']"/>
              </div>
            </div>
          </div>
        </div>
      </div>
  
      <div class="col">
        <div class="card h-100">
          <img src="@/assets/시금치1.jpg" class="card-img-top" alt="..." style="height:200px;">
          <div class="card-body">
            <h5 class="card-title">시금치/4kg</h5>
            <div class="col-20 col-sm-8 col-lg-8" >
              <div class="spinner-border" role="status" v-show="this.$store.state.isLoading" style="width:10vh;height:10vh">
                <span class="visually-hidden">Loading...</span>
              </div>
              <div style="width:20vw;height:200px;" v-show="!(this.$store.state.isLoading)">
                <LineChart v-if="chartData.loaded" v-bind="chartDataGroup['spinach']"/>
              </div>
            </div>
          </div>
        </div>
      </div>
  
      <div class="col">
        <div class="card h-100">
          <img src="@/assets/양배추1.jpg" class="card-img-top" alt="..." style="height:200px;">
          <div class="card-body">
            <h5 class="card-title">양배추/8kg</h5>
            <div class="col-20 col-sm-8 col-lg-8" >
              <div class="spinner-border" role="status" v-show="this.$store.state.isLoading" style="width:10vh;height:10vh">
                <span class="visually-hidden">Loading...</span>
              </div>
              <div style="width:20vw;height:200px;" v-show="!(this.$store.state.isLoading)">
                <LineChart v-if="chartData.loaded" v-bind="chartDataGroup['cabbage']"/>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <div class="col">
        <div class="card h-100">
          <img src="@/assets/오이1.jpg" class="card-img-top" alt="..." style="height:200px;">
          <div class="card-body">
            <h5 class="card-title">오이/50개당</h5>
            <div class="col-20 col-sm-8 col-lg-8" >
              <div class="spinner-border" role="status" v-show="this.$store.state.isLoading" style="width:10vh;height:10vh">
                <span class="visually-hidden">Loading...</span>
              </div>
              <div style="width:20vw;height:200px;" v-show="!(this.$store.state.isLoading)">
                <LineChart v-if="chartData.loaded" v-bind="chartDataGroup['cucumber']"/>
              </div>
            </div>
          </div>
        </div>
      </div>
  
      <div class="col">
        <div class="card h-100">
          <img src="@/assets/토마토1.jpg" class="card-img-top" alt="..." style="height:200px;">
          <div class="card-body">
            <h5 class="card-title">토마토/5kg</h5>
            <div class="col-20 col-sm-8 col-lg-8" >
              <div class="spinner-border" role="status" v-show="this.$store.state.isLoading" style="width:10vh;height:10vh">
                <span class="visually-hidden">Loading...</span>
              </div>
              <div style="width:20vw;height:200px;" v-show="!(this.$store.state.isLoading)">
                <LineChart v-if="chartData.loaded" v-bind="chartDataGroup['tomato']"/>
              </div>
            </div>
          </div>
        </div>
      </div>
    
      <div class="col">
        <div class="card h-100">
          <img src="@/assets/풋고추1.jpg" class="card-img-top" alt="..." style="height:200px;">
          <div class="card-body">
            <h5 class="card-title">풋고추/10kg</h5>
            <div class="col-20 col-sm-8 col-lg-8" >
              <div class="spinner-border" role="status" v-show="this.$store.state.isLoading" style="width:10vh;height:10vh">
                <span class="visually-hidden">Loading...</span>
              </div>
              <div style="width:20vw;height:200px;" v-show="!(this.$store.state.isLoading)">
                <LineChart v-if="chartData.loaded" v-bind="chartDataGroup['pepper']"/>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
      
  <script>
  import axios from 'axios'
  import LineChart from '@/components/LineChart _Oneline.vue'
  
  export default {
    name: 'vegetableCard',
    components: { LineChart},
    data() {
        return {
          chartDataGroup:[],
          chartData : {
            xlabel: [],
            datas: [],
            legend: "",
            item: "",
            item_kor: "",
            loaded: false,
          },
        }
      },
      computed: {
      },
      mounted(){
        this.getDataValueAll()
      },
      methods: {
        async getDataValueAll() {
          this.$store.commit('setIsLoading', true);

          var items = ["carrot","radish","pear","napacabbage","lettuce","watermelon","spinach","cabbage","cucumber","tomato",'pepper'] //당근, 무, 배, 배추, 상추, 수박, 시금치, 양배추, 오이, 토마토, 풋고추
          var items_kor = ["당근","무","배","배추","상추","수박","시금치","양배추","오이","토마토",'풋고추'] //당근, 무, 배, 배추, 상추, 수박, 시금치, 양배추, 오이, 토마토, 풋고추
          var urls = []
          items.forEach( item => {
            var url='/api/v1/seoul_price_api/?item='+item+'&expand=True&period='+0+'&past='+30
            urls.push(url) // url 저장
          })
          var resultData = new Array(urls.length) //배열 크기 생성
          await axios
          .all(urls.map((url) => axios.get(url))) // 가변적 get
          // .get(url)
          .then(axios.spread((...resultData) => { // 가변적 데이터 할당
            // .then(response => {
              const _ = require("lodash") //deepcopy js 모듈 임포트
              console.log(resultData)
              for (var num=0;num<resultData.length;num++) {
                for (var step=0;step<30;step++) {
                    this.chartData.xlabel[step]=(resultData[num].data[step].ds)
                    this.chartData.datas[step]=(resultData[num].data[step].price)
                    this.chartData.item=(resultData[num].data[step].item)//범례명
                }
                var item_index = this.chartData.item
                this.chartData.item_kor=(items_kor[items.indexOf(this.chartData.item)])
                this.chartData.legend = 'price'//범례명
                this.chartData.loaded=true
                // console.log(this.chartData)
                const clone6 = _.cloneDeep(this.chartData) // deepcopy
                this.chartDataGroup[item_index]=(clone6)
              }
          //       // console.log(resultData[index])
          //       // console.log(resultData[index].config.url.split('/')[3].slice(0,-5)+resultData[index].data[0].item)
                
              // }
              // console.log(this.chartData.legend)
          //     // console.log('----------------')
          //   }
          // console.log(this.chartDataGroup)
        }))
        .catch(error => {
          console.log(error)
        })
        this.$store.commit('setIsLoading', false);
      }
    }
  }
  </script>
  
  
        