<template>
    <!-- FOOTER -->
    <footer>
    <div class="inner">
        <ul class="menu">
        <router-link class="btn btn--white" aria-current="page" to="/about">소개</router-link>
        <router-link class="btn btn--white" aria-current="page" to="/searchdetail">포전거래</router-link>
        <router-link class="btn btn--white" aria-current="page" to="/price">농산물 가격</router-link>
        <router-link class="btn btn--white" aria-current="page" to="/noticet">게시판</router-link>
        <router-link class="btn btn--white" aria-current="page" to="">이용약관</router-link>
        </ul>
        
        <div class="info">
        <span>사업자등록번호 123-45-678910</span>
        <span>(주)팜팜 코리아</span>
        <span>TEL : 053) 1234-1234 / FAX : 053) 1234-1234</span>
        <span>개인정보 책임자 : 에이블러</span>
        </div>

        <p class="copyright">
        &copy; <span class="this-year"></span> 2022 FarmFarm Company. All Rights Reseved.
        </p>
        <!-- <img :src="require('@/assets/logo1.png')" alt="" class="logo" /> -->
    </div>
    </footer>
</template>

<script>

</script>>


<style>
    footer {
    margin-top: 100px;
    background-color: #9ac486;
    }
    footer .inner {
    padding: 40px 0 60px 0
    }
    footer .menu {
    display: flex;
    justify-content: center;
    }
    footer .menu li {
    position: relative;
    }
    footer .menu li::before {
    content: "";
    width: 3px;
    height: 3px;
    background-color: #555;
    position: absolute;
    top: 0;
    bottom: 0;
    right: -1px;
    margin: auto;
    }
    footer .menu li:last-child::before {
    display: none;
    }
    footer .menu li a {
    color: #ccc;
    font-size: 12px;
    font-weight: 700;
    padding: 15px;
    display: block;
    }
    footer .menu li a.green {
    color: #669900
    }
    footer .btn-group {
    margin-top: 20px;
    display: flex;
    justify-content: center;
    }
    footer .btn-group .btn {
    font-size: 12px;
    margin-right: 10px;
    }
    footer .btn-group .btn:last-child {
    margin-right: 0px;
    }
    footer .info {
    margin-top: 30px;
    text-align: center;
    }
    footer .info span {
    margin-right: 20px;
    color: #ffffff;
    font-size: 12px;
    }
    footer .info span:last-child {
    margin-right: 0;
    }
    footer .copyright {
    color: #ffffff;
    font-size: 12px;
    text-align: center;
    margin-top: 12px;
    }
    footer .logo {
    margin: 30px auto 0;
    }

</style>