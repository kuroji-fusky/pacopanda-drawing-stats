import Navbar from "./Navbar"
import Footer from "./Footer"

export interface LayoutProps {
  children?: React.ReactNode
}

export function Layout(props: LayoutProps) {
  return (
    <>
      <Navbar />
      {props.children}
      <Footer />
    </>
  )
}
