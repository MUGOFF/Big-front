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
            <finalName v-if="loaded" v-bind="buyer"/>
          </div>
          <div class='col-sm-6'>
            <h5 style="font-weight:bold;">매수인(을)</h5>
            <Name @input_data="input_seller"/>
          </div>
        </div>
        <br>
        <hr style="width:100%;height:5px;border:none;background-color:grey;">
        <Left v-if="loaded" v-bind="business" @input_data="input_buisness"/>
      </div>

      <!-- 오른쪽 -->
      <Right v-if="loaded" v-bind="right"/>
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
    <button type="submit" class="btn btn-danger m-2" @click="refuseContract($event)" >계약거부</button>
    <button type="submit" class="btn btn-primary m-2" @click="submitContract($event)" >계약진행</button>
  </div>
  <br>
</template>
  
<script>
// @ is an alias to /src
import axios from "axios"
import Name from '@/components/ContractName.vue'
import finalName from '@/components/Contractfinal_Name.vue'
import Right from '@/components/Contractfinal_Right .vue'
import Left from '@/components/Contractfinal_Left.vue'

export default {
  name: 'ContractView_final',
  components: {
    Name,Right,Left,finalName
  },
  data() {
    return {
      contract_form : {},
      buyer:{
        name: "",
        birth: "1970-01-01",
        address: "",
        phone: "",
        email: "",
      },
      seller: {
        name: "",
        birth: "1970-01-01",
        address: "",
        phone: "",
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
        special:"",
      },
      agree:false,
      job:"",
      loaded:false,
      s_confirm:"False",
      b_confirm:"False",
    }
  },
  created(){
    this.get_Suggestion()
  },
  methods: {
    get_Suggestion() {
      axios.get('Contract_sign/?id='+Number(this.$route.params.c_id))
      .then(response => {
        // console.log(response)
        this.contract_form = response.data[0]
        this.buyer={
        name: response.data[0].buyer_name,
        birth: response.data[0].buyer_birth,
        address: response.data[0].buyer_address,
        phone: response.data[0].buyer_phone,
        }
        this.seller={
          email: response.data[0].seller_email,
        }
        this.business= {
          region : response.data[0].farm_address.split(' ')[0],
          sub_region : response.data[0].farm_address.split(' ')[1],
          town : response.data[0].farm_address.split(' ')[2],
          category : response.data[0].item.split(' ')[0],
          item : response.data[0].item.split(' ')[1],
          area : response.data[0].farm_area,
          f_date : response.data[0].farm_date,
        }
        this.right= {
          p_date : response.data[0].payment_date,
          p_value: response.data[0].payment,
          a_value: response.data[0].advance,
          a_date: response.data[0].advance_date,
          i_value: response.data[0].interpay,
          i_date: response.data[0].interpay_date,
          b_value: response.data[0].balance,
          b_date: response.data[0].balance_date,
          g_date: response.data[0].goods_date,
          special:response.data[0].special_contract
        }
        this.loaded=true
        // console.log(this.right)
        console.log(this.business)
      })
      .catch(error => {
        console.log(error)
      })
    },
    refuseContract(){
      axios
      .delete('Contract_sign/?id='+Number(this.$route.params.c_id))
      .then(response => {
        console.log(response)
      })
      .catch(error => {
        console.log(error)
      })

      this.$router.push('/mypage')
    },
    submitContract() {
      if (this.agree===false) {
        alert("동의함을 체크하십시오")
        return false
      }
      for (var info in this.buyer) {
        if (this.seller[info]===undefined || this.seller[info]==="") {
          alert("매수인 정보를 모두 입력하십시오")
          return false
        }
      }
      for (var info in this.business) {
        if (this.business[info]===undefined || this.business[info]==="") {
          console.log(this.business)
          alert("계약정보를 모두 입력하십시오")
          return false
        }
      }
      if(this.specials===undefined) {
        this.specials=""
        return false
      }
      // if(this.job==='유통업자') {
      //   this.b_confirm="True"
      // } else {
      //   this.s_confirm="True"
      // }
      axios
      .put('Contract_sign/?id='+Number(this.$route.params.c_id), {
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
        farm_area:Number(this.business.area),
        farm_date:this.business.f_date,
        payment_date:this.business.p_date,
        payment:Number(this.right.p_value),
        advance_date:this.right.a_date,
        advance:Number(this.right.a_value),
        interpay_date:this.right.i_date,
        interpay:Number(this.right.i_value),
        balance_date:this.right.b_date,
        balance:Number(this.right.b_value),
        goods_date:this.right.g_date,
        special_contract:this.right.special,
        buyer_confirmed:'True',
        seller_confirmed:'True',
      })
      .then(response => {
          alert('계약이 체결되었습니다.')
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
      // this.business.category = data.category
      // this.business.item = data.item
      // this.business.area = data.area
      this.business.f_date = data.f_date
    },
    input_right(data) {
      this.right.p_value = data.p_value,
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