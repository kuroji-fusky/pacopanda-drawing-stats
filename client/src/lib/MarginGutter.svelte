<script lang="ts">
  export let className: string = ""

  function FilterClassName(...className: string[]) {
    return className.filter(Boolean).join(" ")
  }
</script>

<div class={FilterClassName("max-w-screen-2xl mx-auto px-8", className)}>
  <slot />
</div>
