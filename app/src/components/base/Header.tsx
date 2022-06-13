import { useRouter } from "next/router";
import Link from "next/link";
import styles from "@/styles/base/Layout.module.scss";

export default function Header() {
  return (
    <header>
      <div className={`${styles["content-wrapper"]} py-5`}>
        {/* <img src="/static/images/logo.png" alt="logo" /> */}
        <nav className="flex gap-x-6">
          <LinkGroup name="Home" route="" />
          <LinkGroup name="Browse data" route="data" />
          <LinkGroup name="API" route="stats-api" />
          <LinkGroup name="About this project" route="about" />
        </nav>
      </div>
    </header>
  );
}

interface ILinkGroupProps {
  route: string
  name: string
  children?: any
}

export function LinkGroup({ route, name, children }: ILinkGroupProps) {
  const router = useRouter();

  return (
    <Link href={`/${route}`} passHref>
      <a className={router.pathname === `/${route}` ? "active" : ""}>
        <span>{name}</span>
        {children}
      </a>
    </Link>
  );
}
