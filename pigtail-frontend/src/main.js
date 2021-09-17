import { createApp } from 'vue'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

library.add(fas);
axios.defaults.baseURL = 'http://127.0.0.1:8000'

createApp(App)
.component('fa', FontAwesomeIcon)
.use(store)
.use(router, axios)
.mount('#app')
