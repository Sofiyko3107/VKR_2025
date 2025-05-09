import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MainView from '../views/MainView.vue'
import CatalogView from '@/views/CatalogView.vue'
import AuthModal from "@/components/AuthModal.vue";
import ConfirmeView from "@/views/ConfirmeView.vue";
import ProfileView from "@/views/ProfileView.vue";
import {useAuthStore} from "@/stores/authStore.js";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainView,
      children: [
        {
          path: '/auth',
          name: 'auth',
          component: AuthModal,
          meta: { requiresAuth: false }
        }
      ]
    },
    {
      path: '/catalog',
      name: 'catalog',
      component: CatalogView,
    },
    {
      path: '/confirm-email',
      name: 'confirm',
      component: ConfirmeView
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView,
      meta: { requiresAuth: true },
    }
  ],
})

router.beforeEach(async (to, from) => {
  const userStore = useAuthStore()

  if (!userStore.isAuthenticated) {
    await userStore.fetchUserData()
  }

  if (!userStore.isAuthenticated && to.name !== 'auth') {
    console.log('profile')
    return { name: 'auth' }
  }

  if (userStore.isAuthenticated && to.name === 'auth') {
    return { name: 'main' }
  }


})

export default router
