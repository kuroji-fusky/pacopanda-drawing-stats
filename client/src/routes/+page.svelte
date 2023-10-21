<script lang="ts">
  import Meta from "$lib/Meta.svelte"
  import Fa from "svelte-fa"
  import { faGithub } from "@fortawesome/free-brands-svg-icons"
  import { Info } from "lucide-svelte"
  import Group from "$lib/components/Group.svelte"
</script>

<Meta
  title="Home"
  description="A statistics project created by Kuroji Fusky that collects and parses artworks from Paco Panda."
/>
<article
  class="flex flex-col items-center text-center w-full px-8 lg:w-3/4 xl:w-1/2 mx-auto gap-y-2.5"
>
  <h2 class="font-heading font-bold my-5 text-5xl">Paco Drawing Stats</h2>
  <p class="text-base xl:text-xl">
    A statistics project created by Kuroji Fusky that collects and parses
    artworks from Paco Panda.
  </p>
  <div class="flex justify-center gap-x-2 mt-4">
    <a
      href="https://github.com/kuroji-fusky/pacopanda-drawing-stats"
      target="_blank"
      class="font-heading font-semibold flex items-center gap-x-1 px-3 py-2 rounded-md bg-green-200 hover:bg-green-400 transition-colors"
    >
      <Fa class="text-xl" icon={faGithub} fw />
      <span> View source code </span>
    </a>
    <a
      href="/about"
      class="font-heading font-semibold flex items-center gap-x-1 px-3 py-2 rounded-md bg-green-200 hover:bg-green-400 transition-colors"
    >
      <Info size={20} />
      <span> About this project </span>
    </a>
  </div>
</article>
<!-- Chart render -->
<div class="px-8">
  <div class="shadow-md grid mx-auto max-w-screen-xl rounded-md grid-cols-2">
    <span class="col-span-2">
      <Group heading="Main chart">Your mom</Group>
    </span>
    <Group heading="Top5MonthChars" />
    <Group heading="Top5MonthSpecies" />
  </div>
</div>
