<template>
	<header>
		<div id="wrapper">
			<div>
				<nuxt-link to="/" class="wordmark-heading">Paco Drawing Stats</nuxt-link>
				<span class="block wordmark-subheading">
					by
					<nuxt-link class="wordmark-subheading" to="https://kurofusky.xyz">
						Kuroji Fusky
					</nuxt-link>
				</span>
			</div>
			<nav>
				<ul class="nav-items">
					<li v-for="item in navItems" :key="item.text">
						<nuxt-link :to="item.link">
							{{ item.text }}
						</nuxt-link>
					</li>
				</ul>
			</nav>
		</div>
	</header>
</template>

<script setup lang="ts">
const navItems = [
	{ link: "/browse", text: "Browse data" },
	{ link: "/statistics", text: "Statistics" },
	{ link: "/api", text: "API" },
	{ link: "/about", text: "About" },
]
</script>

<style lang="scss" scoped>
#wrapper {
	@apply px-12 py-4 flex justify-between items-center;
}

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

.nav-items {
	@apply flex justify-between gap-x-8 text-lg;
}
</style>
