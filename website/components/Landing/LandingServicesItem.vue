<template>
	<li class="services-item">
		<div :v-html="props.logo"></div>
		<h2>{{ props.name }}</h2>
		<span>
			{{ props.description }}
		</span>
	</li>
</template>

<script setup lang="ts">
interface ServiceItemProps {
	name: string
	description: string
	logo?: any
}

const props = defineProps<ServiceItemProps>()
</script>

<style lang="scss">
.services-item {
	@apply flex flex-col items-center p-6 gap-y-3.5 shadow-xl text-center border border-green-600 rounded-md;

	h2 {
		@apply font-inter font-bold text-2xl;
	}
}
</style>
