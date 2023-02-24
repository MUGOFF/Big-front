export default {
    User: [
        {
            user_id: 1,
            name: 'admin',
            created_at: '1999-01-01'
        },
        {
            user_id: 2,
            name: 'mid',
            created_at: '2099-01-01'
        },
        {
            user_id: 3,
            name: 'norm',
            created_at: '2022-01-01'
        },
    ],

    Content: [
        {
            content_id: 1,
            user_id: 1,
            user_name: 'admin',
            title: '태초의 공지사항',
            context: '이 편지는 영국에서 시작되어',
            created_at: '1999-01-01',
            updated_at: null
        },
        {
            content_id: 2,
            user_id: 3,
            user_name: 'norm',
            title: '지우 포켓몬 트레이너 은퇴',
            context: '이 편지는 일본에서 시작되어',
            created_at: '1999-12-31',
            updated_at: null
        },
        {
            content_id: 3,
            user_id: 2,
            user_name: 'mid',
            title: '최종 공지사항입니다',
            context: '이 편지는 미국에서 시작되어',
            created_at: '2022-12-19',
            updated_at: null
        }
    ],

    Question: [
        {
            content_id: 1,
            user_id: 1,
            user_name: 'admin',
            title: '질문1 test',
            context: '이 편지는 영국에서 시작되어',
            created_at: '1999-01-01',
            updated_at: null,
        },
        {
            content_id: 2,
            user_id: 3,
            user_name: 'norm',
            title: 'question2 시험',
            context: '이 편지는 일본에서 시작되어',
            created_at: '1999-12-31',
            updated_at: null,
        },
        {
            content_id: 3,
            user_id: 2,
            user_name: 'mid',
            title: '질문3 제목',
            context: '이 편지는 미국에서 시작되어',
            created_at: '2022-12-19',
            updated_at: null,
        }
    ],

    Answer: [
        {
            comment_id: 1,
            user_id: 1,
            user_name: 'admin',
            content_id: 1,
            context: '왜 편지가 영국에서 시작되었는데 한글로 써져있나요',
            created_at: '2020-01-01',
            updated_at: null
        },
        {
            comment_id: 2,
            user_id: 3,
            user_name: 'norm',
            content_id: 3,
            context: '답변 내용 뭐로하지2',
            created_at: '2021-01-01',
            updated_at: null
        },
        {
            comment_id: 3,
            user_id: 2,
            user_name:'mid',
            content_id: 2,
            context: '답변 내용3',
            created_at: '2022-12-20',
            updated_at: null
        },
        {
            comment_id: 4,
            user_id: 2,
            user_name:'mid',
            content_id: 1,
            context: '영국에는 무슨 야채가 잘 자라나요?',
            created_at: '2022-12-20',
            updated_at: null
        },
    ],
}