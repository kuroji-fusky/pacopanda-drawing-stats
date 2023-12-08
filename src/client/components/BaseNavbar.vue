<script setup lang="ts">
const navLinks = [
  {
    name: "Browse",
    subitems: [
      { name: "By species", link: "/browse/species" },
      { name: "By character", link: "/browse/character" },
      { name: "By chronological order", link: "/browse/chrono" },
    ],
  },
  { name: "About" },
  { name: "Reports" },
]
</script>

<template>
  <header>
    <div class="px-8 py-3.5 flex items-center justify-between">
      <div>logo</div>
      <nav>
        <NuxtLink v-for="item in navLinks" :to="`/${item.name.toLowerCase()}`">
          <div v-if="item.subitems">
            <span>{{ item.name }}</span>
            <div class="flex flex-col">
              <NuxtLink v-for="subitem in item.subitems" :to="subitem.link">
                {{ subitem.name }}
              </NuxtLink>
            </div>
          </div>
          <span v-else>
            {{ item.name }}
          </span>
        </NuxtLink>
      </nav>
    </div>
  </header>
</template>
