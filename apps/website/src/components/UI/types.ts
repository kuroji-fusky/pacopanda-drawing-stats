type UIStates = "error" | "warning" | "info"

export interface ClickableUI<T = HTMLElement> {
  children?: React.ReactNode
  className?: string
  style?: string
  disabled?: boolean
  tooltip?: string
  onHover?: React.MouseEventHandler<T>
  onClick?: React.MouseEventHandler<T>
  onTap?: React.TouchEventHandler<T>
}

export interface ButtonProps extends ClickableUI<HTMLButtonElement> {
  rounded?: boolean
}

export interface LinkProps extends Pick<ClickableUI, "children"> {
  href?: string
  newTab?: boolean
}

type OmitForCardProps = Pick<ClickableUI<undefined>, "children" | "tooltip">

export interface CardProps extends OmitForCardProps {
  heading?: string
  state: UIStates
}
