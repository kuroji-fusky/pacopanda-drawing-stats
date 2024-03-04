<script setup lang="ts">
import { cva, type VariantProps } from "class-variance-authority"

const button = cva("button", {
  variants: {
    variant: {
      primary: "bg-green-100 hover:bg-green-200 text-black",
      secondary: "bg-green-200 hover:bg-green-300 text-black",
      disabled: "bg-gray-400 text-gray-800",
    },
  },
  compoundVariants: [
    {
      variant: "primary",
      class: "primaryMid",
    },
  ],
})

type ButtonProps = VariantProps<typeof button>

withDefaults(defineProps<{ variant: ButtonProps["variant"] }>(), {
  variant: "primary",
})
</script>

<template>
  <button :class="button({ variant })">
    <slot />
  </button>
</template>
