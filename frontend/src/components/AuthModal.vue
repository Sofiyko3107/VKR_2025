<script setup>

import SwitchButton from "@/components/SwitchButton.vue";
import Login from "@/components/AuthComponents/Login.vue";
import { ref } from "vue"
import Register from "@/components/AuthComponents/Register.vue";
import Button from "@/components/Button.vue";
import {mdiClose} from "@mdi/js";
import SvgIcon from "@jamescoyle/vue-icon";
import {useRouter} from "vue-router";

const activeTab = ref('auth');
const router = useRouter();

</script>

<template>
  <div class="fullwidth-center">
      <div class="auth-wrapper">
        <div class="auth-side">
        </div>
        <div class="auth-content">
          <div class="auth-header">
            <switch-button v-model="activeTab"></switch-button>
            <Button icon @click="router.back">
              <template #icon>
                <SvgIcon type="mdi" :path="mdiClose"/>
              </template>
            </Button>
          </div>
          <Login v-if="activeTab === 'auth'"></Login>
          <Register v-else @login="activeTab = 'auth'"></Register>
        </div>
      </div>
  </div>

</template>

<style scoped>
.fullwidth-center {
  z-index: 100;
  position: fixed;
  top: 0; right: 0; bottom: 0; left: 0;
  background-color: #1E1E1E80;
}

.auth-wrapper {
  display: flex;
  width: 820px;
  height: 540px;
  margin: 200px auto auto;
  background-color: white;
  border-radius: 20px;
  opacity: 1;
}

.auth-side {
  width: 288px;
  height: 100%;
  background-color: #F1AF25;
  border-radius: 20px 0 0 20px;
}

.auth-header {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    width: 100%;
    gap: 54px;
    padding-right: 24px;
}

.auth-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  flex-grow: 1;
  margin-top: 23px;
}
</style>
