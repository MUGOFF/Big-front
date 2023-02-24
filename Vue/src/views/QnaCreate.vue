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
            <button @click="write">작성</button>
            
        </div>
    </section>
</template>

<script>
import axios from 'axios';
import data from '@/data'

export default {
    name: 'QnaCreate',
    data() {
        // const contentId = Number(data.Question[0].content_id) + 1;
        return {
            // contentId: contentId,
            // items: data.Question[contentId], 
            // idx: this.$route.query.idx,
            user_name: "",
            title: "",
            // created_at: "",
            context: "",


        }
    },
    mounted(){
        this.get_userRealname()
    },

    methods: {
        get_userRealname() {
            axios
            .get('user/'+ this.$store.state.token)
            .then(response => {
                this.user_name = response.data.username;
                this.user_email = response.data.email;
                // this.user_name =this.user_name.substring(0, 1)+'*'+this.user_name.substring(2)
            })
            .catch(error => {
                console.log(error);
            })
        },
        write() {
            axios.post('api/v1/qnas_detail/', {
                title:this.title,
                content:this.context,
                writer:this.user_name,
                writer_email:this.user_email,
            })
            .then(response => {
                this.$router.push({
                    path: '/qna/detail/' + response.data.id
                })
            })
            .catch(error => {
                console.log(error);
            })
            // const today = new Date();
            // const today_form = today.getFullYear() + '-' + ('0' + (today.getMonth() + 1)).slice(-2) + '-' + ('0' + today.getDate()).slice(-2);
            // const contentId = Number(data.Question[0].content_id) + 1;
            // data.Question.push({
            //     content_id: contentId,
            //     user_name: this.user_name,
            //     title: this.title,
            //     context: this.context.split('\n').join('<br>'),
            //     created_at: today_form,
            //     updated_at: null,
            //     answered: null,
            // })
            // let items = data.Question.slice().sort((a,b) => {return b.content_id - a.content_id})
        },
    }
}
</script>