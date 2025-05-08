import api from "@/plugins/axios/index.js";

const resourse = 'register'

export default {
  register(params) {
    return api.post('register', params)
  }
}
