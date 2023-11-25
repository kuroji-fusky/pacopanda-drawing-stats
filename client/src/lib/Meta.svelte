<script lang="ts">
  import { page } from "$app/stores"
  import { dev } from "$app/environment"

  export let title: string
  export let description: string
  export const SITE_NAME = "Paco Drawing Stats"

  const DEV_URL = "http://localhost:4000"
  const PROD_URL = "paco-api.kurojifusky.com"
</script>

<svelte:head>
  <link rel="prefetch" href={dev ? DEV_URL : PROD_URL} />
  <link rel="canonical" href={$page.url.href} />
  <title>{title} | {SITE_NAME}</title>
  <meta name="description" content={description} />
  <meta property="og:type" content="website" />
  <meta property="og:title" content={title} />
  <meta property="og:description" content={description} />
  <meta property="og:site_name" content={SITE_NAME} />
  <meta name="twitter:card" content="summary_large_card" />
  <meta name="twitter:title" content={title} />
  <meta name="twitter:description" content={description} />
</svelte:head>
