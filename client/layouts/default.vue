<script setup lang="ts">
// import { gsap } from "gsap"
// import { ScrollTrigger } from "gsap/ScrollTrigger"

// gsap.registerEffect(ScrollTrigger)
</script>

<template>
  <BaseNavbar />
  <div class="px-5 lg:px-8">
    <slot />
  </div>
  <BaseFooter />
</template>
