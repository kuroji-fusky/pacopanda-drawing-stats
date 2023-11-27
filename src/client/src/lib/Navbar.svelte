<script lang="ts">
  import { page } from "$app/stores"
  import Fa from "svelte-fa"
  import { faGithub } from "@fortawesome/free-brands-svg-icons"
  import { SearchIcon } from "lucide-svelte"
  import Button from "./components/Button.svelte"

  const navArr = ["Browse", "Reports", "About", "API Reference"]

  const contentsToLowerCase = (input: string) => {
    const filterWhitespace = input.replace(/\s/g, "-")
    return filterWhitespace.toLowerCase()
  }
</script>

<nav
  class="max-w-screen-2xl mx-auto px-8 flex justify-between items-center py-3 sticky top-0 w-full bg-white"
>
  <a href="/" class="flex items-center gap-x-2.5">
    <img
      src="./max-icon.png"
      alt="Paco Drawing Stats"
      width="40"
      height="40"
      class="aspect-square row-span-2"
    />
    <div class="flex flex-col gap-0">
      <span class="text-xl font-bold font-heading">Paco Drawing Stats</span>
      <span class="text-xs">by Kuroji Fusky</span>
    </div>
  </a>
  <div class="flex items-center gap-x-5" data-sveltekit-preload-data>
    {#each navArr as item}
      <a
        href={`/${contentsToLowerCase(item)}`}
        class={$page.url.pathname === `/${contentsToLowerCase(item)}`
          ? "hover:text-green-500 text-green-600 underline"
          : "hover:text-green-500 hover:underline"}>{item}</a
      >
    {/each}
    <Button>
      <SearchIcon size={19} aria-label="Search icon" />
    </Button>
    <a
      href="https://github.com/kuroji-fusky/pacopanda-drawing-stats"
      target="_blank"
    >
      <Fa class="text-lg" icon={faGithub} style="font-size: 1.5em" fw />
    </a>
  </div>
</nav>
