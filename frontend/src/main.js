import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import axios from "@/plugins/axios/index.js";

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(axios, { baseUrl: 'http://localhost:8000'})


app.mount('#app')
