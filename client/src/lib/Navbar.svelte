<script lang="ts">
  import { SearchIcon } from "lucide-svelte";
</script>

<nav
  class="mx-auto max-w-screen-2xl flex justify-between items-center px-8 py-3"
>
  <span> PDS </span>
  <div class="flex items-center gap-x-2">
    <a href="/#"> Browse</a>
    <a href="/#"> About</a>
    <button>
      <SearchIcon />
    </button>
  </div>
</nav>
