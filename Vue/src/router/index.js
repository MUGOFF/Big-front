import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import About from '../views/AboutView.vue'
import SignUp from '../views/SignupView.vue'
import Login from '../views/LoginView.vue'
import NoticeView from '../views/NoticeView.vue'
import QnaView from '../views/QnaView.vue'
import GuideView from '../views/GuideView.vue'
import PriceCategory from '../views/CategoryPriceView.vue'
import ProductView from '../views/ProductView.vue'
import SearchdetailResult from '../views/SearchdetailResultView.vue'
import SearchDetail from '../views/SearchDetailView.vue'
import ProposalBuyer from '../views/ProposalBuyer.vue'
import ProposalSeller from '../views/ProposalSeller.vue'
import Contract from '../views/ContractView.vue'
import Contract_final from '../views/ContractView_final.vue'
import Profile from '../views/ProfileView.vue'
import ReConfirm from '../views/ReConfirmView.vue'
import MyPage from '../views/MyPageView.vue'
import NoticeDetail from '../views/NoticeDetail.vue'
import NoticeCreate from '../views/NoticeCreate.vue'
import NoticeUpdate from '../views/NoticeUpdate.vue'
import QnaDetail from '../views/QnaDetail.vue'
import QnaCreate from '../views/QnaCreate.vue'
import QnaUpdate from '../views/QnaUpdate.vue'
import Deal from '../views/DealView.vue'
import ProductCreate from '../views/ProductCreate.vue'
import store from "../store/index.js"

const requireAuth = () => (to, from, next) => {
  const token = localStorage.getItem('token')
  if (token) {
    store.state.isLogin = true
    return next()
  }
  alert("로그인 후 이용해주세요.") 
  next('/login')
}

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: About
  },
  {
    path: '/signup',
    name: 'signup',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: SignUp
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/notice',
    name: 'notice',
    component: NoticeView
  },
  {
    path: '/notice/detail/:contentId',
    name: 'NoticeDetail',
    component: NoticeDetail,
  },
  {
    path: '/notice/create/:contentId?',
    name: 'NoticeCreate',
    component: NoticeCreate
  },
  {
    path: '/notice/update/:contentId',
    name: 'NoticeUpdate',
    component: NoticeUpdate
  },
  {
    path: '/qna',
    name: 'qna',
    component: QnaView
  },
  {
    path: '/qna/detail/:contentId',
    name: 'QnaDetail',
    component: QnaDetail,
    beforeEnter: requireAuth()
  },
  {
    path: '/qna/create',
    name: 'QnaCreate',
    component: QnaCreate,
    beforeEnter: requireAuth()
  },
  {
    path: '/qna/update/:contentId',
    name: 'QnaUpdate',
    component: QnaUpdate,
    beforeEnter: requireAuth()
  },
  {
    path: '/guide',
    name: 'guide',
    component: GuideView
  },
  {
    path: '/price',
    name: 'price',
    component: PriceCategory
  },
  {
    path: '/product/:contentId',
    name: 'product',
    component: ProductView
  },
  {
    path: '/searchdetail',
    name: 'SearchDetail',
    component: SearchDetail,
    beforeEnter: requireAuth()
  },
  {
    path: '/searchdetail/result',
    name: 'SearchdetailResult',
    component: SearchdetailResult,
    props: true,
  },
  {
    path: '/buyer/:contentId',
    name: 'buyer',
    component: ProposalBuyer
  },
  {
    path: '/seller/:contentId',
    name: 'seller',
    component: ProposalSeller
  },
  {
    path: '/contract/:c_id',
    name: 'contract',
    component: Contract,
  },
  {
    path: '/contract_final/:c_id',
    name: 'contract_final',
    component: Contract_final,
  },
  {
    path: '/profile',
    name: 'profile',
    component: Profile
  },
  {
    path: '/reconfirm',
    name: 'reconfirm',
    component: ReConfirm,
    beforeEnter: requireAuth()
  },
  {
    path: '/mypage',
    name: 'mypage',
    component: MyPage,
  },
  {
    path: '/deal',
    name: 'deal',
    component: Deal
  },
  {
    path: '/productcreate',
    name: 'productcreate',
    component: ProductCreate,
    beforeEnter: requireAuth()
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
