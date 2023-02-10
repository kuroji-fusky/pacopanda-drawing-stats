
<template>
	<div
		class="px-10 py-12 mx-10 mt-8 text-xl text-center bg-white shadow-md rounded-xl"
	>
		<div class="mb-6 font-bold text-red-600">
			<code>REDIS_KEY</code> or <code>.env</code> file not detected.
		</div>
		Running this dashboard will require the
		<code class="il-code-block">REDIS_KEY</code> in the
		<code class="il-code-block">.env</code>
		file.
	</div>
</template>

<style lang="scss">
.il-code-block {
	@apply p-1 rounded-md bg-zinc-200;
}

body {
	@apply bg-zinc-200;
}
</style>
