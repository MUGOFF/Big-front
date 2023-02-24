<template>
  <div id="product">
    <div id="left">
      <div class="upload-box">
        <div id="drop-file" class="drag-file">
          <img id="profile-img" :style="`background-image:url(${imgName})`">
        </div>
      </div>
      <label class="file-label" for="chooseFile">농작물 사진 업로드</label>
      <input class="file" id="chooseFile" type="file"  @change="fileChange" accept="image/*">
      <table class="table table-borderless" style="margin-top: 20px;">
        <tbody>
          <tr>
            <td width="150px"><div id="list">판매자</div></td>
            <td id="listTable" align="left">{{ seller }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div id="right">
      <div id="rightTitle">
        <input class="form-control" style="font-weight: 700; font-size: 25px" type="text" placeholder="제목" v-model="title">
        <div align="right" style="color:gray;"><input type="date" class="form-control" v-model="date"></div>
        
      </div>
      <table class="table table-borderless">
        <tbody>
          <tr>
            <td width="150"><div id="list">품종</div></td>
            <td id="listTable">
              <select class="form-select" v-model="kind" required>
                  <option disabled selected style="display:none;">품종 선택</option>
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
            </td>
          </tr>
          <tr>
            <td width="150"><div id="list">지역</div></td>
            <td id="listTable">
              <select class="form-select" v-model="region_kor" required>
                  <option disabled selected style="display:none;">지역 선택</option>
                  <option v-for="region in regions" :key="region">{{region}}</option>
                  <!-- <option value="pusan">부산</option>
                  <option value="daegu">대구</option>
                  <option value="gwanju">광주</option>
                  <option value="dawjun">대전</option> -->
              </select>
            </td>
          </tr>
          <tr>
            <td width="150"><div id="list">상세지역</div></td>
            <td id="listTable">
              <select class="form-select" v-model="sub_region">
                <option disabled selected style="display:none;">상세지역 선택</option>
                <option v-for="subregion in subregions[region_kor]" :key="subregion">{{ subregion }}</option>
              </select>
            </td>
          </tr>
          <tr>
            <td width="150"><div id="list">품질</div></td>
            <td id="listTable">
              <select class="form-select" v-model="quality" required>
                  <option disabled selected style="display:none;">품질 선택</option>
                  <option value="상등품">상등품</option>
                  <option value="정품">정품</option>
                  <option value="비품">비품</option>
              </select>
            </td>
          </tr>
          <tr>
            <td width="150"><div id="list">면적</div></td>
            <td id="listTable">
              <select class="form-select" v-model="area">
                <option disabled selected style="display:none;">규모 선택</option>
                  <option value="0">전체</option>
                  <option value="1000">1,000평 이상</option>
                  <option value="5000">5,000평 이상</option>
                  <option value="10000">10,000평 이상</option>
                  <option value="50000">50,000평 이상</option>
                  <option value="100000">100,000평 이상</option>
              </select>
            </td>
          </tr>
          <tr>
            <td width="150"><div id="list">판매가격</div></td>
            <td><input type="text" class="form-control" id="listTable" v-model="price" name="rcvordAm" numberOnlyMinComma="true" koreanCurrency="true" required="required" placeholder="입력단위: 천원"></td>
          </tr>
        </tbody>
      </table>
      <div class="buttons">
        <button type="button" style="flex:5;" class="btn btn-outline-success w-100" @click="upload_article"><span id="button-text">등록하기</span></button>
      </div>
      <br>
    </div>
    <div id="bottom">
      <div id="title">상세 정보</div>
      <div id="detail">
        <textarea class="form-control" rows="10" v-model="detail" placeholder="구매자에게 보여질 상세 정보를 기입하세요."></textarea>
      </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios';
import $ from 'jquery';
export default {
  name: 'ProductView',
  data() {
    return {
      regions: ['서울','부산','대구','광주','대전'],
      subregions: {
        '서울': ['종로구','중구','용산구','성동구','광진구','동대문구','중랑구',
          '성북구','강북구','도봉구','노원구','은평구','서대문구','마포구','양천구',
          '강서구','구로구','금천구','영등포구','동작구','관악구','서초구','강남구','송파구','강동구'],
        '부산': ['중구','서구','동구','영도구','부산진구','동래구','남구','북구',
          '강서구','해운대구','사하구','금정구','연제구','수영구','사상구','기장군'],
        '대구': ['중구','동구','서구','남구','북구','수성구','달서구','달성군'],
        '광주': ['동구','서구','남구','북구','광산구'],
        '대전': ['동구','중구','서구','유성구','대덕구'],
      },
      imgName: "",
      seller: "",
      title: "",
      date: "2023-01-01",
      kind: "",
      region_kor: "",
      region: "",
      sub_region: "",
      quality: "",
      area: "",
      price: "",
      detail: "",
    }
  },
  mounted() {
    this.get_username()
  },
  methods: {
    fileChange: function(e) {
      // console.log(e.target.files)//files는 배열로 들어온다.
              // console.log(typeof(e.target.files[0]))//files는 배열로 들어온다.
              let url = URL.createObjectURL(e.target.files[0]);
              // console.log(url);
              // console.log(typeof(url));
              this.imgPath = e.target.files[0];
              this.imgName = url;
          },
          upload_article() {
            var region_kor= ['서울','부산','대구','광주','대전']
            var region= ['seoul','pusan','daegu','gwanju','daejun']
            this.region = region[region_kor.indexOf(this.region_kor)]
            // console.log(this.region)
            // console.log(Number(this.price.replace(',','')))
            let data = new FormData()
            data= {
              profile:this.imgPath,
              seller_name:this.seller,
              seller_email:this.seller_email, 
              g_date:this.date,
              title:this.title,
              item:this.kind, 
              region:this.region, 
              sub_region:this.sub_region, 
              quality:this.quality, 
              area:Number(this.area), 
              price:Number(this.price.replace(',','')), 
              description:this.detail, 
            }
            let AxiosConfig = {
                headers: {
                    "Content-Type": "multipart/form-data",
                }
            }
            axios.post('api/v1/article_list/',data,AxiosConfig)
            .then(response => {
              console.log(response)
              this.$router.push({
                path: '/product/' + response.data.id
              })
            })
            .catch(error => {
              console.log(error)
            })
          },
          get_username() {
            axios
            .get('user/'+ this.$store.state.token)
            .then(response => {
              this.seller_email = response.data.email;
              this.seller = response.data.username;
              // console.log(response.data)
            })
            .catch(error => {
              console.log(error);
            })
          },
        },
}

// 숫자 적으면 알아서 콤마랑 글자 적어주는 제이쿼리문
$(document).on("keyup", "input:text[numberOnlyMinComma]", function()	{
	var strVal = $(this).val();

	event = event || window.event;
	var keyID = (event.which) ? event.which : event.keyCode;

	if( ( keyID >=48 && keyID <= 57 ) || ( keyID >=96 && keyID <= 105 )
				|| keyID == 46 || keyID == 8 || keyID == 109
				|| keyID == 189 || keyID == 9
				|| keyID == 37 || keyID == 39){

		if(strVal.length > 1 && (keyID == 109 || keyID == 189)){
			return false;
		}else{
			return;
		}
	}else{
		return false;
	}
});

$(document).on("keyup", "input:text[numberOnlyMinComma]", function()	{
	$(this).val( $(this).val().replace(/[^-\.0-9]/gi,"") );
	$(this).val( $(this).val().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") );
});

$(document).on("focusout", "input:text[koreanCurrency]", function()	{
	$(this).val( $(this).val().replace(",","") );
	$(this).val( $(this).val().replace(/[^-\.0-9]/gi,"") );
	$(this).val( $(this).val().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") );
	if($(this).val() != '' ) {
		$(this).val( $(this).val()+' 천원');
	}		
});

$(document).on("focus", "input:text[koreanCurrency]", function()	{	
	$(this).val( $(this).val().replace("원", ""));
});
</script>



<style scoped>
#product {
  margin-top: 50px;
  margin-left: 100px;
  margin-right: 100px;
  padding-top: 10px;
  border-top: 3px solid #9ac486;
}
#product > div {
  box-sizing:border-box;
  -moz-box-sizing:border-box;
}
#left {
  padding-top: 10px;
  padding-right:20px;
  float:left;
  width: 50%;
}
#right {
  float:right;
  width: 50%;
}
#rightTitle {
  border-bottom: 1px solid #9ac486;
  margin-bottom:25px;
}
#bottom {
  padding-top: 25px;
  border-top: 3px solid #9ac486;
  clear:both;
}
#title {
  font-weight: 700;
  font-size: 35px;
  line-height: 20px;
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
#detail {
  font-weight: 450;
  font-size: 20px;
  margin : 30px;
}
.w-100 {
  padding: 20px;
}
#button-text {
  font-size:20px; 
  font-weight:700;
}
.buttons {
  display: flex;
}
.btn {
  margin-left: 3px;
  margin-right: 3px;
}

.btn-outline-success {
    --bs-btn-color: #9ac486;
    --bs-btn-border-color: #9ac486;
}
.btn-outline-success:hover {
  background: #9ac486;
  border: none;
}



.file-label {
  margin-top: 30px;
  background-color: #9ac486;
  color: #fff;
  text-align: center;
  padding: 10px 0;
  width: 65%;
  border-radius: 6px;
  cursor: pointer;
}
.file {
  display: none;
}

#profile-img {
  width: 100%;
  height: 100%;
  background-image:url('');
  background-size: 100% 360px;
  /* margin-top: -70px; */
  background-position: center center;
  border: 7px solid white;
}


.upload-box {
  width: 100%;
  box-sizing: border-box;
  margin-right: 30px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.upload-box .drag-file {
  position: relative;
  width: 100%;
  height: 360px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border: 3px dashed #dbdbdb;
}
</style>
