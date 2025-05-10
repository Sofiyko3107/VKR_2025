<script setup>
import { computed } from 'vue';
import SvgIcon from '@jamescoyle/vue-icon';
import { mdiRadioboxBlank, mdiRadioboxMarked } from '@mdi/js';

const props = defineProps({
    modelValue: {
        type: [String, Number, Boolean],
        default: ''
    },
    value: {
        type: [String, Number, Boolean],
        required: true
    },
    label: {
        type: String,
        default: ''
    },
    disabled: {
        type: Boolean,
        default: false
    }
});

const emit = defineEmits(['update:modelValue']);

const isChecked = computed(() => props.modelValue === props.value);

const handleClick = () => {
  if (!props.disabled) {
    emit('update:modelValue', props.value);
  }
};
</script>

<template>
  <div 
    class="radio-button"
    :class="{ 'disabled': disabled }"
    @click="handleClick"
  >
    <svg-icon
      type="mdi"
      :path="isChecked ? mdiRadioboxMarked : mdiRadioboxBlank"
      :size="24"
      :color="disabled ? '#DDDDDD' : (isChecked ? '#FFC633' : '#DDDDDD')"
    />
    <span class="label" :class="{ 'disabled': disabled }">
      {{ label }}
    </span>
  </div>
</template>

<style scoped>
.radio-button {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  user-select: none;
}

.label {
  font-size: 20px;
  color: #1e1e1e;
}

.disabled {
  cursor: not-allowed;
  opacity: 0.6;
}

.label.disabled {
  color: #999;
}
</style>