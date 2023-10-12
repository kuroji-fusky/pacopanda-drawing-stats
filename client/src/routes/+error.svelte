<script lang="ts">
  import { page } from "$app/stores"
</script>

<div class="text-center grid place-items-center">
  <h1>{$page.status}: {$page.error?.message}</h1>
</div>
