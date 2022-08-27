import { useRouter } from "next/router"
import styles from "@/styles/base/LinkComponent.module.scss"
import Link from "next/link"

export default function LinkGroup({ route, name, children }: ILinkGroupProps) {
  const router = useRouter()

  const styleRoute =
    router.pathname === route
      ? styles["link-active"].toString()
      : styles.link.toString()

  return (
    <Link href={route} passHref>
      <a className={styleRoute}>
        <span>{name}</span>
        {children}
      </a>
    </Link>
  )
}
