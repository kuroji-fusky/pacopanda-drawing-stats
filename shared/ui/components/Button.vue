<script setup lang="ts">
defineProps<{ name?: string }>()
</script>

<template>
	<button type="button">
		{{ name }}
	</button>
</template>

<style lang="scss" scoped>
button {
	@apply px-1.5 py-3 rounded-md border-black;
}
</style>
