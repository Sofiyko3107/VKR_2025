<script setup>
import InputGroup from "../components/InputGroup.vue"
import SvgIcon from '@jamescoyle/vue-icon';
import { mdiRadioboxBlank, mdiCheckboxMarkedCircle } from '@mdi/js';
import Button from "../components/Button.vue"
import TabButton from "../components/TabButton.vue"
import { ref } from 'vue'
import RadioButton from "@/components/RadioButton.vue";

const activeTab = ref('profile')    
const gender = ref('male'); // 'male' или 'female'
</script>

<template>
    <div class="screen">
        <div class="tabs-container">
            <TabButton :active="activeTab === 'orders'" @click="activeTab = 'orders'">
             Мои заказы
            </TabButton>
            <TabButton :active="activeTab === 'profile'" @click="activeTab = 'profile'">
             Профиль
            </TabButton>
        </div>
        <div class="H2">
            Персональная информация
        </div>
        <div class="profile-wrapper">
            
            <InputGroup
                input-label="Имя"
                inputPlaceholder="Иван"
            ></InputGroup>
            <InputGroup
                input-label="Фамилия"
                inputPlaceholder="Иванов"
            ></InputGroup>
            <InputGroup
                input-label="Отчество"
                inputPlaceholder="Иванович"
            ></InputGroup>
            <InputGroup
                input-label="Дата рождения"
                inputPlaceholder="01.01.2000"
            ></InputGroup>
            <InputGroup
                input-label="Фамилия"
                inputPlaceholder="Иванов"
            ></InputGroup>
            <div class="wrapper-logo">
                <div class="T2">
                    Пол
                </div>
                <div class="icon-menu">
                    <RadioButton 
                        v-model="gender"
                        value="female"
                        label="Женский"
                        name="gender"
                    />
                    <RadioButton 
                        v-model="gender"
                        value="male"
                        label="Мужской"
                        name="gender"
                    />
                    
                </div>  
            </div>
            <div class="double-column-input">
                <InputGroup
                input-label="Электронная почта"
                inputPlaceholder="user@example.com"
            ></InputGroup>
            </div>
            <div class="button-location buttons-column">
                <!-- Основное использование -->
                <Button @click="">Сохранить</Button>
                <Button alter @click="">Выйти</Button>
            </div>
        </div>
        <div class="H2 address">
            Адреса доставки
        </div>
        <div class="address-line">
            <div class="T1">
                У вас ещё нет добавленных адресов
            </div>
            <div class="button-location buttons-column">
                <Button alter @click="">Добавить</Button>
            </div>
            
        </div>
        
        <input style="width: 100px; height: 20px;" type="file"></input>
    </div>
    
        
    


</template>



<style scoped>

.tabs-container{
    display: flex;
    width: 100%;
}

.tabs-container > * {
    flex: 1; /* чтобы кнопки занимали равное пространство */
}

.address-line{
    display: flex;
    justify-content: space-between; /* Растягивает элементы по краям */
    align-items: center; /* Выравнивает по вертикали */
    margin-top: 16px; /* Отступ от заголовка "Адреса доставки" */

}

.address {
    margin-top: 52px;
    margin-bottom: 40px;

}

.buttons-column {
    display: flex;

    gap: 20px; /* Отступ между кнопками */
    margin-top: 32px;
}


.button-location {
    margin-top: 32px;
}

.double-column-input {
    grid-column: span 2; /* Занимает 2 колонки */
}

.icon-item {
    display: flex;
    align-items: center;
    cursor: pointer;
    gap: 16px;
   
}

.icon-menu {
    
    display: flex;
    flex-direction: column;
    gap: 12px;
}

.T2 {
    font-size: 16px;
    color: #757575;
    width: 100%;
    padding-left: 21px;
    margin-bottom: 8px;

}

.T1{
    font-size: 20px;
    height: 24px;
    padding-bottom: 3px;
    line-height: 1.2;
}
.H2 {
    font-size: 40px;
}

.profile-wrapper {
    display: grid;
    grid-template-columns: repeat(3, 1fr); /* 3 равные колонки */
    gap: 0 20px;
    margin-top: 48px;
}
</style>