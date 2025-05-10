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
        <div class="wrapper">
            <img
                    :src="logo1Url"
                    alt="Название компании"
                    width="150"
                    height="50"
                    class="site-logo"
                >


            <div class="wrapper-nav-list">
                <Button text @click="router.push({ name: 'catalog'})">каталог</Button>
                <Button text @click="router.push({ name: 'services'})">услуги</Button>
                <Button text @click="router.push({ name: 'about'})">о компании</Button>
                <Button text @click="router.push({ name: 'contact'})">контакты</Button>
            </div>

            <div class="wrapper-logo">
                <Button icon @click="">
                    <template #icon><SvgIcon type="mdi" :path="mdiCartOutline"/></template>
                </Button>
                <Button icon @click="">
                    <template #icon><SvgIcon type="mdi" :path="mdiAccountCircleOutline"/></template>
                </Button>

            </div>
        </div>
    </div>


</template>

<style scoped>

.wrapper-logo {
    display: flex;
    flex-direction: row;
    gap: 16px;
    align-items: center;

}

.core {
    background-color: white;
    width: 100%;
    border-bottom: 1px solid #DDDDDD;
}

.wrapper {
    display: flex;
    flex-direction: row;
    margin: auto;
    width: 1440px;
    height: 80px;
    margin: auto;
    padding: 0 100px 0 100px;
    justify-content: space-between;
}

.wrapper-nav-list {
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 48px;
    display: flex;
    flex-direction: row;
}




.site-logo {
    max-height: 71px;
    max-width: 117px; /* Для адаптивности */
    height: auto;    /* Сохраняет пропорции */
    width: auto;
    margin-right: 40px
}
</style>
