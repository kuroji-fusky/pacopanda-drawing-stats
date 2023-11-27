<script lang="ts">
  export let link: string = ""
  export let image: string = ""
  export let name: string = ""
  export let year: string = ""
  export let compileDate: string = ""
</script>

<a
  href={link}
  class="p-3 rounded-md hover:shadow-xl hover:-translate-y-1 shadow-lg flex items-center gap-4 transition-all border hover:border-green-400"
>
  <img
    src={image}
    alt=""
    class="aspect-video flex-shrink-0 h-full w-40 rounded-md"
  />
  <div class="flex flex-col">
    <h2 class="text-xl font-bold my-1">{name}</h2>
    <div class="flex flex-wrap gap-2">
      <span>{year}</span>
      <span>Compiled on {compileDate}</span>
    </div>
  </div>
</a>
