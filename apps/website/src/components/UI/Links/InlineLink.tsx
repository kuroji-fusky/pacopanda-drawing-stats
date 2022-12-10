import Link from "next/link";
import { LinkTypes } from "../types";
import styles from "./InlineLink.module.scss"

export function InlineLink(props: LinkTypes) {
  return <Link href={props.href ?? ""}>
    {props.children}
  </Link>
}