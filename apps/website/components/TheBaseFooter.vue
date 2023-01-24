<template>
	<footer>
		<div id="wrapper">
			<div class="flex divide-x-2 divide-solid">
				<div class="flex-shrink-0 w-4/12 pr-5"></div>
				<article class="grid w-full pl-5 gap-y-2.5">
					<h2 class="text-xl font-bold uppercase font-inter">Copyright Disclaimer</h2>
					<p>
						This is an ambitious passion project created by an individual; I do
						not own nor claim any of the third-party content from this site -
						neither it is stored from the database whatsoever. Before 2019, he
						stopped licensing his work under Creative Commons on DeviantArt.
					</p>
					<p>
						Most of the artwork presented on this website is primarily for
						informational and analytical purposes.
					</p>
				</article>
			</div>
			<div class="grid py-5 text-center place-items-center">
				<span>
					Copyright &copy; 2021-{{ year }}
					Kuroji Fusky; project source code licensed under
					<nuxt-link
						class="link-underline"
						to="https://opensource.org/licenses/MIT"
						>MIT</nuxt-link
					>
				</span>
			</div>
		</div>
	</footer>
</template>

<script setup lang="ts">
const year = new Date().getFullYear()
</script>

<style scoped>
#wrapper {
	@apply px-12 pt-4;
}
</style>
