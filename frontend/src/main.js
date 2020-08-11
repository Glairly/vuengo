import Vue from 'vue'
import './plugins/axios'
import App from './App.vue'
import VueResource from 'vue-resource'
import vuetify from './plugins/vuetify';
import store from './store'
import router from './router'

Vue.use(VueResource)

Vue.config.productionTip = false

new Vue({
  vuetify,
  store,
  router,
  render: h => h(App)
}).$mount('#app')
