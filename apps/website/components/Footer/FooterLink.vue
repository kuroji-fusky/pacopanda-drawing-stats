<template>
	<NuxtLink
		:to="props.href"
		role="listitem"
		:target="!props.external ? '' : '_blank'"
		:rel="!props.external ? '' : 'noopenner noreferrer'"
		class="flex gap-x-3 hover:text-green-500 items-center"
	>
		<component :is="icon" size="25" class="w-5 text-black" />
		<slot />
	</NuxtLink>
</template>

<script setup lang="ts">
interface FooterLinkProps {
	icon: VNode
	href: string
	external?: boolean
}

const props = defineProps<FooterLinkProps>()
</script>
