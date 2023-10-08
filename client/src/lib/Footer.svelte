<script lang="ts">
  import Fa from "svelte-fa";
  import {
    faGithub,
    faMastodon,
    faXTwitter,
    faYoutube,
  } from "@fortawesome/free-brands-svg-icons";

  const year = new Date().getFullYear();
  const copyright = `© 2021-${year} Kuroji Fusky, licensed under MIT`;

  const socials = [
    {
      name: "YouTube",
      icon: faYoutube,
      link: "https://youtube.com/@kurojifusky",
    },
    { name: "GitHub", icon: faGithub, link: "https://github.com/kuroji-fusky" },
    {
      name: "X, formerly Twitter",
      icon: faXTwitter,
      link: "https://twitter.com/@kurojifusky",
    },
    {
      name: "Mastodon",
      icon: faMastodon,
      link: "https://furry.engineer/@kurojifusky",
    },
  ];
</script>

<footer
  class="flex items-center justify-between mx-auto max-w-screen-2xl px-9 py-3.5"
>
  <div>
    {copyright}
  </div>
  <div class="flex items-center gap-x-4">
    <a
      href="https://github.com/kuroji-fusky/pacopanda-drawing-stats"
      target="_blank"
      class="inline-flex gap-x-1 items-center hover:underline"
    >
      <Fa class="text-lg" icon={faGithub} fw />
      <span>Source code</span>
    </a>
    <hr class="h-6 border-l border-l-red-300" />
    {#each socials as item, index (index)}
      <a href={item.link} title={item.name}>
        <Fa class="text-lg" icon={item.icon} fw />
      </a>
    {/each}
  </div>
</footer>
