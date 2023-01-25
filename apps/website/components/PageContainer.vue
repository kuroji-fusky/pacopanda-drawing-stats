<template>
	<main :data-wrap-contents="props.contentWrap">
		<slot />
	</main>
</template>

<script setup lang="ts">
const router = useRoute()

const URL_PATH = `httos://pds.kurofusky.xyz${router.fullPath}`

const props = defineProps<{
	title: string
	description?: string
	contentWrap?: boolean
}>()

const SITE_TITLE = `${props.title} | Paco Drawing Stats`

useHead({
	title: SITE_TITLE,
	meta: [
		{ name: "description", content: props.description },
		{ name: "twitter:title", content: SITE_TITLE },
		{ name: "twitter:description", content: props.description },
		{ name: "twitter:url", content: URL_PATH },
		{ name: "twitter:card", content: "summary_large_card" },
		{ name: "twitter:creator", content: "@kurojifusky" },
		{ property: "og:title", content: SITE_TITLE },
		{ property: "og:description", content: props.description },
		{ property: "og:type", content: "website" },
		{ property: "og:url", content: URL_PATH },
		{ property: "og:site_name", content: "Paco Drawing Stats" }
	],
	link: [{ rel: "canonical", href: URL_PATH }]
})
</script>
