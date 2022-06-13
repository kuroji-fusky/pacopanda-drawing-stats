import layoutStyles from "@/styles/base/Layout.module.scss"

export default function CurrentStats({}: {}) {
  return (
    <div
      className={`${layoutStyles["bg-stats-content"]}`}
      style={{ gridArea: "stats-current" }}
    >
      <h2>{new Date().getFullYear()} - Current Stats</h2>
      <div className="grid grid-cols-3 gap-3 ">
        <div>No. of total drawings; with four quarters</div>
        <div>Most species drawn so far; with four quarters</div>
        <div>Most characters drawn so far; with four quarters</div>
      </div>
    </div>
  )
}
