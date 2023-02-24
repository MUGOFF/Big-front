<template>
  <div class="container my-5">
    <!-- <div class="pb-5">
        <button style="float: right;" @click="write">글쓰기</button>
    </div> -->
    <table class="table caption-top table-hover table-bordered"> <!-- table-striped -->
        <caption>공지사항</caption>
        <thead class="table-success">
            <tr>
                <th style="width: 10%" scope="col">#</th>
                <th style="width: 70%" scope="col">제목</th>
                <!-- <th style="width: 22.5%" scope="col">작성자</th> -->
                <th style="width: 20%" scope="col">작성일</th>
            </tr>
        </thead>
        <tbody>
            <tr :key="value.id" v-for="(value, ) in items" @click="detail(value.id)" > <!--목록 내용-->
                <td>{{value.id}}</td>
                <td>{{value.title}}</td>
                <!-- <td>{{value.user_name}}</td> -->
                <td>{{value.written_date}}</td>
            </tr>
        </tbody>
    </table>
    <div class="d-flex" >

    </div>

  </div>
</template>

<script>
import axios from "axios"
// import data from '@/data'

// let items = data.Content.sort((a,b) => {return b.content_id - a.content_id})
// items = items.map(contentItem => {
//     return {
//         ...contentItem, 
//         user_name: data.User.filter(userItem => userItem.user_id === contentItem.user_id)[0].name
//         }
//     })

export default {
    name: 'NoticeView',
    data() {
        return {
            items: {}//data.Content.sort((a,b) => {return b.content_id - a.content_id})
        };
    },
    mounted() {
        this.get_notices()
    },
    methods: {
        get_notices() {
            axios
            .get('api/v1/notices/',{
            })
            .then(response => {
                // console.log(response)
                this.items = response.data
                
            })
            .catch(error => {
                console.error(error)
            })
        },
        detail(content_id) {
            this.$router.push({
                name: 'NoticeDetail', 
                params: {
                    contentId: content_id 
                }
            })
        },
        write() {
            this.$router.push({
                path: 'notice/create'
            })
        },
    }
};
</script>
