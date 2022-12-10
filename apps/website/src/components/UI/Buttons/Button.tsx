import { ButtonTypes } from "../types"

export function Button(props: ButtonTypes) {
  return (
    <button
      aria-label={props.a11yTitle}
      className={props.className}
      onClick={props.onClick}
    >
      {props.children}
    </button>
  )
}
