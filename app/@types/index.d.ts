declare type Themes = "light" | "dark" | "default"

declare type OptionsCtxTypes = {
  expand: boolean
  theme: Themes
  setExpand: (expand: boolean) => void
  setTheme: (theme: Themes) => void
}

declare interface ILayoutProps {
  children?: React.ReactNode
}

declare interface IBaseHeadProps extends ILayoutProps {
  title: string
  description: string
}

declare interface ILinkGroupProps extends ILayoutProps {
  route: string
  name: string
}
