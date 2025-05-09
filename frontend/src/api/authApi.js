import api from "@/plugins/axios/index.js";


export default {
  getUserData() {
    return api.get('profile')
  },
  logout() {
    return api.post('logout')
  },
  login(params) {
    return api.post('login', params)
  }
}
