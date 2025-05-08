<script setup>

import {mdiCheckCircle} from "@mdi/js";
import SvgIcon from "@jamescoyle/vue-icon";
import Button from "@/components/Button.vue";
import {useRegisterStepsStore} from "@/stores/registerStepStore.js";

const store = useRegisterStepsStore()
console.log(store.getData)
</script>

<template>
  <div class="step4-header">
    <SvgIcon type="mdi" :path="mdiCheckCircle"></SvgIcon>
    <div class="T1">Регистрация прошла успешно</div>
  </div>
  <div>Теперь вы можете войти в личный кабинет</div>
  <div class="step4-actions">
    <Button button-width="224px">Войти</Button>
  </div>
</template>

<style scoped>
.step4-header {
  display: flex;
  flex-direction: row;
  gap: 12px;
  margin-top: 62px;
  margin-bottom: 73px;
}
.step4-actions {
  margin-top: 12px;
}
</style>
