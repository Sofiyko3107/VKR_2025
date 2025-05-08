<script setup>
    const props = defineProps({
      active: {
        type: Boolean,
        default: false
      },
      disabled: {
        type: Boolean,
        default: false
      }
    })

    const emit = defineEmits(['click'])

    const handleClick = () => {
      if (!props.disabled) {
        emit('click')
      }
    }
    </script>

    <template>
      <button
        :class="['tab-button', { active }]"
        :disabled="disabled"
        @click="handleClick"
      >
        <slot></slot>
      </button>
    </template>

    <style scoped>
    .tab-button {
      border: none;
      padding: 12px 24px;
      border-bottom: 1px solid #dddddd;
      background: none;
      font-size: 20px;
      font-weight: 500;
      cursor: pointer;
      color: #6C6C6C;
      position: relative;
      transition: all 0.2s;
    }

    .active {
      color: #1E1E1E;
      border-bottom: 1px solid #1E1E1E;
      font-weight: 600;
    }

    .tab-button .active::after {
      content: '';
      position: absolute;
      bottom: -8px;
      left: 0;
      width: 100%;
      height: 3px;
      background-color: #FFC633;
      border-radius: 3px;
    }

    .tab-button:disabled {
      color: #DDDDDD;
      cursor: not-allowed;
    }

    .tab-button:not(:disabled):hover {
      color: #1E1E1E;
    }
    </style>
