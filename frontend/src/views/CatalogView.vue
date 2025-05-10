<script setup>
import SvgIcon from '@jamescoyle/vue-icon';
import { mdiRadioboxBlank, mdiCheckboxMarkedCircle } from '@mdi/js';
import Button from "../components/Button.vue"
import { ref } from 'vue'
import RadioButton from "@/components/RadioButton.vue";
import CardProduct from '@/components/CardProduct.vue';
import TabButton from "../components/TabButton.vue";

const activeTab = ref('profile')    
const gender = ref('male'); // 'male' или 'female'
</script>

<template>
    <div class="tabs-container">
      <TabButton :active="activeTab === 'orders'" @click="activeTab = 'orders'">
      ЖБИ
      </TabButton>
      <TabButton :active="activeTab === 'profile'" @click="activeTab = 'profile'">
      Бетон
      </TabButton>
    </div>
    <div class="catalog-wrapper">
      
      <CardProduct
        title="M300"
        :characteristics="['B22,5', 'F200', 'W4']"
        price="4 500 ₽/м³"
        button-text="Заказать"
      />
      <CardProduct
        title="M300"
        :characteristics="['B22,5', 'F200', 'W4']"
        price="4 500 ₽/м³"
        button-text="Заказать"
      />
      <CardProduct
        title="M300"
        :characteristics="['B22,5', 'F200', 'W4']"
        price="4 500 ₽/м³"
        button-text="Заказать"
      />
      <CardProduct
        title="M300"
        :characteristics="['B22,5', 'F200', 'W4']"
        price="4 500 ₽/м³"
        button-text="Заказать"
      />
    </div>
      
</template>
      
  
  <style>

.catalog-wrapper {
    display: grid;
    grid-template-columns: repeat(4, 1fr); /* 4 равные колонки */
    gap: 20px;
    margin-top: 48px;
    grid-template-columns: repeat(4, 1fr);
}
  </style>
  