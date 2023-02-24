<template>
  <div class="container my-5">
    <div class="pb-5">
        <button style="float: right;" @click="write">글쓰기</button>
    </div>
    <table class="table caption-top table-hover table-bordered"> <!-- table-striped -->
        <caption>문의게시판</caption>
        <thead class="table-success">
            <tr>
                <th style="width: 5%" scope="col">#</th>
                <th style="width: 50%" scope="col">제목</th>
                <th style="width: 15%" scope="col">작성자</th>
                <th style="width: 15%" scope="col">작성일</th>
                <th style="width: 15%" scope="col">답변</th>
            </tr>
        </thead>
        <tbody>
            <tr :key="value.id" v-for="(value, ) in items" @click="detail(value.id)"> <!--목록 내용-->
                <td>{{value.id}}</td>
                <td>{{value.title}}</td>
                <td>{{value.writer.substring(0, 1)+'*'+value.writer.substring(2)}}</td>
                <td>{{value.written_date}}</td>
                <td>{{value.solvebool ? '답변완료' : '답변대기'}}</td>
                <!-- <td>{{daf.filter(item => item.content_id === value.content_id).length > 0 ? '답변완료' : '답변대기'}}</td> -->
            </tr>
            <tr v-if="!items.length">
                <td></td>
                <td>질문글이 존재 하지 않습니다.</td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
        </tbody>
    </table>

  </div>
</template>

<script>
import axios from 'axios';
// import data from '@/data'

// let items = data.Question.sort((a,b) => {return b.content_id - a.content_id})

export default {
    name: 'QnaView',
    data() {
        return {
            items: {},//data.Question.sort((a,b) => {return b.content_id - a.content_id}),
            // daf: data.Answer
        };
    },
    mounted() {
        this.get_Questions()
    },
    methods: {
        get_Questions() {
            axios
            .get('api/v1/questions/',{
            })
            .then(response => {
                // console.log(response.data)
                this.items = response.data
                // console.log(this.items.length)
            })
            .catch(error => {
                console.error(error)
            })
        },
        detail(content_id) {
            this.$router.push({
                name: 'QnaDetail', 
                params: {
                    contentId: content_id
                }
            })
        },
        write() {
            this.$router.push({
                path: 'qna/create'
            })
        },
    }
};
</script>

