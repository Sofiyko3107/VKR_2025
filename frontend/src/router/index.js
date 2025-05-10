import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MainView from '../views/MainView.vue'
import CatalogView from '@/views/CatalogView.vue'
import AuthModal from "@/components/AuthModal.vue";
import ConfirmeView from "@/views/ConfirmeView.vue";
import ProfileView from "@/views/ProfileView.vue";
import {useAuthStore} from "@/stores/authStore.js";
import Layout from "@/components/Layout.vue";
import ServicesView from "@/views/ServicesView.vue";
import AboutView from "@/views/AboutView.vue";
import ContactView from "@/views/ContactView.vue";
import CartView from "@/views/CartView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'layout',
      component: Layout,
      children: [
        {
          path: '/',
          name: 'main',
          component: MainView
        },
        {
          path: '/catalog',
          name: 'catalog',
          component: CatalogView,
        },
        {
          path: '/services',
          name: 'services',
          component: ServicesView
        },
        {
          path: '/about',
          name: 'about',
          component: AboutView
        },
        {
          path: '/contact',
          name: 'contact',
          component: ContactView
        },
        {
          path: '/confirm-email',
          name: 'confirm',
          component: ConfirmeView
        },
        {
          path: '/card',
          name: 'card',
          component: CartView,
          meta: { requiresAuth: true}
        },
        {
          path: '/profile',
          name: 'profile',
          component: ProfileView,
          meta: { requiresAuth: true },
        },
        {
          path: '/auth',
          name: 'auth',
          component: AuthModal,
          meta: { requiresAuth: false }
        }
      ]
    },
  ],
})

router.beforeEach(async (to, from) => {
  const userStore = useAuthStore()

  if (!userStore.isAuthenticated) {
    await userStore.fetchUserData()
  }

  console.log(to.meta)

  if (!userStore.isAuthenticated && to.meta.requiresAuth) {
    console.log('profile')
    return { name: 'auth' }
  }

  if (userStore.isAuthenticated && to.name === 'auth') {
    return { name: 'main' }
  }

})

export default router
