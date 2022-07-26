import styles from "@/styles/components/YearStats.module.scss"
import layoutStyles from "@/styles/base/Layout.module.scss"
import PreviousStats from "./stats/PreviousStats"
import CurrentStats from "./stats/CurrentStats"

export default function Stats() {
  return (
    <div
      className={`${styles["stats-grid"]} ${layoutStyles["content-wrapper"]}`}
    >
      <CurrentStats />
      <PreviousStats />
    </div>
  )
}
