<script setup lang="ts">
import { onMounted } from "vue"

onMounted(() => {
	const bodyClasses: string[] = ["dark:bg-green-950", "dark:text-green-50"]
	const $body = document.body
	$body.classList.add(...bodyClasses)
})
</script>

<template>
	<AppHeader />
	<main>
		<div
			id="error-overlay"
			class="bg-green-800 mx-auto w-4/5 px-6 py-5 rounded-md mt-5"
		>
			<h2 class="text-2xl">Error: couldn't connect to Redis database source</h2>
			<p>
				Check if you have <code>REDIS_KEY</code> added on the
				<code>.env</code> file, if not, generate one with:
			</p>
			<code class="block py-3 px-5 bg-neutral-900 rounded-md"
				>python paco.py --redis
			</code>
		</div>
	</main>
</template>

<style lang="scss">
#error-overlay *:not(:last-child) {
	@apply pb-2.5;
}
</style>
