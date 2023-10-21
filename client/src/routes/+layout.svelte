<script lang="ts">
  import "../app.css"
  import { page } from "$app/stores"

  import "@fontsource/inter"
  import "@fontsource/open-sans"
  import "@fontsource/open-sans/600.css"

  import Navbar from "$lib/Navbar.svelte"
  import Footer from "$lib/Footer.svelte"
</script>

<svelte:head>
  <link rel="canonical" href={$page.url.href} />
</svelte:head>

<Navbar />
<main class="h-[calc(100dvh-4rem)]">
  <slot />
</main>
<Footer />
