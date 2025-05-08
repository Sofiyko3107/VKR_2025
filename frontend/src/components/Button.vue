<script setup>
const props = defineProps({
  disabled: {
    type: Boolean,
    default: false

  },
  alter: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['click'])

const handleClick = () => {
  if (!props.disabled) {
    emit('click')
  }
}
</script>

<template>
  <button
    :class="[alter ? 'button-alter' : 'button']"
    :disabled="disabled"
    @click="handleClick"
  >
    <slot></slot>
  </button>
</template>

<style scoped>

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