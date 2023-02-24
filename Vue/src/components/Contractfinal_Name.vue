<template>
<!-- 매도인 매수인 -->
  <div class='col-sm-12'>
    <form class="row g-3">
      <div class="col-12">
        <label>성명</label>
        <input type="text" class="form-control" placeholder="홍길동" v-model="name" readonly>
      </div>
      <div class="col-12">  
        <label>생년월일</label>
        <input type="date" class="form-control" v-model="birth" readonly>
      </div>
      <div class="col-12">
        <label>주소</label>
        <textarea class="form-control" rows="3" v-model="address" readonly></textarea>
      </div>
      <div class="col-12">
        <label>연락처</label>
        <input type="text" class="form-control" placeholder="01012345678" v-model="phone" readonly>
      </div>
    </form>
  </div>
</template>
    
<script>
    export default {
        name: 'finalcontractName',
        components: {
        },
        props: {
          name: {type: String},
          birth: {type: String},
          address: {type: String},
          phone: {type: String},
        },
        data() {
          return {
            name: this.name,
            birth: this.birth,
            address: this.address,
            phone: this.phone,
          }
        },
        methods: {
          // toUPward() {
          //   console.log(this.name)
          //   this.$emit('input',this.name,this.birth,this.address,this.phone)
          // }
          // inputName(event) {
          //   let personal_data = { 
          //     'name': this.name,
          //     'birth': this.birth,
          //     'address': this.address,
          //     'phone': this.phone,
          //   }
          //   this.$emit('input_data',personal_data)
          // }
        }
    };
</script>

<style scoped>
</style>
      