<script setup>

import {computed} from "vue";

const props = defineProps({
  steps: {
      type: Number,
      required: true,
    },
  currentStep: {
    type: Number,
    required: true,
    validator: value => value > 0
  }
})

const stepWidth = computed(() => {
  return `${100 / props.steps}%`;
});
</script>

<template>
  <div class="steps-container">
    <div
      v-for="index in steps"
      :key="index"
      class="step-wrapper"
      :style="{ width: stepWidth }"
    >
      <div class="step-content">
        <div
          class="step-circle"
          :class="{
            'active': index < currentStep,
            'current': index === currentStep
          }"
        >
        </div>
      </div>
      <div
        v-if="index < steps"
        class="step-line"
        :class="{ 'active': index < currentStep }"
      ></div>
    </div>
  </div>
</template>

<style scoped>
.steps-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  position: relative;
}

.step-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
}

.step-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  z-index: 2;
}

.step-circle {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background-color: #e0e0e0;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #757575;
  font-weight: bold;
  margin-bottom: 8px;
  transition: all 0.3s ease;
}

.step-circle.active {
  background-color: #FFC633;
}

.step-circle.current {
  background-color: #FFC633;
}

.step-line {
  position: absolute;
  top: 16px;
  left: calc(50% + 16px);
  right: calc(-50% + 16px);
  height: 2px;
  background-color: #F0F0F0;
  z-index: 1;
}

.step-line.active {
  background-color: #FFC633;
}
</style>
