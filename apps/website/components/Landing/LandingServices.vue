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
				but just to get this ambious project out there!
			</p>
		</article>
		<ul class="services-list-grid">
			<li>Vercel - to host this website</li>
			<li>
				Redis Enterprise Cloud - for providing a database (via free tier) from a AWS cloud
				vendor
			</li>
			<li>
				Railway - to host a Docker containers to update the data 24/7 and to host
				the APIs
			</li>
		</ul>
	</section>
</template>

<script setup lang="ts"></script>

<style lang="scss">
.services-section {
	@apply max-w-screen-2xl mx-auto px-12;
}
</style>
