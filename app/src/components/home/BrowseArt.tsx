import Link from "next/link"
import { FontAwesomeIcon as FaIcon } from "@fortawesome/react-fontawesome"
import { faDeviantart } from "@fortawesome/free-brands-svg-icons"

export default function BrowseArt() {
  return (
    <>
      <h2>Browse the art lol</h2>
      <Link href="deviantart.com" passHref>
        <a>
          <FaIcon icon={faDeviantart} />
        </a>
      </Link>
    </>
  )
}
