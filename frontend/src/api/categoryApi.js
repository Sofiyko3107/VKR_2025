import api from '@/plugins/axios'

const resource = 'category'

export default {
  get(params = {}) {
    return api.get(`${resource}/all`, { params })
  },
}
