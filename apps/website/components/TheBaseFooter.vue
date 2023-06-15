<script setup lang="ts">
import { IconGithub } from "@iconify-prerendered/vue-fa6-brands"
import {
  IconGrip,
  IconAsterisk,
  IconCode,
  IconArrowUpRightFromSquare,
} from "@iconify-prerendered/vue-fa6-solid"

const year = new Date().getFullYear()
const COPYRIGHT = `Copyright © 2021-${year} by Kuroji Fusky; its entire source code licensed under`
</script>

<template>
  <footer>
    <div id="wrapper">
      <div class="link-wrapper">
        <div
          role="list"
          class="flex flex-col flex-shrink-0 w-4/12 pr-5 gap-y-4"
        >
          <FooterLink href="/about/how-i-gather-data" :icon="IconAsterisk">
            <span>How I gather and parse data</span>
          </FooterLink>
          <FooterLink href="/api-docs" :icon="IconCode">
            <span
              >Paco Stats API
              <span
                class="text-black relative text-xs left-1 bottom-0.5 px-1 py-0.5 bg-red-300 rounded-sm"
                >WIP</span
              ></span
            >
          </FooterLink>
          <hr class="border border-stone-300" />
          <FooterLink
            external
            href="https://github.com/kuroji-fusky/pacopanda-drawing-stats"
            :icon="IconGithub"
          >
            <span>View source code on GitHub</span>
            <IconArrowUpRightFromSquare size="12" />
          </FooterLink>
          <FooterLink
            external
            href="https://kurofusky.xyz/portfolio"
            :icon="IconGrip"
          >
            <span>More passion projects by Kuroji</span>
            <IconArrowUpRightFromSquare size="12" />
          </FooterLink>
        </div>
        <article class="flex flex-col gap-y-2.5 w-full pl-5">
          <h2 class="text-xl font-bold uppercase font-inter">Disclaimer</h2>
          <p>
            This is an ambitious passion project created by an individual; I do
            not own nor claim any of the third-party content from this site -
            neither it is stored from the database whatsoever. Before 2019, he
            stopped licensing his work under Creative Commons on DeviantArt.
          </p>
          <p>
            The artwork(s) presented on this website is primarily for
            informational and analytical purposes.
          </p>
        </article>
      </div>
      <div class="grid py-6 text-center bg-green-100 place-items-center">
        <span>
          {{ COPYRIGHT }}
          <NuxtLink
            class="link-underline"
            to="https://opensource.org/license/gpl-2-0/"
            >GPL-2.0</NuxtLink
          >
        </span>
      </div>
    </div>
  </footer>
</template>

<style lang="scss" scoped>
#wrapper {
  @apply bg-green-50;
}

.link-wrapper {
  @apply flex px-12 py-10 divide-x-2 divide-solid divide-opacity-30 divide-stone-400 max-w-screen-2xl mx-auto;
}
</style>
