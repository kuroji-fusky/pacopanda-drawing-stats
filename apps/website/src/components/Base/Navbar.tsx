import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { faMagnifyingGlass } from "@fortawesome/free-solid-svg-icons"
import Link from "next/link"
import { Button } from "../UI"
import { ClickableUI } from "../UI/types"
import styles from "./Navbar.module.scss"
import useMobileOnly from "hooks/useMobileOnly"
import { useRouter } from "next/router"

export default function Navbar() {
  const mobile = useMobileOnly()

  return (
    <>
      <div className={styles["root-wrapper"]}>
        <header className={styles["container"]}>
          <div className={styles["logo-wrapper"]}>
            <Link href="/" className={styles["logo-title"]}>
              Paco Drawing Stats
            </Link>
            <Link
              href="https://kurofusky.xyz"
              target="_blank"
              rel="noopenner noreferrer"
              className={styles["logo-subtitle"]}
            >
              <span>Project by&nbsp;</span>
              <span className={styles["logo-kuroji-wordmark"]}>
                Kuroji Fusky
              </span>
            </Link>
          </div>
          <nav className={styles["nav-row"]}>
            <Button tooltip="Search icon" className={styles["nav-item-search"]}>
              <FontAwesomeIcon icon={faMagnifyingGlass} />
            </Button>
            <NavItem link="/browse">{!mobile ? "Browse Data" : "Browse"}</NavItem>
            <NavItem link="/docs/api">
              {!mobile ? "API Docs" : "API"}
              <WIPBadge />
            </NavItem>
            <NavItem link="/about">
              {!mobile ? "About the Project" : "About"}
            </NavItem>
          </nav>
        </header>
      </div>
    </>
  )
}

interface NavItemProps extends Pick<ClickableUI, "children" | "onClick"> {
  link: string
}

function NavItem(props: NavItemProps) {
  const router = useRouter()

  const routeActive =
    router.pathname === props.link
      ? styles["nav-item-active"]
      : styles["nav-item"]

  return (
    <Link className={routeActive} onClick={props.onClick} href={props.link}>
      {props.children}
    </Link>
  )
}

function WIPBadge() {
  return (
    <span className={styles["wip-badge"]} aria-hidden>
      WIP
    </span>
  )
}
