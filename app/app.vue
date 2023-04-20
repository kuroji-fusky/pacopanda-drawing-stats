<script setup lang="ts">
const SITE_NAME = "Paco Drawing Stats"

useHead({
	titleTemplate: (titleChunk) =>
		titleChunk === SITE_NAME ? titleChunk : `${titleChunk} - ${SITE_NAME}`,
})
</script>

<template>
	<NuxtLayout>
		<NuxtPage />
	</NuxtLayout>
</template>

<style lang="scss"></style>
