<script setup lang="ts">
const currentYear = new Date().getFullYear()

const socials = [
  { name: "GitHub", icon: "fa6-brands:github" },
  { name: "Mastodon", icon: "fa6-brands:mastodon" },
]
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
          class="hlink"
          >Apache- 2.0</NuxtLink
        >
        {{ ` license.` }}
      </span>
      <div>
        <NuxtLink v-for="(item, index) in socials" :key="index">
          <Icon :name="item.icon" />
        </NuxtLink>
      </div>
    </footer>
  </div>
</template>
