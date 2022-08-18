import { useRouter } from "next/router"
import Link from "next/link"
import styles from "@/styles/base/Layout.module.scss"
import { HeaderLinkMenu } from "@/models/Menus"

export default function Header() {
  return (
    <header>
      <div className={`${styles["content-wrapper"]} py-5`}>
        {/* <img src="/static/images/logo.png" alt="logo" /> */}
        <nav className="flex gap-x-6">
          {HeaderLinkMenu.map((item, index) => (
            <LinkGroup key={index} name={item.name} route={`/${item.route}`} />
          ))}
        </nav>
      </div>
    </header>
  )
}

export function LinkGroup({ route, name, children }: ILinkGroupProps) {
  const router = useRouter()

  return (
    <Link href={`/${route}`} passHref>
      <a className={router.pathname === `/${route}` ? "active" : ""}>
        <span>{name}</span>
        {children}
      </a>
    </Link>
  )
}
