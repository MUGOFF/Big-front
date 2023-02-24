<template>
  <div id="product-buyer">
    <div id="left">
      <div id="left-top">
        <div style="font-weight: 700; font-size: 35px;">상세정보</div>
        <img style="width:100%" :src="require(`@/assets/product/${imgName}`)"/>
      </div>
      <div id="left-bottom">
        <div id="left-title">
          <div style="font-weight: 700; font-size: 30px;">상품명</div>
          <div align="right" style="color:gray;">게시일 : {{ date }}</div>
        </div>
        <table class="table table-borderless">
          <tbody>
            <tr>
              <td width="150"><div id="list">판매자</div></td>
              <td id="listTable">{{ seller }} <button type="button" class="btn btn-light btn-sm">프로필보기</button></td>
            </tr>
            <tr>
              <td width="150"><div id="list">품종</div></td>
              <td id="listTable">{{ kind }}</td>
            </tr>
            <tr>
              <td width="150"><div id="list">지역</div></td>
              <td id="listTable">{{ region }}</td>
            </tr>
            <tr>
              <td width="150"><div id="list">품질</div></td>
              <td id="listTable">{{ quality }}</td>
            </tr>
            <tr>
              <td width="150"><div id="list">면적</div></td>
              <td id="listTable">{{ area }}</td>
            </tr>
            <tr>
              <td width="150"><div id="list">판매가격</div></td>
              <td id="listTable">{{ price }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div id="right">
      <div id="right-top" style="width:100%;height:480px;margin:20px;">
        <LineChart/>
      </div>
      <div id="right-bottom">
        <table class="table table-borderless">
          <tbody>
            <tr>
              <td width="150"><div id="list">메시지</div></td>
              <td id="listTable"><input type="text" class="form-control" v-model="message" placeholder="제안 메세지 입력"> </td>
            </tr>
            <tr>
              <td width="150"><div id="list">제안가</div></td>
              <td id="listTable"><input type="text" class="form-control" v-model="message" placeholder="제안가 입력"></td>
            </tr>
          </tbody>
        </table>
        <table class="table table-borderless" style="'width:100%">
          <tr>
            <td style="width:30%"><button type="button" class="btn btn-outline-danger w-100"><span id="button-text">취소하기</span></button></td>
            <td style="width:30%"><button type="button" class="btn btn-primary w-100"><span id="button-text">제안하기</span></button></td>
            <td style="width:40%"><button type="button" class="btn btn-success w-100"><span id="button-text">계약하기</span></button> </td>
          </tr>
        </table>
      </div>
    </div>
  </div>
</template>
<script>
import LineChart from '@/components/BarChart.vue'
export default {
  name: 'ProposalBuyer',
  components: { LineChart },
  data() {
    return {
      "title": "상품명",
      "date": "2022-00-00",
      "imgName": "lettuce.png",
      "kind": "상추",
      "region": "상세 주소",
      "quality": "좋음",
      "area": "500평 (1652.89m2)",
      "price": "100,000원 (Kg)",
      "seller": "김농부",
      "message": '',
      "proposalprice": ''
    }
  }
}
</script>
<style scoped>
#product-buyer {
  margin-left: 100px;
  margin-right: 100px;
  padding-top: 10px;
  overflow: hidden;
}
#left {
  padding-top: 10px;
  float:left;
  width: 50%;
  padding-bottom: 50px;
  padding-right: 10px;
}
#left-top {
  padding-top: 10px;
}
#left-bottom {
  border-top: 3px solid #9ac486;
  border-bottom: 3px solid #9ac486;
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
