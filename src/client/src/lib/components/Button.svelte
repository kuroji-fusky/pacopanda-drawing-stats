<script lang="ts">
  export let href: string | undefined = undefined
  export let onClick: ((e: MouseEvent) => void) | undefined = undefined
</script>

{#if !href}
  <button on:click={onClick ?? undefined} type="button">
    <slot />
  </button>
{:else}
  <a {href}>
    <slot />
  </a>
{/if}
