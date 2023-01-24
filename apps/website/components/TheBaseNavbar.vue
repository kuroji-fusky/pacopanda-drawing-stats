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
				<ul class="flex justify-between text-lg gap-x-3">
					<li v-for="item in navItems" :key="item.text" :class="{ 'relative': item.dropdown }">
						<nuxt-link :to="item.link" class="block px-4 py-3.5">
							{{ item.text }}
						</nuxt-link>
						<div v-if="item.dropdown" class="absolute p-4 -translate-x-5 bg-gray-400 rounded-md w-fit top-14">
							<ul class="grid gap-y-1">
								<li v-for="nested in item.dropdown">
									<nuxt-link :to="nested.link"
										class="block w-[11.5rem] px-3.5 py-2 border rounded-md">
										{{ nested.text }}
									</nuxt-link>
								</li>
							</ul>
						</div>
					</li>
				</ul>
			</nav>
		</div>
	</header>
</template>

<script setup lang="ts">
const navItems = [
	{
		link: "/browse",
		text: "Browse data",
		dropdown: [
			{ link: "/browse/characters", text: "Characters" },
			{ link: "/browse/species", text: "Species" },
			{ link: "/browse/chronology", text: "Chronology" },
			{ link: "/about/how-i-gather-data", text: "How I gather data" }
		]
	},
	{
		link: "/statistics",
		text: "Statistics"
	},
	{ link: "/api", text: "API Docs" },
	{ link: "/about", text: "About" }
]
</script>

<style lang="scss" scoped>
#wrapper {
	@apply px-12 py-6 flex justify-between items-center;
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
</style>
