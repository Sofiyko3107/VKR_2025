<script setup>
import InputGroup from "@/components/InputGroup.vue";
import { mdiEmailFastOutline, mdiLock} from "@mdi/js";
import SvgIcon from "@jamescoyle/vue-icon";
import Button from "@/components/Button.vue";
import {ref} from "vue";
import Repository from '@/api/authApi.js'
import { useRouter} from "vue-router";

const router = useRouter()
const email = ref('')
const password = ref('')

const handleLogin = async () => {
  try {
    const { data } = await Repository.login({ email: email.value, password: password.value})
    console.log(data)
    await router.push({name: 'main'})
  } finally {
      console.log('finally')
  }
}

</script>

<template>
  <div class="login-form">
    <input-group
      input-placeholder="Электронная почта"
      with-icon
      v-model="email"
    >
      <template #icon>
        <SvgIcon type="mdi" :path="mdiEmailFastOutline"/>
      </template>
    </input-group>
    <input-group
      input-placeholder="Пароль"
      with-icon
      password-input
      v-model="password"
    >
      <template #icon>
        <SvgIcon type="mdi" :path="mdiLock"/>
      </template>
    </input-group>
    <div class="login-actions">
      <Button text>забыли пароль?</Button>
      <Button @click="handleLogin()">Войти</Button>
    </div>
  </div>
</template>

<style scoped>
.login-form {
  flex-grow: 1;
  margin-top: 86px;
}

.login-actions {
  display: flex;
  flex-direction: row;
  margin-top: 48px;
  align-items: center;
  justify-content: space-between;
}
</style>
