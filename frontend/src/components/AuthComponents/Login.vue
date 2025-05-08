<script setup>
import InputGroup from "@/components/InputGroup.vue";
import { mdiEmailFastOutline, mdiLock} from "@mdi/js";
import SvgIcon from "@jamescoyle/vue-icon";
import Button from "@/components/Button.vue";
</script>

<template>
  <div class="login-form">
    <input-group
      input-placeholder="Электронная почта"
      with-icon
    >
      <template #icon>
        <SvgIcon type="mdi" :path="mdiEmailFastOutline"/>
      </template>
    </input-group>
    <input-group
      input-placeholder="Пароль"
      with-icon
    >
      <template #icon>
        <SvgIcon type="mdi" :path="mdiLock"/>
      </template>
    </input-group>
    <div class="login-actions">
      <Button text>забыли пароль?</Button>
      <Button>Войти</Button>
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
