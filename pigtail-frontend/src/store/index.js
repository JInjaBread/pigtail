import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
  state: {
    auth: false,
    accGroup: '',
    acessToken: '',
    refreshToken: ''
  },
  mutations: {
    updateStorage(state,{access, refresh, groups}){
      state.acessToken = access
      state.refreshToken = refresh
      state.accGroup = groups
    }
  },

  actions: {
    userLogin (context, usercredentials){
      return new Promise((resolve, reject) => {
        axios
        .post('/api-token/', {
          username: usercredentials.username,
          password: usercredentials.password
        })
        .then(response => {
          context.commit('updateStorage', {access: response.data.access, refresh: response.data.refresh, groups: response.data.groups})
          const auth = this.state.auth
          localStorage.setItem('auth', !auth)
          localStorage.setItem('accessToken', response.data.access)
          axios.defaults.headers.common['Authorization'] = 'Bearer ${response.data.access}'
          resolve()
        })
      })
    }
  },
  modules: {
  }
})
