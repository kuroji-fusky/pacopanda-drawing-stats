<script lang="ts">
  import clsx from "clsx"

  export let className: string = ""
</script>

<div class={clsx("max-w-screen-2xl mx-auto px-8", className)}>
  <slot />
</div>
