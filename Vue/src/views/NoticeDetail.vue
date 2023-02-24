<template>
    <div class="container my-5">
        <div class="pb-5">
            <div style="float: left;" class="col">글 번호: {{ items.id }}</div>
            <!-- <button style="float: right;" @click="deleteData">삭제</button>
            <button style="float: right;" @click="updateData">수정</button> -->
        </div>
        <div class="row my-1">
            <div class="container text-center">
                
                <div style="float: center;" class="col"><h2>{{ items.title }}</h2></div>
                
                <!-- <div style="float: right;" class="m-2">{{ items.updated_at !== null  ? items.updated_at : '수정 없음'}}</div>
                <div style="float: right;" class="m-2">수정일:</div> -->
                <div style="float: right;" class="m-2">작성일: {{ items.written_date }}</div>
                <!-- <div style="float: right;" class="m-2">작성자: {{ items.user_name }}</div> -->
                
                
            </div>

            <div class="container-fluid text-center border py-5">
                <div>{{ items.content }}</div>
            </div>

        </div>
        <button @click="toList" class="mt-5">목록</button>
        
    </div>
</template>

<script>
import data from '@/data';
import axios from 'axios';

export default {
    name: 'NoticeDetail', 
    data() {
        // const contentId = Number(this.$route.params.contentId); // view 페이지에서 클릭한 글의 글번호
        // const realId = Number(data.Content.map((x, index) => {if (x.content_id == contentId) {return index}}).filter(e => e)[0]);
        // const contentData = data.Content.filter(item => item.content_id === contentId)[0];
        return {
            items: {},//contentData,
            // contentId: contentId,
            // rId: realId,
            // user: data.User.filter((i) => {if (i.user_id === contentData.user_id) {return i.name}})[0],

        }
    },
    mounted(){
        this.get_Notice()
    },
    methods: {
        get_Notice() {
            axios.get('api/v1/notices_detail/?id='+Number(this.$route.params.contentId))
            .then(response =>{
                console.log(response.data)
                this.items = response.data[0]
            })
            .catch(error =>{
                console.error(error)
            })
        },
        toList() {
            this.$router.push({
                path: '/notice'
            })
        },
        // deleteData() {
        //     data.Content.splice(this.rId, 1)
        //     this.$router.push({
        //         path: '/notice'
        //     })
        // },
        // updateData() {
        //     const contentId = Number(this.$route.params.contentId);
        //     this.$router.push({
        //         name: 'NoticeUpdate',
        //         params: {
        //             contentId: contentId
        //         }
        //     })
        // }

    }

}
</script>
