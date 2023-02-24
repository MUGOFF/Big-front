<template>
  <div id="searchresult">
		<div class="title">
			<div class="title-left">
				<h3>검색 결과</h3>
				<p class="lead text-muted">
					조건 - 지역: {{$route.query.region}} / 상세 지역: {{$route.query.subregion}} / 품목: {{$route.query.category}} / 규모: {{$route.query.scale}} 
					<button type="button" @click="$router.push('/searchdetail')" class="btn btn-light btn-sm">조건 수정</button>
				</p>
			</div>
			<div class="sort">
				<select class="form-select" aria-label="Default select example">
					<option selected>정렬: 인기순</option>
					<option value="1">정렬: 높은 가격순</option>
					<option value="2">정렬: 낮은 가격순</option>
					<option value="3">정렬: 최신순</option>
				</select>
			</div>
		</div>
		<!-- <div class="d-flex"> -->

			<div class="row row-cols-1 row-cols-md-4 g-4" >
				<div class="col" v-for="aritcle in article_list" :key="aritcle">
					<div class="item" @click="detail(aritcle.id)">
						<div style="height:50%">
							<img :src="aritcle.profile" style="height:100%"/>
						</div>
						<div class="itemdetail">
							<div class="top">
								<span style="font-size:25px;">{{aritcle.title}}<br></span>
								<span style="font-size:15px; color:gray;">{{aritcle.region_kor + aritcle.sub_region}}</span>
							</div>
							<table class="table table-borderless">
								<tr>
									<td style="width: 50%" align="left">거래 가격</td>
									<td align="right">{{aritcle.price}} 천원</td>
								</tr>
							</table>
							<button @click="detail(aritcle.id)" class="btn btn-success w-100">상세보기</button>
						</div>
					</div>
				</div>
			</div>
		<!-- </div> -->
			<!--<div class="col">
				<div class="item">
					<router-link to="/product"><div class="itempic"/></router-link>
					<div class="itemdetail">
						<div class="top">
							<span style="font-size:25px;">{{itemtitle}}<br></span>
							<span style="font-size:15px; color:gray;">{{address}}</span>
						</div>
						<table class="table table-borderless">
							<tr>
								<td style="width: 50%" align="left">거래 가격</td>
								<td align="right">{{price}}</td>
							</tr>
						</table>
						<button @click="$router.push('/product')" class="btn btn-success w-100">상세보기</button>
					</div>
				</div>
			</div>
			<div class="col">
				<div class="item">
					<router-link to="/product"><div class="itempic"/></router-link>
					<div class="itemdetail">
						<div class="top">
							<span style="font-size:25px;">{{itemtitle}}<br></span>
							<span style="font-size:15px; color:gray;">{{address}}</span>
						</div>
						<table class="table table-borderless">
							<tr>
								<td style="width: 50%" align="left">거래 가격</td>
								<td align="right">{{price}}</td>
							</tr>
						</table>
						<button @click="$router.push('/product')" class="btn btn-success w-100">상세보기</button>
					</div>
				</div>
			</div>
			 <div class="col">
				<div class="item">
					<router-link to="/product"><div class="itempic"/></router-link>
					<div class="itemdetail">
						<div class="top">
							<span style="font-size:25px;">{{itemtitle}}<br></span>
							<span style="font-size:15px; color:gray;">{{address}}</span>
						</div>
						<table class="table table-borderless">
							<tr>
								<td style="width: 50%" align="left">거래 가격</td>
								<td align="right">{{price}}</td>
							</tr>
						</table>
						<button @click="$router.push('/product')" class="btn btn-success w-100">상세보기</button>
					</div>
				</div>
			</div> -->
	</div>
</template>
<script>
import axios from 'axios';

export default {
  name: 'SearchdetailResult',
  data() {
    return {
			'status': '판매중',
			'itemtitle': '상추팝니다',
			'address': '상세 주소',
			'price': '100,000원',
			article_list : [],
		}
	},
	mounted() {
		this.get_article_list()
	},
	methods: {
		get_article_list() {
			var region_kor= ['서울','부산','대구','광주','대전']
            var region= ['seoul','pusan','daegu','gwanju','daejun']
			var items = ["carrot","radish","pear","napacabbage","lettuce","watermelon","spinach","cabbage","cucumber","tomato",'pepper'] //당근, 무, 배, 배추, 상추, 수박, 시금치, 양배추, 오이, 토마토, 풋고추
      		var items_kor = ["당근","무","배","배추","상추","수박","시금치","양배추","오이","토마토",'풋고추']
			if (this.$route.query.region===undefined||this.$route.query.region==='') {
				var region_Pick = ''
			} else {
				var region_Pick = region[region_kor.indexOf(this.$route.query.region)]
			}
			if (this.$route.query.subregion===undefined||this.$route.query.subregion==='') {
				var subregion_Pick = ''
			} else {
				var subregion_Pick = this.$route.query.subregion
			}
			if (this.$route.query.category===undefined||this.$route.query.category==='') {
				var item_Pick = ''
			} else {
				var item_Pick = items[items_kor.indexOf(this.$route.query.category)]
			}
			if (this.$route.query.scale===undefined||this.$route.query.scale==='') {
				var price_Pick = 0
			} else {
				var price_Pick = this.$route.query.scale
			}
			axios.get('api/v1/article_list/?region='+region_Pick+'&sub_region='+subregion_Pick+'&item='+item_Pick+'&price='+Number(price_Pick))
			.then(response => {
				for (var step=0;step<response.data.length;step++) {
					this.article_list[step] = response.data[step]
					this.article_list[step].region_kor = region_kor[region.indexOf(response.data[step].region)]
				}
				console.log(this.article_list)
			})
			.catch(error => {
				console.log(error)
			})
		},
		detail(content_id) {
            this.$router.push({
                name: 'product', 
                params: {
                    contentId: content_id
                }
            })
        },
	},
}
</script>
<style scoped>
#searchresult {
	padding-top: 50px;
	padding-bottom: 50px;
	padding-left: 100px;
	padding-right: 100px;
}
.title {
	display: flex;
	margin-bottom: 20px;
}
.title-left {
	flex:8;
	text-align: left;
}
.sort {
	flex: 2;
}
.item {
	width: 100%;
  height: 400px;
  margin-bottom: 20px;
  border-top-left-radius: 24px;
  border-top-right-radius: 24px;
  border-bottom-left-radius: 24px;
  border-bottom-right-radius: 24px;
  box-shadow: 0px 4px 40px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}
.itempic {
  width: 100%;
  height: 220px;
  background-image:url('@/assets/product/lettuce.png');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center center;
  overflow: hidden;
	margin-bottom: 10px;
}
.itemdetail {
	padding-left: 20px;
	padding-right: 20px;
}
.top {
	margin-bottom: 10px;
}
</style>
