import Head from "next/head"
import Header from './Header'
import Footer from './Footer'

interface ILayout {
  mainClassName: string
  children: React.ReactNode
}

export default function Layout({ children, mainClassName }: ILayout) {
  return (
    <>
      <Head>
        <meta charSet="utf-8" />
        <meta name="viewport" content="initial-scale=1.0, width=device-width" />
        <meta httpEquiv="X-UA-Compatible" content="IE=edge" />
      </Head>
      <Header />
      <main className={mainClassName}>
        {children}
      </main>
      <Footer />
    </>
  )
}