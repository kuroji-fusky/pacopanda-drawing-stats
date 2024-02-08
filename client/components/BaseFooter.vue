<script setup lang="ts">
const currentYear = new Date().getFullYear()
</script>

<template>
  <div class="mx-auto max-w-screen-2xl">
    <footer class="flex items-center justify-between px-8 py-3.5">
      <span>
        {{
          `Copyright © 2021-${currentYear} Kuroji Fusky, licensed under the`
        }}
        <NuxtLink
          to="https://opensource.org/license/apache-2-0/"
          :external="true"
          >Apache License, Version 2.0.</NuxtLink
        >
      </span>
      <div>github stuff and socials</div>
    </footer>
  </div>
</template>
