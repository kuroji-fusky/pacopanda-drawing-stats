<script lang="ts">
  import { onMount } from "svelte"

  export let title: string

  onMount(() => {
    console.log("Yes")
  })
</script>

<div class="">
  <button>
    {title}
  </button>
  <slot />
</div>
