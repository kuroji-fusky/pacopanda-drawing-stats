<template>
  <div class="shelf-container">
    <div
      class="shelf-heading"
      :aria-label="`Shelf container for ${props.heading}`"
    >
      <h2>{{ props.heading }}</h2>
      <NuxtLink to="#" role="button">See more</NuxtLink>
    </div>
    <div id="carousel">Carousel items here</div>
  </div>
</template>

<script setup lang="ts">
interface CarouselProps {
  heading?: string
  items?: Array<{
    name: string
    species: string
  }> &
    never[]
}

const props = defineProps<CarouselProps>()
</script>

<style lang="scss" scoped>
.shelf-heading {
  @apply flex items-center gap-x-3 mb-3;

  h2 {
    @apply font-inter text-3xl font-bold;
  }
}
.shelf-carousel {
}
</style>
