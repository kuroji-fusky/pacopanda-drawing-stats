<template>
	<section class="px-12 mx-auto max-w-screen-2xl">
		<article class="article-prose">
			<h2>In the beginning...</h2>
			<p>
				During my early days in web development - I've had this idea far beyond
				my knowledge at the time, where I compile various drawing data - I have
				no knowledge of automating things with code besides pure HTML and CSS.
			</p>
			<p>
				As I've gotten around with basic data science and Python scripting;
				there are has been substanial progress from the beginning but due to
				other projects and tasks, this project has been delayed with little to
				no progress for the entire 2022.
			</p>
		</article>
	</section>
</template>

<style lang="scss" scoped>
.article-prose {
	h2 {
		@apply mb-4 text-4xl font-bold font-inter;
	}

	p {
		@apply text-xl mb-4 leading-8;

		&:last-child {
			@apply mb-0;
		}
	}
}
</style>
