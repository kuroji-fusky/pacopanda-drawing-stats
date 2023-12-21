<script setup lang="ts">
const currentYear = new Date().getFullYear()
const copyright = `© 2021-${currentYear} Kuroji Fusky, licensed under MIT`
</script>

<template>
  <div class="mx-auto max-w-screen-2xl">
    <footer class="px-8 py-3.5 flex items-center justify-between">
      <span>{{ copyright }}</span>
      <div>github stuff and socials</div>
    </footer>
  </div>
</template>
