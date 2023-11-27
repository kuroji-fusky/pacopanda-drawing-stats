<script lang="ts">
  import Meta from "$lib/Meta.svelte"
  import { page } from "$app/stores"
</script>

<Meta title="404 Not Found" description="" />
<div class="text-center grid place-items-center">
  <h1>{$page.status}: {$page.error?.message}</h1>
</div>
