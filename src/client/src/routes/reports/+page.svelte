<script lang="ts">
  import MarginGutter from "$lib/MarginGutter.svelte"
  import Meta from "$lib/Meta.svelte"
  import ReportsItem from "$lib/components/ReportsItem.svelte"
</script>

<Meta title="Reports" description="Various compiled reports" />

<MarginGutter>
  <div class="my-9 prose-p:my-2.5 mx-7">
    <h1 class="text-4xl font-heading font-bold">Reports</h1>
    <p class="text-lg">Various compiled reports from previous artwork data</p>
  </div>
  <div class="flex flex-col gap-y-4">
    <ReportsItem year="2021" name="2021 report" compileDate="12/28/2021" />
    <ReportsItem year="2020" name="2020 report" compileDate="12/28/2020" />
    <ReportsItem year="2019" name="2019 report" compileDate="12/28/2019" />
    <ReportsItem year="2018" name="2018 report" compileDate="12/28/2018" />
  </div>
</MarginGutter>
