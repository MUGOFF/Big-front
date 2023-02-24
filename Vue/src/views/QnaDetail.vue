<template>
    <div class="container my-5">
        <div class="pb-5">
            <div style="float: left;" class="col">글 번호: {{ items.id }}</div>
            <button style="float: right;" @click="deleteData">삭제</button>
            <button style="float: right;" v-if="sameuser" @click="updateData">수정</button>
        </div>
        <div class="row my-1">
            <div class="container text-center">
                
                <div style="float: center;" class="col"><h2>{{ items.title }}</h2></div>
                
                <!-- <div style="float: right;" class="m-2">{{ items.updated_at !== null  ? items.updated_at : '수정 없음'}}</div> -->
                <div style="float: right;" class="m-2">수정일: {{ items.recent_updated }}</div>
                <div style="float: right;" class="m-2">작성일: {{ items.written_date }}</div>
                <div style="float: right;" class="m-2">작성자: {{ items.writer }}</div>
                
                
            </div>

            <div class="container-fluid text-center border py-5">
                <div>{{items.content  }}</div>
            </div>

            <div class="content-detail-comment" v-show="comment_exist">
                <!-- <QnaAnswer :contentId="contentId"/> -->
                <div>
                    <div class= "comment-list-item">
                        <div class="comment-list-item-name">
                            <div>{{comment.author}}</div>
                            <!-- <div>{{commentObj.created_at}}</div> -->
                        </div>
                        <div class="comment-list-item-context">{{comment.message}}</div>
                        <div class="comment-list-item-button">
                            <div>작성 일자: {{comment.created}}</div>
                            <div>최종 일자: {{comment.updated}}</div>
                            <!-- <button @click="deleteData">삭제</button> -->
                        </div>
                    </div>
                </div>
            </div>
            
        </div>
        <button @click="toList" class="mt-5">목록</button>
    </div>
</template>

<script>
import axios from 'axios';
// import data from '@/data';
// import QnaAnswer from './QnaAnswer';
export default {
    name: 'QnaDetail', 
    components: {
        // QnaAnswer,
    },
    data() {
        // const contentId = Number(this.$route.params.contentId);
        // const realId = Number(data.Question.map((x, index) => {if (x.content_id == contentId) {return index}}).filter(e => e)[0]);
        // const contentData = data.Question.filter(item => item.content_id === contentId)[0];
        return {
            items: {},//contentData,
            // contentId: contentId,
            // title: contentData.title,
            // rId: realId,
            comment: {},
            comment_exist : false,
            sameuser: false,
        }
    },
    mounted(){
        this.get_Question()
        this.get_answer()
        this.get_user_info()
    },
    methods: {
        get_user_info() {
            axios
            .get('user/'+ this.$store.state.token)
            .then(response => {
                this.user_email = response.data.email;
                if(this.user_email === this.items.writer_email) {
                    this.sameuser=true
                }
            })
            .catch(error => {
                console.log(error);
            })
        },
        get_answer() {
            axios.get('api/v1/answer_comment/?id='+Number(this.$route.params.contentId))
            .then(response => {
                // console.log(response)
                if (response.data.length >0) {
                    this.comment=response.data[0]
                    this.comment_exist=true
                }
            })
            .catch(error => {
                console.error(error)
            })
        },
        get_Question() {
            // console.log('detail', this.$route.params.contentId)
            axios.get('api/v1/qnas_detail/?id='+Number(this.$route.params.contentId))
            .then(response =>{
                // console.log(response.data)
                this.items = response.data[0]
                this.items.writer = this.items.writer.substring(0,1)+'*'+this.items.writer.substring(2)
            })
            .catch(error =>{
                console.error(error)
            })
        },
        toList() {
            this.$router.push({
                path: '/qna'
            })
        },
        deleteData() {
            // data.Question.splice(this.rId, 1)
            axios
            .delete('api/v1/qnas_detail/?id='+Number(this.$route.params.contentId))
            .then(response =>{
                console.log(response)
                this.$router.push({
                    path: '/qna'
                })
            })
            .catch(error =>{
                console.error(error)
            })
        },
        updateData() {
            var contentId = Number(this.$route.params.contentId)
            this.$router.push({
                name: 'QnaUpdate',
                params: {
                    contentId: contentId//this.contentId
                }
            })
        }

    }

}
</script>

<style scoped>
.content-detail-comment {
  border: 1px solid #D1E7DD; /* #9AC486 */
  /* border: 1px solid black; */
  margin-top: 1rem;
  padding: 2rem;
}
.comment-list-item {
  display: flex;
  justify-content: space-between;
  padding-bottom: 1em;
}
.comment-list-item-name {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 10%;
  border: 0.5px solid #D1E7DD;
  padding: 1em;
  background-color: #D1E7DD;
}
.comment-list-item-context {
  display: flex;
  justify-content: left;
  align-items: center;
  padding: 1.5em;
  width: 65%;
  border: 3px solid #D1E7DD;
}
.comment-list-item-button {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 25%;
  border: 3px solid #D1E7DD;
  padding: 1em;
  background-color: #D1E7DD;
}
</style>