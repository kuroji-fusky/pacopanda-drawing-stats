<template>
	<header>
		<div id="wrapper">
			<navbar-logo />
			<nav>
				<ul class="nav-list-container">
					<li
						v-for="item in navItems"
						:key="item.text"
						:class="{ 'has-dropdown': item.dropdown }"
					>
						<nuxt-link :to="item.link" class="nav-list-item">
							{{ item.text }}
							<IconChevronDown v-if="item.dropdown" />
						</nuxt-link>
						<div v-if="item.dropdown" class="nav-dropdown-list">
							<ul class="dropdown-render-list">
								<li v-for="nested in item.dropdown">
									<nuxt-link :to="nested.link" class="dropdown-item">
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
import { IconChevronDown } from "@iconify-prerendered/vue-fa6-solid"

const navItems = [
	{
		link: "/browse",
		text: "Browse data",
		dropdown: [
			{ link: "/browse/characters", text: "By characters" },
			{ link: "/browse/species", text: "By species" },
			{ link: "/browse/chronology", text: "By chronology" },
			{ link: "/browse/tags", text: "By tags" }
		]
	},
	{ link: "/api", text: "API" },
	{
		link: "/about",
		text: "About",
		dropdown: [
			{ link: "/about#faq", text: "FAQs" },
			{ link: "/about/how-i-gather-data", text: "How I gather data" }
		]
	}
]
</script>

<style lang="scss" scoped>
#wrapper {
	@apply px-12 py-6 flex justify-between items-center;
}

.nav-list-container {
	@apply flex justify-between gap-x-2 text-[1.015rem];
}

.nav-list-item {
	@apply flex gap-x-3 items-center px-4 py-[0.5rem] rounded-md border border-white;

	@apply hover:bg-green-100;

	&.router-link-active {
		@apply bg-green-200 border-green-500 text-green-800;
	}
}

.has-dropdown {
	@apply relative;

	&:hover > .nav-dropdown-list {
		@apply opacity-100 top-10 pointer-events-auto;
	}
}

.has-dropdown:last-child .nav-dropdown-list {
	@apply right-0 translate-x-3;
}

.nav-dropdown-list {
	@apply absolute pt-3 -translate-x-3 w-fit top-[2.75rem] opacity-0 pointer-events-none transition-all duration-300;
}

.dropdown-render-list {
	@apply grid gap-y-0.5 bg-slate-100 shadow-lg rounded-md py-4;
}

.dropdown-item {
	@apply block w-[11.5rem] mx-3 px-3 py-1.5 border rounded-lg hover:text-green-600 hover:bg-green-200 hover:bg-opacity-30 border-transparent hover:border-green-400 transition-colors duration-100;
}
</style>
