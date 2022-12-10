import Link from "next/link"
import styles from "./Navbar.module.scss"

export default function Navbar() {
  return (
    <>
      <div className={styles["root-wrapper"]}>
        <header className={styles["container"]}>
          <Link href="/" className={styles["logo-wrapper"]}>
            <strong className={styles["logo-title"]}>Paco Drawing Stats</strong>
            <div className={styles["logo-subtitle"]}>
              <span>by&nbsp;</span>
              <span className={styles["logo-kuroji-wordmark"]}>
                Kuroji Fusky
              </span>
            </div>
          </Link>
          <nav className={styles["nav-row"]}>
            <Link href="/browse">Browse</Link>
            <Link href="/docs/api">API</Link>
            <Link href="/about">About</Link>
          </nav>
        </header>
      </div>
    </>
  )
}
