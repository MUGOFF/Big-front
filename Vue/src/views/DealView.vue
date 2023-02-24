<template>

  <div id="deal">
    <div class="item sell" style="cursor: pointer;" @click="redirectToSell">
      <div class="img">
        <img class="img-fluid" :src="require('@/assets/deal1.png')"/>
      </div>
      <div class="text">
        판매하기
      </div>
    </div>
    <div class="item buy" style="cursor: pointer;" @click="redirectToBuy">
      <div class="img">
        <img class="img-fluid" :src="require('@/assets/deal2.png')"/>
      </div>
      <div class="text">
        구매하기
      </div>
    </div>
  </div>
  <br><br><br><br>
</template>
<script>
export default {
  name: 'Deal',
  methods: {
    redirectToSell () {
      this.$router.push(
          {
            path: '/productcreate',
          }
        )
      },
    redirectToBuy () {
      this.$router.push(
          {
            path: '/searchdetail',
          }
        )
      }
  },
};
</script>
<style scoped>
.img{
  width: 100%;
}

#deal {
  display: flex;
}
.item {
	width: 100%;
  height: 100%;
  margin-bottom: 20px;
  margin: 30px;
  padding: 50px;
  border-top-left-radius: 24px;
  border-top-right-radius: 24px;
  border-bottom-left-radius: 24px;
  border-bottom-right-radius: 24px;
  font-size: 40px;
  font-weight: 700;
  overflow: hidden;
}
.buy {
  margin-right: 100px;
  border: 5px solid #d8e37b;
  flex: 1;
}
.sell{
  margin-left: 100px;
  border: 5px solid #9ac486;
  flex: 1;
}
.text {
  margin-top: 20px;
}
</style>