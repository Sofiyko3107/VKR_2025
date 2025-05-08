import axios from 'axios'

// Создаем экземпляр Axios с базовыми настройками
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000/api',
  timeout: 10000,
  withCredentials: true,
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  }
})

// Request Interceptor - обработка ВСЕХ исходящих запросов
api.interceptors.request.use(
  (config) => {
    // Добавляем токен авторизации (если есть)
    const token = localStorage.getItem('authToken')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }

    // Логируем запрос (только в dev-режиме)
    if (import.meta.env.DEV) {
      console.log('Отправка запроса:', config.method?.toUpperCase(), config.url)
    }

    return config
  },
  (error) => {
    // Обработка ошибки при формировании запроса
    console.error('Ошибка в запросе:', error)
    return Promise.reject(error)
  }
)

// Response Interceptor - обработка ВСЕХ входящих ответов
api.interceptors.response.use(
  (response) => {
    // Логируем успешный ответ
    if (import.meta.env.DEV) {
      console.log('Успешный ответ:', response.config.url, response.data)
    }
    return response
  },
  (error) => {
    // Обработка ошибок от сервера
    if (error.response) {
      switch (error.response.status) {
        case 401:
          // Если токен протух или невалидный
          console.error('Ошибка 401: Не авторизован')
          // Можно перенаправить на страницу логина
          // router.push('/login')
          break
        case 403:
          console.error('Ошибка 403: Доступ запрещен')
          break
        case 404:
          console.error('Ошибка 404: Ресурс не найден')
          break
        case 500:
          console.error('Ошибка 500: Ошибка сервера')
          break
        default:
          console.error('Неизвестная ошибка:', error.response.status)
      }
    } else if (error.request) {
      // Запрос был сделан, но ответ не получен
      console.error('Нет ответа от сервера:', error.request)
    } else {
      // Ошибка при формировании запроса
      console.error('Ошибка:', error.message)
    }

    return Promise.reject(error)
  }
)

export default api
