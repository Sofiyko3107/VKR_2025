<script setup>

import StepProgress from "@/components/StepProgress.vue";
import {ref, watch} from "vue";
import Step1 from "@/components/AuthComponents/RegisterSteps/Step1.vue";
import Step2 from "@/components/AuthComponents/RegisterSteps/Step2.vue";
import Step3 from "@/components/AuthComponents/RegisterSteps/Step3.vue";
import Step4 from "@/components/AuthComponents/RegisterSteps/Step4.vue";
import RepositoryHelper from "@/api/registerHelperApi.js"
import {useRegisterStepsStore} from "@/stores/registerStepStore.js";

const currentStep = ref(1);
const steps = [Step1, Step2, Step3, Step4];
const store = useRegisterStepsStore()

const nextStep = async () => {
  switch (currentStep.value) {
    case 1:
      const { data } = await RepositoryHelper.send_confirmation_message({ email: store.getEmail })
      console.log(data);
      break;
    case 2:
      console.log('2');
      break;
    case 3:
      console.log('3');
      break;
    case 4:
      console.log('4');
      break;
    default:
      return
  }

  if (currentStep.value < steps.length) {
    currentStep.value++;
  }
};

const prevStep = () => {
  if (currentStep.value > 1) {
    currentStep.value--;
  }
};

</script>

<template>
  <div class="reg-form">
    <div class="step-progress">
      <step-progress :current-step="currentStep" :steps="steps.length"></step-progress>
    </div>
    <div class="steps">
      <component
        :is="steps[currentStep - 1]"
        @next="nextStep"
        @prev="prevStep"
      />
    </div>
  </div>

</template>

<style scoped>
.reg-form {
  display: block;
  width: 414px;
  flex-grow: 1;
  margin: 50px auto 0 auto;
}
</style>
