<script setup lang="ts">
import { gsap } from "gsap"
import { ScrollTrigger } from "gsap/ScrollTrigger"

gsap.registerEffect(ScrollTrigger)
</script>

<template>
  <div>
    <BaseNavbar />
    <slot />
    <BaseFooter />
  </div>
</template>
