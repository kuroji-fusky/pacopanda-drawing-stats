import Link from "next/link";
import { useRouter } from "next/router";

export function Navbar() {
  return (
    <header className="px-6 py-5">
      <nav className="flex justify-center gap-5">
        <DefaultLink href="/" name="Home" />
        <DefaultLink href="/about" name="About" />
      </nav>
    </header>
  );
}

function DefaultLink(props: { href: string; name: string }) {
  const router = useRouter();

  return (
    <Link href={props.href ?? ""}>
      <a className={router.pathname === props.href ? "text-purple-700" : ""}>
        {props.name ?? ""}
      </a>
    </Link>
  );
}
