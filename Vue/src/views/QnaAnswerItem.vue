<template>
    <div>
        <div class="comment-list-item">
            <div class="comment-list-item-name">
                <div>{{name}}</div>
                <div>{{commentObj.created_at}}</div>
            </div>
            <div class="comment-list-item-context">{{commentObj.context}}</div>
            <div class="comment-list-item-button">
                <button @click="deleteData">삭제</button>
            </div>
        </div>
    </div>
</template>

<script>
import data from '@/data';

export default {
    name: 'QnaAnswerItem', 
    props: {
        commentObj: Object,
        reloadComment: Function,
    },
    data() {
        // const commentId = Number(this.$route.params.comment_id);
        // const realId = Number(data.Answer.map((x, index) => {if (x.comment_id == commentId) {return index}}).filter(e => e)[0]);
        return {
            name: data.User.filter(item => item.user_id === this.commentObj.user_id)[0].name,
            // rId: realId,
            // commentId: commentId,
        }
    },
    methods: {
        deleteData() {
            const commentId = this.commentObj.comment_id;
            const realId = data.Answer.findIndex(item => item.comment_id === commentId)
            data.Answer.splice(realId, 1)
            this.reloadComment()
        },
    }
}
</script>

<style scoped>
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
  width: 12.5%;
  border: 0.5px solid #D1E7DD;
  padding: 1em;
  background-color: #D1E7DD;
}
.comment-list-item-context {
  display: flex;
  justify-content: left;
  align-items: center;
  padding: 1.5em;
  width: 75%;
  border: 3px solid #D1E7DD;
}
.comment-list-item-button {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 12.5%;
  border: 3px solid #D1E7DD;
  padding: 1em;
  background-color: #D1E7DD;
}
.btn {
  margin-bottom: 1em;
}
</style>