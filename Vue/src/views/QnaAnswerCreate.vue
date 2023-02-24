<template>
    <div>
        <div class="input-group mb-3">
            <span class="input-group-text">{{name}}</span>
            <textarea class="form-control" v-model="context" placeholder="답변을 입력하세요."/>
            <span class="input-group-text" @click="createComment">작성</span>
        </div>
    </div>
</template>

<script>
import data from "@/data";
export default {
    name: 'QnaAnswerCreate',
    props: {
        contentId: Number,
        reloadComment: Function,
    },
    data() {
        return{
            name: "관리자",
            context: "",
        };
    },
    methods: {
        createComment() {
            const today = new Date();
            const today_form = today.getFullYear() + '-' + ('0' + (today.getMonth() + 1)).slice(-2) + '-' + ('0' + today.getDate()).slice(-2);
            data.Answer.push({
                comment_id: data.Answer[data.Answer.length - 1].comment_id + 1,
                user_id: 1,
                // user_name: this.name,
                content_id: this.contentId,
                context: this.context,
                created_at: today_form,
                updated_at: null
            });
            this.reloadComment();
            this.context = "";
            
        }
    }
}
</script>

<style scoped>
.comment-create {
  display: flex;
  margin-bottom: 1em;
}
</style>