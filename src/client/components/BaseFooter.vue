<script setup lang="ts">
const currentYear = new Date().getFullYear()
const copyright = `© 2021-${currentYear} Kuroji Fusky`
</script>

<template>
  <footer>
    <p>{{ copyright }}</p>
  </footer>
</template>
