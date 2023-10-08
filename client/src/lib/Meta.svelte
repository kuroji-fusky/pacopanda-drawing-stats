<script lang="ts">
  export let title: string;
  export let description: string
</script>

<svelte:head>
  <title>{title}</title>
  <meta name="description" content={description} />
  <!-- Open Graph -->
  <meta property="og:type" content="website" />
  <meta property="og:title" content={title} />
  <meta property="og:description" content={description} />
  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_card" />
  <meta name="twitter:title" content={title} />
  <meta name="twitter:description" content={description} />
</svelte:head>
