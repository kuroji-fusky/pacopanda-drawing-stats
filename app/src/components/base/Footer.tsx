import { FontAwesomeIcon as FaIcon } from "@fortawesome/react-fontawesome"
import { faGithub } from "@fortawesome/free-brands-svg-icons"
import Link from "next/link"
import styles from "@/styles/base/Footer.module.scss"
import { LinkGroup } from "./Header"
import { FooterLinkMenu } from "@/models/Menus"

export default function Footer() {
  return (
    <footer id={styles.container}>
      <div id={styles.wrapper}>
        <div>
          <h2>Navigation</h2>
          <ul>
            {FooterLinkMenu.map((item, index) => (
              <li key={index}>
                <LinkGroup name={item.name} route={`/${item.route}`} />
              </li>
            ))}
          </ul>
        </div>
        <div>
          <p>
            <strong>NOTE:</strong> Prior to sometime in 2019, most the artwork
            presented on this website is primarily for informational purposes.
            He has stopped licensing his work for Creative Commons on
            DeviantArt.
          </p>
          <p>
            But despite this, the use of content is heavily transformative falls
            under the doctrine of Fair Use. This is a passion project is 100%
            open source and I don't have any incentive to monetize this
            whatsoever.
          </p>
        </div>
        <div>
          <span className="flex gap-1">
            Written in Next.js and FastAPI.
            <Link
              href="https://github.com/skepfusky/pacopanda-drawing-stats"
              passHref
            >
              <a>
                <FaIcon icon={faGithub} className="mr-[4px]" />
                <span>Source code on GitHub</span>
              </a>
            </Link>
          </span>
          <p>Copyright &copy; 2021-{new Date().getFullYear()} skepfusky</p>
        </div>
      </div>
    </footer>
  )
}
