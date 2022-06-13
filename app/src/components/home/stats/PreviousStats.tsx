import layoutStyles from "@/styles/base/Layout.module.scss"

interface HighlightStatsProps {
  year?: number
  children?: React.ReactNode
  style: React.CSSProperties
}

export default function PreviousStats() {
  return (
    <>
      <HighlightStats year={new Date().getFullYear() - 1} style={{ gridArea: "stats-1" }} />
      <HighlightStats year={new Date().getFullYear() - 2} style={{ gridArea: "stats-2" }} />
      <HighlightStats style={{ gridArea: "stats-prev"}}>
        <div>Line chart for all the previous years for no. of artworks, characters, and species drawn</div>
        <div>Seperate line chart for all the digital or traditional</div>
      </HighlightStats>
      <OverallStats>
        <div>A bar chart of activity of artworks he uploaded on a per-week basis and an average</div>
        <div>Most character and species drawn</div>
        <div>Drawings with most tags used</div>
      </OverallStats>
    </>
  )
}

export function HighlightStats({ year, children, style }: HighlightStatsProps) {
  return (
    <div className={layoutStyles["bg-stats-content"]} style={style}>
      {year ? <h2>Stats from {year}</h2> : <h2>Previous Stats</h2>}
      {children}
    </div>
  )
}

export function OverallStats({ children }: {children: React.ReactNode}) {
  return(
    <div className={`${layoutStyles["bg-stats-content"]}`} style={{ gridArea: "stats-overall" }}>
      <h2>Overall Stats</h2>
      {children}
    </div>
  )
}