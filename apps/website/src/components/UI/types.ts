type States = "warning" | "error" | "info"

interface UI {
  children?: React.ReactNode
  className?: string
  style?: string
  disabled?: boolean
  a11yTitle?: string
}

export interface ButtonTypes extends UI {
  onClick?: () => void
  rounded?: boolean
}

export interface LinkTypes extends Pick<UI, "children" | "disabled"> {
  href?: string
  newTab?: boolean
}

export interface Cards extends Pick<UI, "children"> {
  heading?: string
  state: States
}