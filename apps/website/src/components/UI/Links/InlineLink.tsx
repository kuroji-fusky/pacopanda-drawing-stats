import Link from "next/link";
import { LinkProps } from "../types";
import styles from "./InlineLink.module.scss"

export function InlineLink(props: LinkProps) {
  return <Link href={props.href ?? ""}>
    {props.children}
  </Link>
}