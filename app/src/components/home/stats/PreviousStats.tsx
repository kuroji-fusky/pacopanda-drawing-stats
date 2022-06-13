import { HighlightStats } from "./YearStats"
import layoutStyles from "@/styles/base/Layout.module.scss"

export default function PreviousStats() {
  return (
    <>
      <div id={layoutStyles["grid-container"]}>
        <HighlightStats year={new Date().getFullYear() - 1} />
        <HighlightStats year={new Date().getFullYear() - 2} />
      </div>
      <HighlightStats>
        <p>lol</p>
      </HighlightStats>
    </>
  )
}
