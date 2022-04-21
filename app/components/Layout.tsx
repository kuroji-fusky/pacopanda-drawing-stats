import Head from "next/head"
import Header from './Header'
import Footer from './Footer'

export default function Layout({ children }: any) {
  return (
    <>
      <Head>
        <meta charSet="utf-8" />
        <meta name="viewport" content="initial-scale=1.0, width=device-width" />
        <meta httpEquiv="X-UA-Compatible" content="IE=edge" />
      </Head>
      <Header />
      <main>
        {children}
      </main>
      <Footer />
    </>
  )
}