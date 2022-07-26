import BaseHead from "@/components/base/BaseHead"
import BrowseArt from "@/components/home/BrowseArt"
import Stats from "@/components/home/Stats"

export default function Home() {
  return (
    <>
      <BaseHead title="Home" description="Stats for latest drawings" />
      <Stats />
      <BrowseArt />
    </>
  )
}
