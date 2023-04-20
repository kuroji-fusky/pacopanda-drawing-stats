<script setup lang="ts">
const { page } = useContent()

usePageMeta({
	title: "Home",
	description: page.value.description,
})
</script>

<template>
	<ContentDoc />
</template>
