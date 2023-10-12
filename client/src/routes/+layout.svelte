<script lang="ts">
  // @ts-ignore
  import type { PageLoad } from "./$types"
  import "@fontsource/inter"
  import "@fontsource/open-sans"
  import "@fontsource/open-sans/600.css"
  import "../app.css"

  import Navbar from "$lib/Navbar.svelte"
  import Footer from "$lib/Footer.svelte"

  export let data: PageLoad
</script>

<svelte:head>
  <link rel="canonical" href={data.computedUrl} />
</svelte:head>

<Navbar />
<main class="h-[calc(100dvh-4rem)]">
  <slot />
</main>
<Footer />
