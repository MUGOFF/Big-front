<template>
    <section>
        <div class="container text-center my-5">
            <div class="row my-1">
                <textarea cols="60" rows="1" v-model="title" placeholder="제목"/>
            </div>
            <div class="row my-1">
                <textarea cols=40 rows=1 v-model="user_name" placeholder="작성자" readonly/>
            </div>
            <div class="row my-3">
                <textarea cols="60" rows="10" v-model="context" placeholder="내용"/>
            </div>
            <button @click="update">수정</button>
            <!-- <button>{{idx}}</button> -->
        </div>
    </section>
</template>

<script>
// import data from '@/data'
import axios from 'axios'

export default {
    name: 'QnaUpdate',
    data() {
        // const contentId = Number(this.$route.params.contentId);
        // const realId = Number(data.Question.map((x, index) => {if (x.content_id == contentId) {return index}}).filter(e => e)[0]);
        // const contentData = data.Question.filter(item => item.content_id === contentId)[0];
        return {
            // contentId: contentId,
            // items: contentData, 
            // rId: realId,
            // idx: this.$route.query.idx,
            user_name: "",//contentData.user_name,
            title: "",//contentData.title,
            // created_at: contentData.created_at,
            // updated_at: contentData.updated_at,
            context:"",// contentData.context.split('<br>').join('\n'),


        }
    },
    mounted(){
        this.get_Question()
    },
    methods: {
        get_Question() {
            axios.get('api/v1/qnas_detail/?id='+Number(this.$route.params.contentId))
            .then(response =>{
                // console.log(response.data)
                this.user_name = response.data[0].writer
                this.title = response.data[0].title
                this.context = response.data[0].content
            })
            .catch(error =>{
                console.error(error)
            })
        },
        update() {
            // const contentId = Number(this.$route.params.contentId);
            // const today = new Date();
            // const today_form = today.getFullYear() + '-' + ('0' + (today.getMonth() + 1)).slice(-2) + '-' + ('0' + today.getDate()).slice(-2);
            // data.Question[this.rId].user_name = this.user_name
            // data.Question[this.rId].title = this.title
            // data.Question[this.rId].updated_at = today_form
            // data.Question[this.rId].context = this.context.split('\n').join('<br>')
            axios.put('api/v1/qnas_detail/?id='+Number(this.$route.params.contentId),{
                title:this.title,
                content:this.context,
                writer:this.user_name,
            })
            .then(response =>{
                // console.log(response)
                const contentId = Number(this.$route.params.contentId);
                this.$router.push({
                    path: '/qna/detail/'+ Number(this.$route.params.contentId),
                    params: {
                        contentId: contentId
                    }
                })
            })
            .catch(error =>{
                console.log(error)
            })
            
        }
    }
}
</script>