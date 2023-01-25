<template>
	<nuxt-link
		:to="props.href"
		role="listitem"
		:target="!props.external ? '' : '_blank'"
		:rel="!props.external ? '' : 'noopenner noreferrer'"
		class="flex gap-x-3 hover:text-green-500"
	>
		<slot />
	</nuxt-link>
</template>

<script setup lang="ts">
interface FooterLinkProps {
	href: string
	external?: boolean
}

const props = defineProps<FooterLinkProps>()
</script>
