<template>
<!-- 매도인 매수인 -->
  <div class='col-sm-12'>
    <form class="row g-3">
      <div class="col-12">
        <label>성명</label>
        <input type="text" class="form-control" placeholder="홍길동" v-model="name" @input="inputName($event)">
      </div>
      <div class="col-12">  
        <label>생년월일</label>
        <input type="date" class="form-control" v-model="birth" @input="inputName($event)">
      </div>
      <div class="col-12">
        <label>주소</label>
        <button type="button" class="btn btn-light btn-sm" @click="showApi">주소 찾기</button>
        <textarea class="form-control" rows="3" v-model="address" @input="inputName($event)"></textarea>
      </div>
      <div class="col-12">
        <label>연락처</label>
        <input type="text" class="form-control" placeholder="01012345678" v-model="phone" @input="inputName($event)">
      </div>
    </form>
  </div>
</template>
    
<script>
    export default {
        name: 'contractName',
        components: {
        },
        // props: {
        //   name: {type: String},
        //   birth: {type: String},
        //   address: {type: String},
        //   phone: {type: String},
        // },
        data() {
          return {
            name: "",//this.name,
            birth: "1969-01-01",//this.birth,
            address: "",//this.address,
            phone: "",//this.phone,
          }
        },
        methods: {
          // toUPward() {
          //   console.log(this.name)
          //   this.$emit('input',this.name,this.birth,this.address,this.phone)
          // }
          inputName(event) {
            let personal_data = { 
              'name': this.name,
              'birth': this.birth,
              'address': this.address,
              'phone': this.phone,
            }
            this.$emit('input_data',personal_data)
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
                this.address = this.address + this.zip
                this.address_base = fullRoadAddr;
                this.address = this.address + this.address_base
            }
            }).open()
          },
        }
    };
</script>

<style scoped>
</style>
      