<script lang="ts">
  export let heading: string = ""
</script>

<div class="p-3">
  <div class="flex justify-between items-center">
    <span class="font-heading font-bold text-xl">{heading}</span>
    <slot name="lefty" />
  </div>
  <slot />
</div>
