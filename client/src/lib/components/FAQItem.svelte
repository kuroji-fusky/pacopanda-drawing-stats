<script lang="ts">
  import { onMount } from "svelte"

  export let title: string

  onMount(() => {
    console.log("MY DICK")
  })
</script>

<div class="">
  <button>
    {title}
  </button>
  <slot />
</div>
