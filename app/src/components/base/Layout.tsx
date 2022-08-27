import { createContext, useState, useEffect } from "react"
import Navbar from "./Navbar"
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
      {/* <Navbar /> */}
      {children}
      {/* <Footer /> */}
      <footer className="text-center py-9">
        <p>
          Project licensed under MIT. Media content licensed under CC-BY-SA 4.0.
        </p>{" "}
        <p>Copyright &copy; 2014-{new Date().getFullYear()} skepfusky</p>{" "}
      </footer>
    </OptionsContext.Provider>
  )
}
