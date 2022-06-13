import layoutStyles from "@/styles/base/Layout.module.scss"
import styles from "@/styles/components/YearStats.module.scss"

export function CurrentStats({ children }: { children?: React.ReactNode }) {
  return (
    <div>
      <h2>{new Date().getFullYear()} - Current Stats</h2>
      {children}
    </div>
  )
}

interface HighlightStatsProps {
  year?: number
  children?: React.ReactNode
}

export function HighlightStats({ year, children }: HighlightStatsProps) {
  return (
    <div>
      {year ? <h2>Stats from {year}</h2> : <h2>Previous Stats</h2>}
      {children}
    </div>
  )
}
