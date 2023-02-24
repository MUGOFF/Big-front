<template>
  <div class="home">
    <div id="carousel" class="content">
      <Carousel/>
    </div>
    
    <br>
    <div class="container text-center">
      <div class="row">
        <div class="col">
          <h3>오늘의 농산물 가격</h3>
          <p class="lead text-muted">서울지역 최근 30일 동향</p>
          <!-- <p class="lead text-muted">AI모델이 예측한 날짜별 농산물 가격을 확인하세요.</p> -->
        </div>
        <!-- <div class="col">
          <select class="form-select" aria-label="Default select example">
            <option selected>정렬: 인기순</option>
            <option value="1">정렬: 높은 가격순</option>
            <option value="2">정렬: 낮은 가격순</option>
            <option value="3">정렬: 인기순</option>
          </select>
        </div> -->
      </div>
    </div>
    <div id="card" class="content">
      <Card/>
    </div>
  </div>



</template>


<script>
// @ is an alias to /src
import Carousel from '@/components/Carousel.vue'
import Card from '@/components/Card.vue'

export default {
  name: 'HomeView',
  components: {
    Carousel,Card
  }
}
</script>

<style scoped>
#card {
  margin: 30px 50px;
}
</style>

