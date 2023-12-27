<script setup lang="ts">
const navLinks = [
  {
    name: "Browse",
    subitems: [
      { name: "By species", link: "/browse?filter=species" },
      { name: "By character", link: "/browse?filter=characters" },
      { name: "By chronological order", link: "/browse?filter=chronological" }
    ]
  },
  { name: "About" }
]
</script>

<template>
  <div class="sticky top-0 z-10 mx-auto max-w-screen-2xl">
    <header class="px-8 py-3.5 flex items-center justify-between">
      <NuxtLink to="/">logo</NuxtLink>
      <nav class="flex items-center gap-x-1">
        <button class="px-3 py-2 rounded-md border border-green-400">
          <LucideSearch :size="19" />
        </button>
        <template v-for="item in navLinks">
          <NuxtLink
            v-if="!item.subitems"
            :to="`/${item.name.toLowerCase()}`"
            class="px-3 py-2 hover:bg-green-400 rounded-md"
          >
            {{ item.name }}
          </NuxtLink>
          <div v-else class="relative group">
            <NuxtLink
              class="px-3 py-2.5 hover:bg-green-400 rounded-md"
              :to="`/${item.name.toLowerCase()}`"
            >
              {{ item.name }}
            </NuxtLink>
            <div
              class="bg-white absolute z-10 top-9 flex flex-col w-fit shadow-md py-2 rounded-md opacity-0 transition-all group-hover:opacity-100 pointer-events-none group-hover:pointer-events-auto translate-y-1 group-hover:translate-y-0"
            >
              <NuxtLink
                v-for="subitem in navLinks[0].subitems"
                :to="subitem.link"
                class="whitespace-nowrap px-3 py-1 hover:bg-green-300"
              >
                {{ subitem.name }}
              </NuxtLink>
            </div>
          </div>
        </template>
      </nav>
    </header>
  </div>
</template>
