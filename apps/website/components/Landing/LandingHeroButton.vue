<template>
	<nuxt-link :to="props.href ?? '#'" class="hero-button">
		<span class="text-2xl font-bold font-inter">{{ props.text }}</span>
	</nuxt-link>
</template>

<script setup lang="ts">
interface ButtonProps {
	href?: string
	text?: string
	img?: string
}
const props = defineProps<ButtonProps>()
</script>

<style lang="scss" scoped>
.hero-button {
	@apply rounded-md px-7 py-5 relative bg-white;

	&::before {
		content: "";
		border-radius: inherit;

		@apply -z-10 absolute block -inset-[0.125rem] bg-gradient-to-br from-green-500 to-amber-300;
	}
}
</style>
