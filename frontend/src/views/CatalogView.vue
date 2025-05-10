<script setup>
import SvgIcon from '@jamescoyle/vue-icon';
import { mdiRadioboxBlank, mdiCheckboxMarkedCircle } from '@mdi/js';
import Button from "../components/Button.vue"
import { ref } from 'vue'
import RadioButton from "@/components/RadioButton.vue";
import CardProduct from '@/components/CardProduct.vue';
import TabButton from "../components/TabButton.vue";
import Checkbox from '@/components/CheckBox.vue';





const isChecked = ref(false);
const isAgreed = ref(false);
const isDisabled = ref(true);
const selected = ref([])

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
      
      <div>
        <div class="text-Catalog">
          Каталог
        </div>
        <div class="text-sort">
          Cортировка
        </div>
        <div>
                    <RadioButton 
                        v-model="cost"
                        value="expensive"
                        label="Сначала дороже"
                    
                    />
                    <RadioButton 
                        v-model="cost"
                        value="cheap"
                        label="Сначала дешевле"
                
                    />
                    
        </div>
        <div>
          <Checkbox v-model:selected="selected" />

        </div>
      </div>
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

.text-sort {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 20px;
}

.text-Catalog {
    font-size: 48px;
    margin-bottom: 28px;
}

.catalog-wrapper {
    display: grid;
    grid-template-columns: repeat(4, 1fr); /* 4 равные колонки */
    gap: 20px;
    margin-top: 48px;
    grid-template-columns: repeat(4, 1fr);
}
  </style>
  