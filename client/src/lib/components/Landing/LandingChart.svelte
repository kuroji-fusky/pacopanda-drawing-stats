<script lang="ts">
  import Group from "$lib/components/Group.svelte"
</script>

<div class="px-8">
  <div class="shadow-md grid mx-auto max-w-screen-xl rounded-md grid-cols-2">
    <span class="col-span-2">
      <Group heading="Main chart">Your mom</Group>
    </span>
    <Group heading="Top5MonthChars" />
    <Group heading="Top5MonthSpecies" />
  </div>
</div>
