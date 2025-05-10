<script setup>
import { computed } from 'vue'
import SvgIcon from '@jamescoyle/vue-icon';
import { mdiCartOutline, mdiAccountCircleOutline } from '@mdi/js';

const props = defineProps({
  disabled: {
    type: Boolean,
    default: false
  },
  alter: {
    type: Boolean,
    default: false
  },
  text: {
    type: Boolean,
    default: false
  },
  icon: {
    type: Boolean,
    default: false
  },
  buttonWidth: {
    type: String,
    default: '190px'
  }
})

const emit = defineEmits(['click'])

const buttonClass = computed(() => {
  if (props.alter) return 'button-alter'
  if (props.text) return 'text-button'
  if (props.icon) return "icon-button"
  return 'button'
})

const buttonWidthComputed = computed(() => {
  console.log(buttonClass)
  if (buttonClass.value === 'button') {
    return props.buttonWidth;
  } else {
    return 'auto'
  }
});

const handleClick = () => {
  if (!props.disabled) {
    emit('click')
  }
}
</script>

<template>
  <div>{{ buttonWidth }}</div>
  <button
    :class="buttonClass"
    :style="{ width: buttonWidthComputed}"
    :disabled="disabled"
    @click="handleClick"
  >
    <slot></slot>
    <slot name="icon"></slot>
  </button>
</template>

<style scoped>

.icon-button{
  width: fit-content;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background-color: transparent;
  border: none;
  padding: 0;
  color:#1E1E1E;
  transition: color 0.1s;
}

.icon-button:hover{
  color:#6C6C6C;
}

.text-button{
  font-size: 20px;
  height: 24px;
  width: auto;
  background-color: transparent;
  border: none;
  padding: 0;
  color:#1E1E1E;
  transition: color 0.1s;

}

.text-button:hover {
  color:#6C6C6C;
}

.button-alter{
    padding: 12px 24px;
    border: none;
    border-radius: 62px;
    font-size: 20px;
    font-weight: 500;
    height: 64px;
    width: 190px;
    cursor: pointer;
    transition: background-color 0.2s;
}

.button-alter:not(:disabled) {
  background-color: #F0F0F0;
  color: #6C6C6C;
}

.button {
  padding: 12px 24px;
  border: none;
  border-radius: 62px;
  font-size: 20px;
  font-weight: 500;
  height: 64px;
  width: 190px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.button:not(:disabled) {
  background-color: #FFC633; /* Желтый цвет для активной кнопки */
  color: #1E1E1E;
}

.button:disabled {
  background-color: #DDDDDD; /* Серый цвет для неактивной кнопки */
  color: #888;
  cursor: not-allowed;
}

.button:not(:disabled):hover {
  background-color: #FFD966; /* Светло-желтый при наведении */
}
</style>
