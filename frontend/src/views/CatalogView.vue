<script setup>
import SvgIcon from '@jamescoyle/vue-icon';
import { mdiRadioboxBlank, mdiCheckboxMarkedCircle } from '@mdi/js';
import Button from "../components/Button.vue"
import {computed, onMounted, ref, watch} from 'vue'
import RadioButton from "@/components/RadioButton.vue";
import CardProduct from '@/components/CardProduct.vue';
import TabButton from "../components/TabButton.vue";
import Checkbox from '@/components/CheckBox.vue';
import Repository from '@/api/catalogApi.js'


const isChecked = ref(false);
const isAgreed = ref(false);
const isDisabled = ref(true);
const selected = ref([]);
const activeTab = ref('');
const categories = ref([])
const products = ref([])
const selectedProducts = ref([])

const loadCategory = async () => {
  const { data } = await Repository.getCategory();
  categories.value = data
  activeTab.value = categories.value[0].name
  console.log(categories.value)
}

const loadData = async (category_id) => {
  const { data } = await Repository.getProductCategory(category_id)
  products.value = data;
}

const productChecked = computed(() => {
  return products.value.map((p) => p.name)
})

onMounted(() => {
  loadCategory()
})

watch(activeTab, (newVal) => {
  loadData(categories.value.find((element) => element.name === newVal).id);
})

</script>

<template>
  <div class="tabs-container">
    <div v-for="c in categories" :key="c.id">
      <TabButton :active="activeTab === c.name" @click="activeTab = c.name" >{{ c.name }}</TabButton>
    </div>
  </div>
  <div class="catalog-wrapper">
    <div class="catalog-sidebar">
      <div class="H2">Каталог</div>
      <div>
        <div>Товары</div>
        <Checkbox :options="productChecked" :selected="selectedProducts" @update:selected="(selected) => selectedProducts = selected"></Checkbox>
        <div>Сортировка</div>
      </div>
    </div>
    <div class="catalog-products">
      <span v-for="product in products" :key="product.id">
        <CardProduct :product="product" />
      </span>
    </div>
  </div>
</template>

<style scoped>
.catalog-wrapper {
  display: flex;
  flex-direction: row;
}
.catalog-sidebar {
  width: 300px;
}
.catalog-products {
  margin-top: 30px;
  display: flex;
  flex-grow: 1;
  flex-wrap: wrap;
  gap: 12px;
}
</style>
