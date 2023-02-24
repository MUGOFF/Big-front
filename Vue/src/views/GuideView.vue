<template>
  <div class="about">
    <div class="title"><span style="font-weight:bold; font-size:2em;">서비스 이용 가이드</span></div>
    <img :src="require('@/assets/guide1.png')" class="img-fluid" >

    <section>
      <div class="container my-5">
        <div class="row p-4 pb-0 pe-lg-0 pt-lg-5 align-items-center rounded-3 border shadow-lg">
          <div class="row">
            <div class="col-sm-3 display-7 fw-bold lh-1 mb-3">
              <img :src="require('@/assets/signin.png')" class="img-fluid" >
            </div>
            <div class="col-sm-9">
              <h1 class="display-7 fw-bold lh-1 mb-3">STEP 1. 회원가입 </h1>
              <br>
              <p class="lead">회원가입을 합니다.</p>
              <p class="lead">*는 필수 기입 정보 입니다.</p>
              <p class="lead">선호 품종과 선호 지역을 선택하지 않으면</p>
              <p class="lead">없음으로 자동 선택 됩니다.</p>
            </div>
          </div>
        </div>
      </div>
    </section>


    <section>
      <div class="container my-5">
        <div class="row p-4 pb-0 pe-lg-0 pt-lg-5 align-items-center rounded-3 border shadow-lg">
          <div class="row">
            <div class="col-sm-3 display-7 fw-bold lh-1 mb-3">
              <img :src="require('@/assets/login.png')" class="img-fluid" >
            </div>
            <div class="col-sm-9">
              <h1 class="display-7 fw-bold lh-1 mb-3">STEP 2. 로그인 </h1>
              <br>
              <p class="lead">로그인을 합니다.</p>
              <p class="lead">아이디에는 이메일을 입력합니다.</p>
              <p class="lead">비밀번호는 특수기호, 문자, 숫자가 포함되어있습니다.</p>
              <p class="lead">아이디 또는 비밀번호를 잊어버렸을 경우</p>
              <p class="lead">찾기를 이용하면 됩니다.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section>
      <div class="container my-5">
        <div class="row p-4 pb-0 pe-lg-0 pt-lg-5 align-items-center rounded-3 border shadow-lg">
          <div class="row">
            <div class="col-sm-3 display-7 fw-bold lh-1 mb-3">
              <img :src="require('@/assets/search.png')" class="img-fluid" >
            </div>
            <div class="col-sm-9">
              <h1 class="display-7 fw-bold lh-1 mb-3">STEP 3. 조건에 맞게 검색 </h1>
              <br>
              <p class="lead">포전거래 메뉴에서 구매하기를 들어갑니다.</p>
              <p class="lead">지역, 상세지역, 품목, 규모를 선택합니다.</p>
              <p class="lead">원하는 글의 상세보기에 들어갑니다.</p>
              <p class="lead">판매내용을 확인합니다.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section>
      <div class="container my-5">
        <div class="row p-4 pb-0 pe-lg-0 pt-lg-5 align-items-center rounded-3 border shadow-lg">
          <div class="row">
            <div class="col-sm-3 display-7 fw-bold lh-1 mb-3">
              <img :src="require('@/assets/profile.png')" class="img-fluid" >
            </div>
            <div class="col-sm-9">
              <h1 class="display-7 fw-bold lh-1 mb-3">STEP 4. 프로필 확인 </h1>
              <br>
              <p class="lead">이전 판매내용에서 판매자의 프로필보기를 클릭합니다.</p>
              <p class="lead">재배작물, 지역, 재거래희망률, 최근거래목록 등</p>
              <p class="lead">판매자의 정보를 확인하실 수 있습니다.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section>
      <div class="container my-5">
        <div class="row p-4 pb-0 pe-lg-0 pt-lg-5 align-items-center rounded-3 border shadow-lg">
          <div class="row">
            <div class="col-sm-3 display-7 fw-bold lh-1 mb-3">
              <img :src="require('@/assets/paper.png')" class="img-fluid" >
            </div>
            <div class="col-sm-9">
              <h1 class="display-7 fw-bold lh-1 mb-3">STEP 5. 계약서 작성 </h1>
              <br>
              <p class="lead">판매내용 페이지나 판매자 프로필에서 계약서 작성을 클릭합니다.</p>
              <p class="lead">계약서 작성페이지가 나타납니다.</p>
              <p class="lead">양식에 맞게 계약서를 작성합니다.</p>
              <p class="lead">작성을 완료한 후 계약진행을 클릭합니다.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section>
      <div class="container my-5">
        <div class="row p-4 pb-0 pe-lg-0 pt-lg-5 align-items-center rounded-3 border shadow-lg">
          <div class="row">
            <div class="col-sm-3 display-7 fw-bold lh-1 mb-3">
              <img :src="require('@/assets/deal.png')" class="img-fluid" >
            </div>
            <div class="col-sm-9">
              <h1 class="display-7 fw-bold lh-1 mb-3">STEP 6. 거래 완료 </h1>
              <br>
              <p class="lead">거래가 완료되었습니다.</p>
              <p class="lead"></p>
              <p class="lead"></p>
              <p class="lead"></p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'GuideView',
  components: {}
}
</script>
  