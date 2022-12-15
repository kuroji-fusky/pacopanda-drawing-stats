import { ButtonProps } from "../types"

export function Button(props: ButtonProps) {
  return (
    <button
      aria-label={props.tooltip}
      className={props.className}
      onClick={props.onClick}
    >
      {props.children}
    </button>
  )
}
