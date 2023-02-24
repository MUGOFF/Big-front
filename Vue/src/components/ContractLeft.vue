<template>
    <div class='col-sm-12'>
        <form class="row g-3">
            <label>소재지</label>
            <button type="button" class="btn btn-light btn-sm" @click="showApi">주소 찾기</button>
            <div class="col-6">
                <input class="form-control" readonly v-model="region" placeholder="우편번호" @change="inputName($event)">
            </div>
            <div class="col-6">
                <input class="form-control" v-model="sub_region" placeholder="기본주소" @change="inputName($event)">
            </div>
            <div class="col-12">
                <input class="form-control" v-model="town" placeholder="상세주소 입력" @change="inputName($event)">
            </div>

            <label>품목</label>
            <div class="col-5">
                <select class="form-select" v-model="category" @change="inputName($event)">
                    <option selected>상추</option>
                    <option>...</option>
                </select>
            </div>
            <div class="col-7">
                <select class="form-select" v-model="item" @change="inputName($event)">
                    <option selected>적상추</option>
                    <option>...</option>
                </select>
            </div>
            <div class="col-md-5">
                <label>계약면적</label>
                <input type="text" @change="inputName($event)" v-model="area" class="form-control" id="rcvordAm" name="rcvordAm" numberOnlyMinComma="true" koreanCurrency="true" required="required" placeholder="입력단위: m2">
            </div>
            <div class="col-md-7">
                <label>지급일</label>
                <input type="date" @change="inputName($event)" v-model="p_date" class="form-control">
            </div>
        </form>
    </div>
</template>

<script>
// @ is an alias to /src
import $ from 'jquery';

export default {
    name: 'contractLeft',
    data(){
        return {
            region : "",
            sub_region : "",
            town : "",
            category : "",
            item : "",
            area : "",
            p_date : "",
        }
    },
    methods: {
        inputName(event) {
            let b_data = {
                region : this.region,
                sub_region : this.sub_region,
                town : this.town,
                category : this.category,
                item : this.item,
                area : this.area,
                p_date : this.p_date,
            }
            this.$emit('input_data',b_data)
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
                this.region = data.zonecode; //5자리 새우편번호 사용
                this.sub_region = fullRoadAddr;
            }
            }).open()
        },
    }
};

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