import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import Repository from '@/api/authApi.js'

export const useAuthStore = defineStore('auth', () => {
  const user = ref(null)
  const isAuthenticated = ref(false)

  const fetchUserData = async () => {
    try {
      const { data } = await Repository.getUserData();
      console.log(data)
      user.value = data;
      isAuthenticated.value = true;
    } catch (error) {
      console.log('fetch')
      user.value = null;
      isAuthenticated.value = false
    }
  }

  const logout = async () => {
    await Repository.logout()
    user.value = null
    isAuthenticated.value = false
  }

  return { user, isAuthenticated, fetchUserData, logout }

})
