import styles from "@/styles/base/Navbar.module.scss"
import LinkGroup from "./LinkGroup"
import { HeaderLinkMenu } from "@/models/Menus"

export default function Header() {
  return (
    <header id={styles.root}>
      <div id={styles.wrapper}>
        <nav className={styles["nav-wrapper"]}>
          {HeaderLinkMenu.map((item, index) => (
            <LinkGroup key={index} name={item.name} route={`/${item.route}`} />
          ))}
        </nav>
      </div>
    </header>
  )
}
