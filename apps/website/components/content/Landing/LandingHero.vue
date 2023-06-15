<template>
  <section class="landing-hero-section">
    <article class="grid text-center place-items-center">
      <h1 class="py-6 text-5xl font-bold font-inter">Paco Drawing Stats</h1>
      <p class="w-3/5 text-lg">
        A data visualization project created by
        <span id="kuro-hl">Kuroji Fusky</span> - a website that collects and
        visualizes 1.9k+ drawings from a furry artist and illustrator Panda
        Paco. Made purely out of curiousity.
      </p>
    </article>
    <div class="flex grid-cols-3 gap-4">
      <landing-hero-button text="About this project" />
      <landing-hero-button text="Browse stats" href="/browse" />
      <landing-hero-button text="API" />
    </div>
    <div aria-hidden="true"></div>
  </section>
</template>

<script setup lang="ts"></script>

<style lang="scss">
.landing-hero-section {
  @apply grid place-items-center h-[40rem];
}

#kuro-hl {
  @apply bg-gradient-to-br from-violet-500 to-cyan-500 font-bold bg-clip-text text-transparent;
}
</style>
