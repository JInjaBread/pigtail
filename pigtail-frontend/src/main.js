import { createApp } from 'vue'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import App from './App.vue'
import router from './router'
import WaveUI from 'wave-ui'
import 'wave-ui/dist/wave-ui.css'
import store from './store'
import axios from 'axios'

library.add(fas);
axios.defaults.baseURL = 'http://127.0.0.1:8000'

const app = createApp(App)
.component('fa', FontAwesomeIcon)
.use(store)
.use(router, axios);

new WaveUI(app, {
    // Some Wave UI options.
  })

  app.mount('#app')