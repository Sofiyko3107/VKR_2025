<script setup>
defineProps({
  title: {
    type: String,
    required: true
  },
  characteristics: {
    type: Array,
    default: () => []
  },
  price: {
    type: String,
    required: true
  },
  buttonText: {
    type: String,
    default: 'Заказать'
  }
})
</script>

<template>
  <div class="product-card">
    <h3 class="product-title">{{ title }}</h3>
    
    <ul class="characteristics-list">
      <li 
        v-for="(item, index) in characteristics" 
        :key="index"
        class="characteristic-item"
      >
        {{ item }}
      </li>
    </ul>
    
    <div class="price">{{ price }}</div>
    
    <button class="order-button">
      {{ buttonText }}
    </button>
  </div>
</template>

<style scoped>
.product-card {
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 20px;
  max-width: 250px;
  text-align: center;
  font-family: Arial, sans-serif;
}

.product-title {
  font-size: 22px;
  font-weight: bold;
  margin-bottom: 15px;
  color: #333;
}

.characteristics-list {
  list-style: none;
  padding: 0;
  margin: 0 0 15px 0;
  text-align: left;
}

.characteristic-item {
  font-size: 16px;
  color: #555;
  margin-bottom: 8px;
  position: relative;
  padding-left: 15px;
}

.characteristic-item::before {
  content: "•";
  position: absolute;
  left: 0;
  color: #888;
}

.price {
  font-size: 20px;
  font-weight: bold;
  color: #222;
  margin: 20px 0;
}

.order-button {
  background-color: #FFC633;
  color: #1E1E1E;
  border: none;
  border-radius: 62px;
  padding: 12px 24px;
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
  width: 100%;
  transition: background-color 0.2s;
}

.order-button:hover {
  background-color: #FFD966;
}
</style>