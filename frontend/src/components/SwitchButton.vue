<script setup>
import { ref } from 'vue'

const modelValue = defineModel()

const emit = defineEmits(['click-on-active'])
function handleClick(tab) {
  modelValue.value = tab
  console.log(modelValue)
  // if (tab !== activeTab.value) {
  //   emit('click-on-active', activeTab.value)
  // }
}
</script>

<template>
  <div class="switch-container">
    <div class="slider">
      <div
        class="text"
        :class="{ active: modelValue === 'auth' }"
        @click="handleClick('auth')"
      >
        Авторизация
      </div>
      <div
        class="text"
        :class="{ active: modelValue === 'reg' }"
        @click="handleClick('reg')"
      >
        Регистрация
      </div>
      <div
        class="slider-button"
        :class="{ moved: modelValue === 'reg' }"
      ></div>
    </div>
  </div>
</template>

<style scoped>
.switch-container {
  width: 318px;
  height: 48px;
  position: relative;
}

.slider {
  position: relative;
  width: 100%;
  height: 100%;
  background: #F5F5F5;
  border-radius: 62px;
  overflow: hidden;
  display: flex;
}

.text {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  color: #1E1E1E;
  transition: color 0.3s;
  cursor: pointer;
  z-index: 2;
  position: relative;
}

.text.active {
  color: #FFFFFF;
}

.slider-button {
  position: absolute;
  top: 0;
  left: 0;
  width: 50%;
  height: 100%;
  background: black;
  border-radius: 62px;
  transition: transform 0.3s ease;
  z-index: 1;
}

.slider-button.moved {
  transform: translateX(100%);
}
</style>
