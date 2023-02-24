<template>
  <div>
    <div :key="item.comment_id" v-for="item in comments">
        <QnaAnswerItem :commentObj="item" :reloadComment="reloadComment"/>
    </div>
    <QnaAnswerCreate :contentId="contentId" :reloadComment="reloadComment"/>
  </div>
</template>

<script>
import data from "@/data";
import QnaAnswerItem from './QnaAnswerItem';
import QnaAnswerCreate from './QnaAnswerCreate';

export default {
  name: "QnaAnswer",
  components: {
    QnaAnswerItem,
    QnaAnswerCreate,
  },
  props: {
    contentId: Number
  },
  data() {
    return {
      comments: data.Answer.filter(item => item.content_id === this.contentId),
    }
  },
  methods: {
    reloadComment() {
      this.comments = data.Answer.filter(item => item.content_id === this.contentId)
    },
  }
};
</script>