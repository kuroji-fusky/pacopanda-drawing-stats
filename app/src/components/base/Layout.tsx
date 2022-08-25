import { createContext, useState, useEffect } from "react"
import Header from "./Header"
import Footer from "./Footer"

export default function Layout({ children }: ILayoutProps) {
  const [theme, setTheme] = useState<Themes>("default")
  const [expand, setExpand] = useState(false)

  const OptionsContext = createContext<OptionsCtxTypes>({
    expand: false,
    theme: "default",
    setExpand: () => {},
    setTheme: () => {}
  })

  if (typeof window !== "undefined") {
    const themeOverrideHandler = (theme: Themes) => {
      localStorage.setItem("theme", theme)
      document.body.setAttribute("theme-override", theme)
    }

    themeOverrideHandler("default")
  }

  return (
    <OptionsContext.Provider value={{ theme, setTheme, expand, setExpand }}>
      <Header />
      {children}
      <Footer />
    </OptionsContext.Provider>
  )
}
