<script setup lang="ts">
import { gsap } from "gsap"
import { ScrollTrigger } from "gsap/ScrollTrigger"

gsap.registerEffect(ScrollTrigger)
</script>

<template>
  <div class="font-body text-sm">
    <BaseNavbar />
    <slot />
    <BaseFooter />
  </div>
</template>
