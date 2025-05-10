<script setup>

const props = defineProps({
  options: {
    type: Array,
    default: () => []
  },
  selected: {
    type: Array,
    default: () => []
  }
});

const emit = defineEmits(['update:selected']);

const toggleOption = (optionValue) => {
  console.log(optionValue)
  const newSelected = props.selected.includes(optionValue)
    ? props.selected.filter(v => v !== optionValue)
    : [...props.selected, optionValue];
  console.log(newSelected);
  emit('update:selected', newSelected);
};
</script>

<template>
  <div class="checkbox-group">
    <ul class="options-list">
      <li
        v-for="option in options"
        :key="option"
        class="option-item"
        @click="toggleOption(option)"
      >
        <div class="checkbox" :class="{ checked: selected.includes(option) }">
          <span v-if="selected.includes(option)" class="check-icon">✓</span>
        </div>
        <span class="option-label">{{ option }}</span>
      </li>
    </ul>
  </div>
</template>

<style scoped>
.checkbox-group {
  font-family: Arial, sans-serif;
}

.group-title {
  font-size: 16px;
  font-weight: bold;
  margin-bottom: 12px;
  color: #333;
}

.options-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.option-item {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
  cursor: pointer;
}

.checkbox {
  width: 18px;
  height: 18px;
  border: 2px solid #ccc;
  border-radius: 4px;
  margin-right: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
}

.checkbox.checked {
  border-color: #FFC633;
  background-color: #FFC633;
}

.check-icon {
  color: white;
  font-size: 12px;
  font-weight: bold;
}

.option-label {
  font-size: 14px;
  color: #333;
}

.option-item:hover .checkbox {
  border-color: #FFD966;
}
</style>
