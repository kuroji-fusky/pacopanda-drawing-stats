<template>
	<div>
		<nuxt-link to="/" class="wordmark-heading">Paco Drawing Stats</nuxt-link>
		<span class="block wordmark-subheading">
			by
			<nuxt-link class="wordmark-subheading" to="https://kurofusky.xyz">
				Kuroji Fusky
			</nuxt-link>
		</span>
	</div>
</template>

<style lang="scss">
.wordmark {
	&-heading {
		@apply text-3xl font-inter font-bold;
	}

	&-subheading {
		@apply text-sm;
	}
}

a.wordmark-subheading {
	@apply text-violet-600 font-semibold;
}
</style>
