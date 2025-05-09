<script setup>
import InputGroup from "@/components/InputGroup.vue";
import {mdiLock} from "@mdi/js";
import SvgIcon from "@jamescoyle/vue-icon";
import Button from "@/components/Button.vue";
import {ref} from "vue";
import {useRegisterStepsStore} from "@/stores/registerStepStore.js";
import Repository from "@/api/registrationApi.js"

const emit = defineEmits(['next', 'prev'])
const store = useRegisterStepsStore()

const password = ref('')
const password2 = ref('')

const handleContinue = async () => {
  store.setPassword(password.value)
  store.setPassword2(password2.value)
  const { data } = await Repository.register(store.getData)
  emit('next')
}

</script>

<template>
  <div class="step3-header">Придумайте надёжный пароль</div>
  <div>
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
    <input-group
      input-placeholder="Повторите пароль"
      with-icon
      password-input
      v-model="password2"
    >
      <template #icon>
        <SvgIcon type="mdi" :path="mdiLock"/>
      </template>
    </input-group>
  </div>
  <div>
    <Button button-width="224px" @click="handleContinue">Продолжить</Button>
  </div>
</template>

<style scoped>
.step3-header {
  margin-top: 36px;
}
</style>
