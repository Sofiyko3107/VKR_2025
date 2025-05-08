<script setup>
import { ref, onMounted, onUnmounted} from "vue";
import Button from "@/components/Button.vue";
import {mdiEmail} from "@mdi/js";
import SvgIcon from "@jamescoyle/vue-icon";
import Repository from "@/api/registerHelperApi.js"
import {useRegisterStepsStore} from "@/stores/registerStepStore.js";

const emit = defineEmits(['next', 'prev']);
const store = useRegisterStepsStore()
let interval = null;

const checkStatus = async () => {
  const { data } = await Repository.check_status({email: store.getEmail})
  if (data.status === 'confirmed') {
    if (interval) clearInterval(interval)
    emit('next')
  }
};

const initInterval = () => {
  interval = setInterval(checkStatus, 5000)
}

onMounted(() => {
  initInterval()
})


onUnmounted(() => {
    if (interval) clearInterval(interval);
});
</script>

<template>
  <div class="step2-header">
    <SvgIcon type="mdi" :path="mdiEmail"></SvgIcon>
    <div class="T1">Проверьте вашу почту</div>
  </div>
  <div style="margin-bottom: 34px">Мы отправили ссылку для подтверждения вашей электронной почты</div>
  <div>Не получили письмо?</div>
  <div class="step2-actions">
    <Button button-width="300px">Отправить повторно</Button>
    <Button button-width="300px" alter>Указать другой адрес</Button>
  </div>
</template>

<style scoped>
.step2-header {
  display: flex;
  flex-direction: row;
  gap: 12px;
  margin-top: 40px;
  margin-bottom: 44px;
}

.step2-header > div {
  flex-grow: 1;
}

.step2-actions {
  display: flex;
  flex-direction: column;
  margin-top: 8px;
  gap: 8px
}
</style>
