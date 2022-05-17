import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faGithub } from "@fortawesome/free-brands-svg-icons";
import Link from "next/link";
import styles from "../styles/Footer.module.scss";
import { LinkGroup } from "./Header";

export default function Footer() {
  return (
    <footer id={styles["footer-container"]}>
      <div id={styles.wrapper}>
        <div>
          <h2 className="text-2xl font-bold">Navigation</h2>
          <ul>
            <li>
              <LinkGroup name="Browse" route="browse" />
            </li>
            <li>
              <LinkGroup
                name="Paco Stats API (yes you heard me)"
                route="stats-api"
              />
            </li>
            <li>
              <LinkGroup name="About this project" route="about" />
            </li>
            <li>
              <LinkGroup
                name="How I gather project"
                route="about#how-i-gather-data"
              />
            </li>
          </ul>
        </div>
        <div>
          <strong>NOTE:</strong> Prior to sometime in 2019, most the artwork
          presented on this website is primarily for informational purposes. He
          has stopped licensing his work for Creative Commons on DeviantArt -
          but despite this, the use of content is heavily transformative falls
          under the doctrine of Fair Use. This is a passion project is 100% open
          source and I don't have any incentive to monetize this whatsoever.
        </div>
        <div>
          <span className="flex gap-1">
            Written in Next.js and Flask.
            <Link
              href="https://github.com/skepfusky/pandapaco-drawing-stats"
              passHref
            >
              <a>
                <FontAwesomeIcon
                  icon={faGithub}
                  style={{ marginRight: "4px" }}
                />
                <span>Source code on GitHub</span>
              </a>
            </Link>
          </span>
          <p>Copyright &copy; 2021-{new Date().getFullYear()} skepfusky</p>
        </div>
      </div>
    </footer>
  );
}
