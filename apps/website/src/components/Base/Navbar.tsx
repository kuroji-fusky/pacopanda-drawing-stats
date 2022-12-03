import styles from "./Navbar.module.scss"

export default function Navbar() {
  return (
    <>
      <div className={styles["root-wrapper"]}>
        <header className={styles["container"]}>
          <div className={styles["logo-wrapper"]}>
            <strong className={styles["logo-title"]}>Paco Drawing Stats</strong>
            <div className={styles["logo-subtitle"]}>
              <span>by&nbsp;</span>
              <span className={styles["logo-kuroji-wordmark"]}>
                Kuroji Fusky
              </span>
            </div>
          </div>
          <nav className={styles["nav-row"]}>Item 2</nav>
        </header>
      </div>
    </>
  )
}
