<script setup>
import { ref } from "vue"

const props = defineProps({
    inputLabel: String,
    inputPlaceholder: String,
    disabled: {
        type: Boolean,
        default: false
    }

})

</script>
<template>
    <div class="input-wrapper">
        <div class="input-label">{{ inputLabel }}</div>
        <input type="text" :placeholder="inputPlaceholder" :disabled="disabled">
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
input {
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    box-shadow: none;
    height: 64px;
    border: 1px solid #dddddd;
    border-radius: 12px;
    width: 100%;
    margin-bottom: 24px;
}

input::placeholder {
    color: #6C6C6C;
    padding-left: 20px;
    font-size: 20px;
}

input:disabled {
    background-color: #dddddd;
}

</style>