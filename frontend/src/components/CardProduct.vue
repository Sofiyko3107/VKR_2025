<script setup>
import Button from "@/components/Button.vue";
import {computed} from "vue";

const props = defineProps({
  product: {
    type: Object,
    default: {}
  }
})


const fullImageUrl = computed(() => {
  if (!props.product.image) return null;

  const baseUrl = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

  const imagePath = props.product.image.startsWith('/')
    ? props.product.image.substring(1)
    : props.product.image;

  return `${baseUrl}/${imagePath}`;
});

</script>

<template>
  <div class="card-wrapper" :class="[{ 'card-border': (product.category.name === 'Бетон') }]">
    <div v-if="product.category.name !== 'Бетон'">
      <img
        v-if="product.image"
        :src="fullImageUrl"
        :alt="product.name"
        class="product-image"
      >
    </div>
    <div class="card-header T1">{{ product.name }}</div>
    <div>
      <div class="card-specs" v-for="spec in product.specifications" :key="spec.id">
        <div>
          {{ spec.name }}: {{ spec.description }}
        </div>
      </div>
    </div>
    <div class="card-price T1">{{ product.price }} ₽</div>
    <Button button-width="100%">Заказать</Button>
  </div>
</template>

<style scoped>
.card-wrapper {
  width: 300px;
  border-radius: 20px;
  padding: 16px 8px
}
.card-border {
  border: 1px solid #c4c4c4;
}

.card-header {
  margin-bottom: 20px;
}
.card-specs > * {
  margin-bottom: 12px;
  margin-left: 8px;
}
.card-price {
  margin-top: 12px;
  margin-bottom: 16px;
}

.product-image {
  width: 100%;
  height: 200px;
  object-fit: contain;
  border-radius: 8px;
  background-color: #f5f5f5;
}
</style>
