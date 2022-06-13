import BaseHead from "@/components/base/BaseHead"
import { CurrentStats } from "@/components/home/stats/YearStats"
import PreviousStats from "@/components/home/stats/PreviousStats"
import BrowseArt from "@/components/home/BrowseArt"

export default function Home() {
  return (
    <>
      <BaseHead title="Home" description="Stats for latest drawings" />
      <CurrentStats />
      <PreviousStats />
      <BrowseArt />
    </>
  )
}
