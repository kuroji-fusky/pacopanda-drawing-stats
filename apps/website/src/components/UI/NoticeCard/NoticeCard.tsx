import { Cards } from "../types"
import styles from "./NoticeCard.module.scss"

export function NoticeCard(props: Cards) {
  const CardStates = {
    info: styles["info"],
    warning: styles["warning"],
    error: styles["error"],
  }

  return (
    <div aria-label={props.heading}>
      <div>
        {props.heading && <h2>{props.heading}</h2>}
        {props.children}
      </div>
    </div>
  )
}
