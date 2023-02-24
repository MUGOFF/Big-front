<template>
  <NavBar />
  <router-view/>
  <FooterVue/>
  <ToTop/>
</template>


<script>
import axios  from 'axios'
// @ is an alias to /src
import NavBar from '@/components/NavBar.vue'
import FooterVue from '@/components/Footer.vue'
import ToTop from '@/components/ToTopButton.vue'

export default {
  name: 'App',
  components: {
    NavBar,FooterVue,ToTop
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
    const token = this.$store.state.token

    if (token) {
      axios.defaults.headers.common['Authorization'] = "Token " +token
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  },
}
</script>

<style>
#app {
  font-family: GmarketSansMedium;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #9ac486;
}
@font-face {
    font-family: 'GmarketSansMedium';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/GmarketSansMedium.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
</style>
