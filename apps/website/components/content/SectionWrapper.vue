<script setup lang="ts">
defineProps<{ heading?: string }>()
</script>

<template>
	<div>
		<h2>{{ heading }}</h2>
		<slot />
	</div>
</template>
