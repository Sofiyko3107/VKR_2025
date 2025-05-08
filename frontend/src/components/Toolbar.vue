<script setup>
import SvgIcon from '@jamescoyle/vue-icon';
import { mdiCartOutline, mdiAccountCircleOutline } from '@mdi/js';
import logoUrl from '@/assets/logo.png'
</script>

<template>
    <div class="core">
        <div class="wrapper">
            <div class="nav">
                <img 
                    :src="logoUrl" 
                    alt="Название компании" 
                    width="150" 
                    height="50" 
                    class="site-logo"
                >
                <div class="wrapper-nav-list">
                    <div>каталог</div>
                    <div>услуги</div>
                    <div>о компании</div>
                    <div>контакты</div>
                </div>
            </div>
            <div class="wrapper-logo">
                <SvgIcon type="mdi" :path="mdiCartOutline"/>
                <SvgIcon type="mdi" :path="mdiAccountCircleOutline"/>
            </div>
        </div>
    </div>


</template>

<style scoped>
.core {
    background-color: white;
    width: 100%;
}

.wrapper {
    display: flex;
    flex-direction: row;
    margin: auto;
    width: 86%;
    height: 71px;
    justify-content: space-between;
}

.wrapper-nav-list {
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 24px;
}



.nav {
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