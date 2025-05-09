<script setup>
import Repository from '@/api/registerHelperApi.js'
import {onMounted, ref} from "vue";
import {useRoute} from "vue-router";

const route = useRoute()

const message = ref('Ожидание подтверждения')

const send_confirmation = async () => {

  const token = route.query.token
  console.log(token)
  if (!token) return

  const { data } = await Repository.verify_email(route.query.token)
}

onMounted(() => {
  send_confirmation()
});

</script>

<template>
<div class="T1">{{ message }}</div>
</template>

<style scoped>

</style>
