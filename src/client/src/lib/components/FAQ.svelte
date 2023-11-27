<script lang="ts">
  import dedent from "dedent"
  import FaqItem from "$lib/components/FAQItem.svelte"

  const faqItems = [
    {
      title: "What is Paco Drawing Stats?",
      content: dedent`
      It's a case project and data science project when I was
      learning web development at the time.`,
    },
    {
      title: "What is the purpose of this project?",
      content: dedent`
      The main purpose of this project is to track 2,000+ drawings and
      calculate his posting frequency of his drawings, as well as, other characters
      he's frequently drawn for a decade`,
    },
    {
      title: "What data does it get?",
      content: dedent`
      Using an automated Python script, it gathers all public
      data from his FurAffinity, Weasyl, DeviantArt, and more.

      With the exception of his X/Twitter profile since its corresponding
      API is no longer free.`,
    },
  ]
</script>

<div class="px-8">
  <div class="mx-auto max-w-screen-xl">
    <h2
      class="text-center text-4xl my-6 font-bold font-heading"
      aria-label="Frequently asked questions"
    >
      FAQs
    </h2>
    <div class="flex flex-col gap-y-3">
      {#each faqItems as { title, content }}
        <FaqItem {title} {content} />
      {/each}
    </div>
  </div>
</div>
