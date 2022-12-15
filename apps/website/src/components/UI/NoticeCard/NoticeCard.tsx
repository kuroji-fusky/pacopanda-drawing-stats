import { CardProps } from "../types"
import styles from "./NoticeCard.module.scss"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import {
  faTimesCircle,
  faWarning,
  faInfoCircle
} from "@fortawesome/free-solid-svg-icons"

export function NoticeCard(props: CardProps) {
  const statesMap = {
    error: { class: styles["error-card"], icon: faTimesCircle },
    warning: { class: styles["warning-card"], icon: faWarning },
    info: { class: styles["info-card"], icon: faInfoCircle }
  }

  const cardStyles = statesMap[props.state].class
  const cardIcons = statesMap[props.state].icon

  return (
    <div aria-label={props.heading} className={cardStyles}>
      <FontAwesomeIcon icon={cardIcons} size="xl" className={styles["icon"]} />
      <div>
        {props.heading && (
          <h2 className={styles["heading"]}>{props.heading}</h2>
        )}
        {props.children}
      </div>
    </div>
  )
}
