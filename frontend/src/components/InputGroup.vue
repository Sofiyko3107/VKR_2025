<script setup>
import { ref } from "vue"

const model = defineModel();

const props = defineProps({
    inputLabel: String,
    inputPlaceholder: String,
    disabled: {
        type: Boolean,
        default: false
    },
    withIcon: {
        type: Boolean,
        default: false
    },
    passwordInput: {
    type: Boolean,
    default: false
  }
})
</script>

<template>
    <div class="input-wrapper">
        <div class="input-label">{{ inputLabel }}</div>
        <div class="input-container">
            <slot v-if="withIcon" name="icon"></slot>
            <input
                v-model="model"
                :type="passwordInput ? 'password' : 'text'"
                :placeholder="inputPlaceholder"
                :disabled="disabled"
                :class="['custom-input', { 'with-icon': withIcon }]"
            >
        </div>
    </div>
</template>

<style scoped>
.input-wrapper {
    min-width: 400px;
}

.input-label {
    font-size: 16px;
    color: #757575;
    width: 100%;
    padding-left: 21px;
    margin-bottom: 8px;
}

.input-container {
    position: relative;
    display: flex;
    align-items: center;
    margin-bottom: 24px;
}

.custom-input {
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    box-shadow: none;
    height: 64px;
    border: 1px solid #dddddd;
    border-radius: 12px;
    width: 100%;
    padding-left: 20px;
    font-size: 20px;
}

.custom-input.with-icon {
    padding-left: 60px;
}

.custom-input::placeholder {
    color: #6C6C6C;
}

.custom-input:disabled {
    background-color: #dddddd;
}

/* Стили для иконки только когда она есть */
.input-container ::v-slotted(svg) {
    position: absolute;
    left: 20px;
    z-index: 2;
    width: 24px;
    height: 24px;
    color: #A9A9A9;
}
</style>
