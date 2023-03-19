<template>
	<div>
		<NuxtLink to="/" class="wordmark-heading">Paco Drawing Stats</NuxtLink>
		<span class="block wordmark-subheading">
			by
			<NuxtLink class="wordmark-subheading" to="https://kurofusky.xyz">
				Kuroji Fusky
			</NuxtLink>
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
