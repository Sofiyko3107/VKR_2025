<script setup>
import SvgIcon from '@jamescoyle/vue-icon';
import { mdiCartOutline, mdiAccountCircleOutline } from '@mdi/js';
import logo1Url from '@/assets/logo1.png'
import Button from "./Button.vue"
import {useRouter} from "vue-router";

const router = useRouter();

</script>

<template>
    <div class="core">
        <div class="wrapper-toolbar">
          <div class="site-logo">
            <img
              :src="logo1Url"
              alt="Название компании"
            >
          </div>
          <div class="wrapper-nav-list">
            <Button text @click="router.push({ name: 'catalog'})">каталог</Button>
            <Button text @click="router.push({ name: 'services'})">услуги</Button>
            <Button text @click="router.push({ name: 'about'})">о компании</Button>
            <Button text @click="router.push({ name: 'contact'})">контакты</Button>
          </div>
          <div class="wrapper-logo">
            <Button icon @click="router.push({ name: 'cart'})">
              <template #icon><SvgIcon type="mdi" :path="mdiCartOutline"/></template>
            </Button>
            <Button icon @click="router.push({ name: 'profile'})">
              <template #icon><SvgIcon type="mdi" :path="mdiAccountCircleOutline"/></template>
            </Button>
          </div>
        </div>
    </div>


</template>

<style scoped>
.core {
    background-color: white;
    width: 100%;
    border-bottom: 1px solid #DDDDDD;
}
.wrapper-toolbar {
  width: 1440px;
  height: 80px;
  margin: auto;
  padding: 0 100px 0 100px;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;

}
.site-logo {
  width: 106px;
  height: 64px;
}
.wrapper-nav-list {
  display: flex;
  flex-direction: row;
  gap: 48px
}
.wrapper-logo {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  width: 62px;
  height: 24px;
}

</style>
