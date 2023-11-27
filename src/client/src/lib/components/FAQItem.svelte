<script lang="ts">
  import clsx from "clsx"
  import SvelteMarkdown from "svelte-markdown"
  import { ChevronDown } from "lucide-svelte"

  export let title: string
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  export let content: any

  let isExpanded = false
  let faqContents: HTMLDivElement

  const toggleItem = () => {
    isExpanded = !isExpanded

    const contentHeight = faqContents.scrollHeight
    faqContents.style.height = !isExpanded ? "0px" : `${contentHeight}px`
  }
</script>

<div
  class={clsx(
    "rounded-md shadow-md overflow-hidden border transition-colors",
    isExpanded ? "border-green-500" : ""
  )}
  aria-expanded={isExpanded}
>
  <button
    class="px-4 py-3 text-lg font-heading w-full flex justify-between"
    on:click={toggleItem}
  >
    <h2 class="font-semibold">{title}</h2>
    <ChevronDown
      class={clsx("transition-transform", isExpanded ? "rotate-180" : "")}
    />
  </button>
  <div
    bind:this={faqContents}
    class="transition-all duration-300"
    style="height: 0px"
    aria-hidden={!isExpanded}
  >
    <article class="px-4 pb-3">
      <SvelteMarkdown source={content} />
    </article>
  </div>
</div>
