import type { AppProps } from "next/app"
import Head from "next/head"
import { library, config } from "@fortawesome/fontawesome-svg-core"
import { fas } from "@fortawesome/free-solid-svg-icons"
import { fab } from "@fortawesome/free-brands-svg-icons"
import "@fortawesome/fontawesome-svg-core/styles.css"
import "@/styles/globals.scss"
import Layout from "@/components/layouts/Default"

config.autoAddCss = false
library.add(fas)
library.add(fab)

export default function PandaPacoStatsApp({ Component, pageProps }: AppProps) {
  return (
    <>
      <Head>
        <meta charSet="utf-8" />
        <meta name="viewport" content="initial-scale=1.0, width=device-width" />
        <meta httpEquiv="X-UA-Compatible" content="IE=edge" />
        <link
          rel="preconnect"
          href="https://fonts.gstatic.com/"
          crossOrigin=""
        />
        <link
          rel="preconnect"
          href="https://fonts.googleapis.com/"
          crossOrigin=""
        />
      </Head>
      <Layout>
        <Component {...pageProps} />
      </Layout>
    </>
  )
}
