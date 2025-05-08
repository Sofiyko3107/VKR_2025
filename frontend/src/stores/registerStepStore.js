import {defineStore} from "pinia";
import {computed, ref} from "vue";

export const useRegisterStepsStore = defineStore('registerStepsStore', () => {
  const email = ref('')
  const password = ref('')
  const password2 = ref('')

  const getEmail = computed(() => email.value)
  const getData = computed(() => {
    return {
      email: email.value,
      password: password.value,
      password2: password2.value
    }
  })
  function setEmail(e) {
    email.value = e;
  }

  function setPassword(p) {
    password.value = p;
  }

  function setPassword2(p) {
    password2.value = p;
  }

  return { getEmail, getData, setEmail, setPassword, setPassword2 }
})
