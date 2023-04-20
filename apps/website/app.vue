<script setup lang="ts">
const SITE_NAME = "Paco Drawing Stats"

useHead({
	titleTemplate: (titleChunk) =>
		titleChunk === SITE_NAME ? titleChunk : `${titleChunk} - ${SITE_NAME}`,
})
</script>

<template>
	<div id="__paco">
		<TheBaseNavbar />
		<NuxtPage />
		<TheBaseFooter />
	</div>
</template>

<style lang="scss"></style>
