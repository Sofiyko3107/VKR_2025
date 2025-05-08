<script setup>

import {mdiEmailFastOutline} from "@mdi/js";
import SvgIcon from "@jamescoyle/vue-icon";
import InputGroup from "@/components/InputGroup.vue";
import Button from "@/components/Button.vue";
import {ref} from "vue";
import { useRegisterStepsStore } from "@/stores/registerStepStore.js";

const store = useRegisterStepsStore();

const emit = defineEmits(['next', 'prev']);

const data = ref({
  email: ''
});

const handleNextStep = () => {
  store.setEmail(data.value.email);
  emit('next');
}
</script>

<template>
    <p class="T1 step1-header">Укажите адрес электронной почты для регистрации</p>
    <input-group
      input-placeholder="Электронная почта"
      with-icon
      v-model="data.email"
    >
      <template #icon>
        <SvgIcon type="mdi" :path="mdiEmailFastOutline"/>
      </template>
    </input-group>
    <div class="step1-agreed">
      <input class="login-checkbox" type="checkbox">
      <div style="flex-grow: 1">Я согласен(а) на обработку персональных данных</div>
    </div>
    <div class="step1-actions">
      <Button @click="handleNextStep">Продолжить</Button>
    </div>
</template>

<style scoped>
.step1-header {
  margin-top: 52px;
}
.step1-agreed {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 16px;
  margin-top: 34px;
  margin-bottom: 34px;
}
.step1-actions {
  display: flex;
  justify-content: flex-end;
}
</style>
