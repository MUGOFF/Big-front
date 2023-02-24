<template>
<!-- 계약서 페이지 -->
  <div class="container">
    <div class="title" >
      <span style="font-weight:bold; font-size:2em;">계약서 작성 </span>
    </div>
    <div class='row g-5 '>
      <!-- 왼쪽 -->
      <div class='col-sm-6'>
        <div class='row g-3'>
          <div class='col-sm-6'>
            <h5 style="font-weight:bold;">매도인(갑)</h5>
            <finalName v-if="loaded" v-bind="seller"/>         
          </div>
          <div class='col-sm-6'>
            <h5 style="font-weight:bold;">매수인(을)</h5>
            <Name @input_data="input_buyer"/>
          </div>
        </div>
        <br>
        <hr style="width:100%;height:5px;border:none;background-color:grey;">
        <Left @input_data="input_buisness"/>
      </div>

      <!-- 오른쪽 -->
      <Right @input_data="input_right"/>
    </div>
  </div>
  <br>
  <div class="col-12">
    <input class="form-check-input" type="checkbox" id="gridCheck" v-model="agree">
    <label class="form-check-label" for="gridCheck">
      위 사항을 읽었으며, 계약내용에 동의합니다.
    </label>
  </div>
  <br>
  <div class="col-12">
    <button type="submit" class="btn btn-primary" @click="submitContract($event)" >계약진행</button>
  </div>
  <br>
</template>
  
<script>
// @ is an alias to /src
import axios from "axios"
import Name from '@/components/ContractName.vue'
import finalName from '@/components/Contractfinal_Name.vue'
import Right from '@/components/ContractRight.vue'
import Left from '@/components/ContractLeft.vue'

export default {
  name: 'ContractView',
  components: {
    Name,Right,Left,finalName
  },
  data() {
    return {
      buyer:{
        name: "",
        birth: "1970-01-01",
        address: "",
        phone: "",
        email: "",
      },
      seller: {
        name: "임시이름",
        birth: "1970-01-01",
        address: "임시주소",
        phone: "0000000000",
        email: "",
      },
      business: {
        region : "",
        sub_region : "",
        town : "",
        category : "",
        item : "",
        area : "",
        f_date : "",
      },
      right: {
        p_date : "",
        p_value: "",
        a_value: "",
        a_date: "",
        i_value: "",
        i_date: "",
        b_value: "",
        b_date: "",
        g_date: "",
      },
      loaded:false,
      specials:"",
      agree:false,
      job:"",
      s_confirm:"False",
      b_confirm:"False",
    }
  },
  mounted(){
    this.get_username()
  },
  methods: {
    get_username() {
      axios.get('api/v1/article_detail/?id='+Number(this.$route.params.c_id))
      .then(response => {
        this.loaded=true
        this.seller.email = response.data[0].seller_email
        this.seller.name = response.data[0].seller_name
        axios
        .get('user/'+ this.$store.state.token)
        .then(response => {
          this.job = response.data.job
          if (response.data.job=='유통업자'){
            this.buyer.email = response.data.email;
          }
          // console.log(this.buyer.email)
        })
        .catch(error => {
          console.log(error);
        })
      })
      .catch(error => {
        console.log(error)
      })
    },
    submitContract() {
      // console.log(this.buyer.email)
      // console.log(this.buyer)
      if (this.agree===false) {
        alert("동의함을 체크하십시오")
        return false
      }
      // for (var info in this.seller) {
      //   if (this.seller[info]===undefined || this.seller[info]==="") {
      //     alert("매도인 정보를 모두 입력하십시오")
      //     return false
      //   }
      // }
      for (var info in this.buyer) {
        if (this.buyer[info]===undefined || this.buyer[info]==="") {
          alert("매수인 정보를 모두 입력하십시오")
          return false
        }
      }
      for (var info in this.business) {
        if (this.business[info]===undefined || this.business[info]==="") {
          alert("계약정보를 모두 입력하십시오")
          return false
        }
      }
      for (var info in this.right) {
        if (this.right[info]===undefined || this.right  [info]==="") {
          alert("계약정보를 모두 입력하십시오")
          return false
        }
      }
      if(this.specials===undefined) {
        this.specials=""
        return false
      }
      if(this.job==='유통업자') {
        this.b_confirm="True"
      } else {
        this.s_confirm="True"
      }
      axios
      .post('Contract_list/', {
        // post:Number(this.$route.params.c_id),
        buyer_name:this.buyer.name,
        seller_name:this.seller.name,
        buyer_birth:this.buyer.birth,
        seller_birth:this.seller.birth,
        buyer_email:this.buyer.email,
        seller_email:this.seller.email,
        buyer_address:this.buyer.address,
        seller_address:this.seller.address,
        buyer_phone:this.buyer.phone,
        seller_phone:this.seller.phone,
        farm_address:this.business.region+" "+this.business.sub_region+" "+this.business.town,
        item:this.business.category+" "+this.business.item,
        farm_area:Number(this.business.area.replace(",","")),
        farm_date:this.business.f_date,
        payment_date:this.right.p_date,
        payment:Number(this.right.p_value.replace(",","")),
        advance_date:this.right.a_date,
        advance:Number(this.right.a_value.replace(",","")),
        interpay_date:this.right.i_date,
        interpay:Number(this.right.i_value.replace(",","")),
        balance_date:this.right.b_date,
        balance:Number(this.right.b_value.replace(",","")),
        goods_date:this.right.g_date,
        special_contract:this.specials,
        buyer_confirmed:this.b_confirm,
        seller_confirmed:this.s_confirm,
      })
      .then(response => {
          alert('계약을 진행합니다.')
          this.$router.push('/mypage')
      })
      .catch(error => {
          console.log(error)
      })
    },
    input_seller(data) {
      this.seller.name=data.name
      this.seller.birth=data.birth
      this.seller.address=data.address
      this.seller.phone=data.phone
    },
    input_buyer(data) {
      this.buyer.name=data.name
      this.buyer.birth=data.birth
      this.buyer.address=data.address
      this.buyer.phone=data.phone
    },
    input_buisness(data) {
      this.business.region = data.region
      this.business.sub_region = data.sub_region
      this.business.town = data.town
      this.business.category = data.category
      this.business.item = data.item
      this.business.area = data.area
      this.business.f_date = data.f_date
    },
    input_right(data) {
      this.right.p_value = data.p_value,
      this.right.p_date = data.p_date
      this.right.a_value = data.a_value,
      this.right.a_date = data.a_date,
      this.right.i_value = data.i_value,
      this.right.i_date = data.i_date,
      this.right.b_value = data.b_value,
      this.right.b_date = data.b_date,
      this.right.g_date = data.g_date,
      this.specials = data.special
    },
  }
}
</script>

<style scoped>
  .btn{
    /* color: #000; */
    background-color: #9ac486;
    border: none;
  }
</style>