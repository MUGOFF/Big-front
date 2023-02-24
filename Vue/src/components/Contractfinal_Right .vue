<template>
    <div class='col-sm-6'>
      <form class="row g-4">
        <p></p>
        <div class="col-md-5">
          <label >총 매매대금</label>
          <input type="text" class="form-control" readonly v-model="p_value" id="rcvordAm" name="rcvordAm" numberOnlyMinComma="true" koreanCurrency="true" required="required" placeholder="입력단위: 천원">
        </div>
        <div class="col-md-7">
            <label>지급일</label>
            <input type="date" readonly v-model="p_date" class="form-control">
        </div>
        <div class="col-md-5">
          <label>계약금</label>
          <input type="text" class="form-control" readonly v-model="a_value" id="rcvordAm" name="rcvordAm" numberOnlyMinComma="true" koreanCurrency="true" required="required" placeholder="입력단위: 천원">
        </div>
        <div class="col-md-7">
          <label>지급일</label>
          <input type="date" class="form-control" readonly v-model="a_date">
        </div>

        <div class="col-md-5">
          <label>중도금</label>
          <input type="text" class="form-control" readonly v-model="i_value" id="rcvordAm" name="rcvordAm" numberOnlyMinComma="true" koreanCurrency="true" required="required" placeholder="입력단위: 천원">
        </div>
        <div class="col-md-7">
          <label>지급일</label>
          <input type="date" class="form-control" readonly v-model="i_date">
        </div>

        <div class="col-md-5">
          <label>잔금</label>
          <input type="text" class="form-control" readonly v-model="b_value" id="rcvordAm" name="rcvordAm" numberOnlyMinComma="true" koreanCurrency="true" required="required" placeholder="입력단위: 천원">
        </div>
        <div class="col-md-7">
          <label>지급일</label>
          <input type="date" class="form-control" readonly v-model="b_date">
        </div>

        <div class="col-12">
          <label>반출일</label>
          <input type="date" class="form-control" readonly v-model="g_date">
        </div>

        <div class="col-12">
          <label>특약사항</label>
          <textarea class="form-control" readonly v-model="special" rows="10"></textarea>
        </div>
      </form> 
    </div>
</template>

<script>
// @ is an alias to /src
import $ from 'jquery';

export default {
    name: 'finalcontractMaemae',
    props: {
      p_value : {type:Number},
      p_date : {type: String},
      a_value : {type:Number},
      a_date : {type:String},
      i_value : {type:Number},
      i_date : {type:String},
      b_value : {type:Number},
      b_date : {type:String},
      g_date : {type:String},
      special : {type:String},
    },
    data() {
      return {
        p_value : this.p_value,
        p_date : this.p_date,
        a_value : this.a_value,
        a_date : this.a_date,
        i_value : this.i_value,
        i_date : this.i_date,
        b_value : this.b_value,
        b_date : this.b_date,
        g_date : this.g_date,
        special : this.special,
      }
    },
    methods: {
      // inputData(event) {
      //   let right_data = { 
      //     'p_value' : this.p_value,
      //     'a_value' : this.a_value,
      //     'a_date' : this.a_date,
      //     'i_value' : this.i_value,
      //     'i_date' : this.i_date,
      //     'b_value' : this.b_value,
      //     'b_date' : this.b_date,
      //     'g_date' : this.g_date,
      //     'special' : this.special,
      //   }
      //   this.$emit('input_data',right_data)
      // }
     },
};

// 가격 적으면 알아서 콤마랑 글자 적어주는 제이쿼리문
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