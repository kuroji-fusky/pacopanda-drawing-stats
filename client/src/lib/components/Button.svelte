<script lang="ts">
  export let href: string
  export let onClick: (e: MouseEvent) => void
</script>

{#if !href}
  <a {href}>
    <slot />
  </a>
{:else}
  <button on:click={onClick} type="button">
    <slot />
  </button>
{/if}
