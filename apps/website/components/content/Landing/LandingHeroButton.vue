<template>
  <nuxt-link :to="props.href ?? '#'" class="hero-button">
    <span class="text-2xl font-bold font-inter">{{ props.text }}</span>
  </nuxt-link>
</template>

<script setup lang="ts">
interface ButtonProps {
  href?: string
  text?: string
  img?: string
}
const props = defineProps<ButtonProps>()
</script>

<style lang="scss">
.hero-button {
  @apply rounded-md px-7 py-5 relative bg-white w-[20vw] h-[9.5rem] transition-shadow;

  &:hover {
    @apply shadow-lg;
  }

  &::before {
    content: "";
    border-radius: inherit;
    background-size: 300%;
    background-position: 0% 0%;
    transition: background 250ms ease;

    @apply -z-10 absolute block -inset-[0.125rem] bg-gradient-to-br from-green-500 via-amber-400 to-lime-500;
  }

  &:hover::before {
    background-position: 100% 50%;
  }
}
</style>
