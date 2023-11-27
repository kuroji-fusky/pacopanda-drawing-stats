<script lang="ts">
  import "../app.css"

  import "@fontsource/inter"
  import "@fontsource/open-sans"
  import "@fontsource/open-sans/600.css"

  import Navbar from "$lib/Navbar.svelte"
  import Footer from "$lib/Footer.svelte"
</script>

<Navbar />
<div class="h-[calc(100dvh-4rem)]">
  <slot />
</div>
<Footer />
