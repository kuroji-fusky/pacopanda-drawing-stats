<template>
	<main>
		<slot />
	</main>
</template>

<script setup lang="ts">
const router = useRoute()

const URL_PATH = `httos://pds.kurofusky.xyz${router.fullPath}`

const props = defineProps<{
	title: string
	description?: string
}>()

useHead({
	title: props.title,
	meta: [
		{ name: "description", content: props.description },
		{ name: "twitter:title", content: props.title },
		{ name: "twitter:description", content: props.description },
		{ name: "twitter:url", content: URL_PATH },
		{ name: "twitter:card", content: "summary_large_card" },
		{ name: "twitter:creator", content: "@kurojifusky" },
		{ property: "og:title", content: props.title },
		{ property: "og:description", content: props.description },
		{ property: "og:type", content: "website" },
		{ property: "og:url", content: URL_PATH },
		{ property: "og:site_name", content: "Paco Drawing Stats" },
	],
	link: [{ rel: "canonical", href: URL_PATH }],
})
</script>
