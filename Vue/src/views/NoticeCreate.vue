<template>
    <section>
        <div class="container text-center my-5">
            <div class="row my-1">
                <textarea cols="60" rows="1" v-model="title" placeholder="제목"/>
            </div>
            <div class="row my-1">
                <textarea cols=40 rows=1 v-model="user_name" placeholder="작성자"/>
            </div>
            <div class="row my-3">
                <textarea cols="60" rows="10" v-model="context" placeholder="내용"/>
            </div>
            <button @click="write">작성</button>
            
        </div>
    </section>
</template>

<script>
import data from '@/data'

export default {
    name: 'NoticeCreate',
    data() {
        const contentId = Number(data.Content[0].content_id) + 1;
        return {
            contentId: contentId,
            idx: this.$route.query.idx,
            user_name: "",
            title: "",
            context: "",
        }
    },

    methods: {
        write() {
            const today = new Date();
            const today_form = today.getFullYear() + '-' + ('0' + (today.getMonth() + 1)).slice(-2) + '-' + ('0' + today.getDate()).slice(-2);
            const contentId = Number(data.Content[0].content_id) + 1;
            data.Content.push({
                content_id: contentId,
                user_name: this.user_name,
                title: this.title,
                context: this.context.split('\n').join('<br>'),
                created_at: today_form,
                updated_at: null,
            })
            let items = data.Content.slice().sort((a,b) => {return b.content_id - a.content_id})
            this.$router.push({
                path: '/notice/detail/' + this.contentId
            })
        },
    }
}
</script>