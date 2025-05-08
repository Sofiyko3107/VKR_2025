import api from "@/plugins/axios/index.js";

export default {
  send_confirmation_message(params) {
    return api.post('send-confirmation-message', params)
  },
  check_status(p) {
    return api.get('check-confirmation', {params: p});
  }
}
