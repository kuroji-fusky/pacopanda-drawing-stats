import Head from "next/head"
import Header from '../base/Header'
import Footer from '../base/Footer'

export default function Layout({ children }: any) {
  return (
    <>
      <Head>
        <meta charSet="utf-8" />
        <meta name="viewport" content="initial-scale=1.0, width=device-width" />
        <meta httpEquiv="X-UA-Compatible" content="IE=edge" />
        <link rel="preconnect" href="https://fonts.gstatic.com/" crossOrigin="" />
        <link rel="preconnect" href="https://fonts.googleapis.com/" crossOrigin="" />
      </Head>
      <Header />
      {children}
      <Footer />
    </>
  );
}