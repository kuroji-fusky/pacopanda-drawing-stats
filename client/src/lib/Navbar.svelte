<script lang="ts">
  import Fa from "svelte-fa"
  import { faGithub } from "@fortawesome/free-brands-svg-icons"
  import { SearchIcon } from "lucide-svelte"
</script>

<nav
  class="max-w-screen-2xl mx-auto px-8 flex justify-between items-center py-3 sticky top-0 w-full bg-white"
>
  <a href="/" class="grid grid-cols-[minmax(0,1fr)_auto] grid-rows-2 gap-x-3">
    <img
      src="./max-icon.png"
      alt="PDS"
      width="48"
      height="48"
      class="aspect-square row-span-2"
    />
    <span class="text-lg font-bold">Paco Drawing Stats</span>
    <span>by Kuroji Fusky</span>
  </a>
  <div class="flex items-center gap-x-5">
    <a href="/browse">Browse</a>
    <a href="/reports">Reports</a>
    <a href="/about">About</a>
    <button>
      <SearchIcon size={21} aria-label="Search icon" />
    </button>
    <a
      href="https://github.com/kuroji-fusky/pacopanda-drawing-stats"
      target="_blank"
    >
      <Fa class="text-lg" icon={faGithub} style="font-size: 1.5em" fw />
    </a>
  </div>
</nav>
