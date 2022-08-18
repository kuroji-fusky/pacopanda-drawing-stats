import Head from "next/head"
import Header from "../base/Header"
import Footer from "../base/Footer"

export default function Layout({ children }: any) {
  return (
    <>
      <Header />
      {children}
      <Footer />
    </>
  )
}
