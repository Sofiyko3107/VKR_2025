import api from "@/plugins/axios/index.js";

export default {
  send_confirmation_message(params) {
    return api.post('send-confirmation-message', params)
  },
  check_status(params) {
    return api.get('check-confirmation', {params: params});
  },
  verify_email(token) {
    return api.get(`verify-email/${token}`)
  },
}
