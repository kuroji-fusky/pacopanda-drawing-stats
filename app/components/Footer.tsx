import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faGithub } from "@fortawesome/free-brands-svg-icons";
import Link from "next/link";
import styles from "../styles/Layout.module.scss";

export default function Footer() {
  return (
    <footer>
      <div className={styles['content-wrapper']}>
        <hr />
        <span className="flex flex-col gap-2 text-center items-center">
          <p>
            Prior to sometime in 2019, most the artwork presented on this
            website is primarily for informational purposes. He has stopped
            licensing his work for Creative Commons on DeviantArt - but despite
            this, the use of content is heavily transformative falls under the
            doctrine of Fair Use. This is a passion project is 100% open source
            and I don't have any incentive to monetize this whatsoever.
          </p>
          <span className="flex gap-1">
            Written in Next.js and Flask.
            <Link href="https://github.com/skepfusky/pandapaco-drawing-stats" passHref>
              <a className="flex items-center gap-x-1">
                <FontAwesomeIcon icon={faGithub} />
                <span>Source code on GitHub</span>
              </a>
            </Link>
          </span>
          <p>Copyright &copy; 2021-{new Date().getFullYear()} skepfusky</p>
        </span>
      </div>
    </footer>
  );
}
