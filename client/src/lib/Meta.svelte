<script lang="ts">
  import { page } from "$app/stores"

  export let title: string
  export let description: string
  export const SITE_NAME = "Paco Drawing Stats"
</script>

<svelte:head>
  <title>{title} | {SITE_NAME}</title>
  <meta name="description" content={description} />
  <!-- Open Graph -->
  <meta property="og:type" content="website" />
  <meta property="og:title" content={title} />
  <meta property="og:description" content={description} />
  <meta property="og:site_name" content={SITE_NAME} />
  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_card" />
  <meta name="twitter:title" content={title} />
  <meta name="twitter:description" content={description} />
  <link rel="canonical" href={$page.url.href} />
</svelte:head>
