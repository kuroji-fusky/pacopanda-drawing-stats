<template>
	<section class="services-section">
		<article class="article-prose">
			<p>
				Currently, this project is running under limited resources on their free
				tier from the services I use; meaning that the data you see here won't
				be updated immediately to save costs on server infrastructure.
			</p>
			<p>
				This is purely a hobby project that doesn't need to be scaled further
				but just enough to get this ambious project out there!
			</p>
		</article>
		<ul class="services-list-grid">
			<LandingServicesItem
				v-for="service in SERVICES_LIST"
				:name="service.service"
				:logo="service.logo"
				:description="service.purpose"
			/>
		</ul>
	</section>
</template>

<script setup lang="ts">
import Railway from "../Icons/Railway.vue"

const SERVICES_LIST = [
	{
		service: "Vercel",
		link: "https://vercel.com/home",
		purpose: "To host this website and the APIs (yes it's possible!)",
	},
	{
		service: "Redis Enterprise Cloud",
		link: "https://redis.com",
		purpose:
			"For providing a Redis database (via the free tier) from a Google Cloud vendor",
	},
	{
		service: "Railway",
		link: "https://railway.app",
		logo: Railway,
		purpose: "To host a Docker container to update the data on a daily basis",
	},
]
</script>

<style lang="scss">
.services-list-grid {
	@apply grid grid-flow-col grid-cols-3 gap-5;
}
</style>
