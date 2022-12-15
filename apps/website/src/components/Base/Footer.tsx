import Link from "next/link"
import styles from "./Footer.module.scss"

export default function Footer() {
  return (
    <div className={styles["root-wrapper"]}>
      <footer className={styles["wrapper"]}>
        <div className={styles["disclaimer-lower-third"]}>
          <p>
            <strong>Paco Drawing Stats</strong> is a data viz and an open-source
            project created by Kuroji Fusky. I do not own or claim any of the
            third-party content to this site whatsoever.
          </p>
          <p>
            <strong>NOTE:</strong> Prior to 2019, he has stopped licensing his
            work under Creative Commons on DeviantArt. Most the artwork
            presented on this website is primarily for analytical purposes.
          </p>
          <p>
            {`© ${new Date().getFullYear()} Kuroji Fusky - source code licensed under `}
            <Link
              href="https://opensource.org/licenses/MIT"
              target="_blank"
              rel="noopenner noreferrer"
              className="underline"
            ></Link>
          </p>
        </div>
        <div>source code and other links</div>
      </footer>
    </div>
  )
}
