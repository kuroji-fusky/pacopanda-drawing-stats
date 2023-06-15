<template>
  <PageContainer title="Browse" class="px-12">
    <div class="banner-notice">
      <p>
        Keep in mind that most of the data here might be out of date or some
        shit; I'm running this project with limited resources.
      </p>
      <p>
        For any questions, visit
        <NuxtLink to="about#faq" class="link-underline">FAQs</NuxtLink>
      </p>
    </div>
    <div class="grid my-8 gap-y-5">
      <ShelfCarousel heading="Artwork" />
      <ShelfCarousel heading="Characters" />
    </div>
  </PageContainer>
</template>

<script setup lang="ts"></script>
