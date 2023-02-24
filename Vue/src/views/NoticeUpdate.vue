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
            <button @click="update">수정</button>
        </div>
    </section>
</template>

<script>
import data from '@/data'

export default {
    name: 'NoticeUpdate',
    data() {
        const contentId = Number(this.$route.params.contentId);
        const realId = Number(data.Content.map((x, index) => {if (x.content_id == contentId) {return index}}).filter(e => e)[0]);
        const contentData = data.Content.filter(item => item.content_id === contentId)[0];
        return {
            contentId: contentId,
            items: contentData,
            rId: realId,
            idx: this.$route.query.idx,
            user_name: contentData.user_name,
            title: contentData.title,
            created_at: contentData.created_at,
            updated_at: contentData.updated_at,
            context: contentData.context.split('<br>').join('\n'),


        }
    },

    methods: {
        update() {
            const contentId = Number(this.$route.params.contentId);
            const today = new Date();
            const today_form = today.getFullYear() + '-' + ('0' + (today.getMonth() + 1)).slice(-2) + '-' + ('0' + today.getDate()).slice(-2);
            data.Content[this.rId].user_name = this.user_name
            data.Content[this.rId].title = this.title
            data.Content[this.rId].updated_at = today_form
            data.Content[this.rId].context = this.context.split('\n').join('<br>')
            this.$router.push({
                path: '/notice/detail/' + contentId
            })
            
        }
    }
}
</script>