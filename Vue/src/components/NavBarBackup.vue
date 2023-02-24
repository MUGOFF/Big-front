<template>
<!--네비바-->
  <nav class="navbar navbar-expand-lg">
    <div class="container-fluid">
      <!-- <router-link class="navbar-brand" to="/">로고는아직</router-link> -->
      <router-link class="navbar-brand" to="/"><img :src="require('@/assets/logo2.png')" class="head-log"></router-link>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarScroll" aria-controls="navbarScroll" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarScroll">
        <ul class="navbar-nav me-auto my-2 my-lg-0 navbar-nav-scroll" style="--bs-scroll-height: 100px;">
          <li class="nav-item">
            <router-link class="nav-link" aria-current="page" to="/about">소개</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" aria-current="page" to="/deal">포전거래</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" aria-current="page" to="/price">농산물 가격</router-link>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="/notice" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              게시판
            </a>
            <ul class="dropdown-menu">
              <li><router-link class="nav-link" aria-current="page" to="/notice">공지사항</router-link></li>
              <li><router-link class="nav-link" aria-current="page" to="/guide">이용 가이드</router-link></li>
              <li><router-link class="nav-link" aria-current="page" to="/qna">문의게시판</router-link></li>
            </ul>
          </li>
        </ul>
        <button class="btn btn-outline position-relative">
          <i class="fa-solid fa-bell"></i>
          <span class="position-absolute top-0 start-100 translate-middle p-2 bg-danger border border-light rounded-circle">
            <span class="visually-hidden">New alerts</span>
          </span>
        </button>

        <!-- 마이페이지 -->
        <button class="btn btn-outline" type="submit">
          <router-link class="fa-solid fa-user" to="/reconfirm"></router-link>
        </button>
        <router-link class="navbar-brand" to="/login"><button class="btn btn-outline-success" type="submit">로그인</button></router-link>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'navBar',
};
</script>

<style scoped>
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a{
  color: #000000;
}
.navbar {
  padding: 20px;
}
.head-log{
  width: 120px;
}

.btn-outline-success {
    --bs-btn-color: #9ac486;
    --bs-btn-border-color: #9ac486;
}
.btn-outline-success:hover {
  background: #9ac486;
  border: none;
}

.fa-solid{
  color: black;
}

.btn {
  font-size: 1.2rem;
}

.nav-item {
  font-size: 1.2rem;
}

img, svg {
    vertical-align: baseline;
}

</style>
  