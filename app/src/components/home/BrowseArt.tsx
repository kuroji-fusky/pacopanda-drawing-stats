import Link from "next/link"
import layoutStyles from "@/styles/base/Layout.module.scss"
import { FontAwesomeIcon as FaIcon } from "@fortawesome/react-fontawesome"
import { faDeviantart } from "@fortawesome/free-brands-svg-icons"

export default function BrowseArt() {
  return (
    <div className={layoutStyles["content-wrapper"]}>
      <h2>Browse the art lol</h2>
      <Link href="deviantart.com" passHref>
        <FaIcon icon={faDeviantart} />
      </Link>
    </div>
  )
}
