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
    <header class="flex items-center justify-between px-8 py-3.5">
      <NuxtLink to="/">logo</NuxtLink>
      <nav class="flex items-center gap-x-1">
        <button class="rounded-md border border-green-400 px-3 py-2">
          <LucideSearch :size="19" />
        </button>
        <template v-for="item in navLinks">
          <NuxtLink
            v-if="!item.subitems"
            :to="`/${item.name.toLowerCase()}`"
            class="rounded-md px-3 py-2 hover:bg-green-400"
          >
            {{ item.name }}
          </NuxtLink>
          <div v-else class="group relative">
            <NuxtLink
              class="rounded-md px-3 py-2.5 hover:bg-green-400"
              :to="`/${item.name.toLowerCase()}`"
            >
              {{ item.name }}
            </NuxtLink>
            <div
              class="pointer-events-none absolute top-9 z-10 flex w-fit translate-y-1 flex-col rounded-md bg-white py-2 opacity-0 shadow-md transition-all group-hover:pointer-events-auto group-hover:translate-y-0 group-hover:opacity-100"
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
