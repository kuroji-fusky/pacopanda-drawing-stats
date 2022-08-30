import type { AppProps } from "next/app"
import Head from "next/head"
import { library, config } from "@fortawesome/fontawesome-svg-core"
import { MDXProvider } from "@mdx-js/react"
import { fas } from "@fortawesome/free-solid-svg-icons"
import { fab } from "@fortawesome/free-brands-svg-icons"
import "@fortawesome/fontawesome-svg-core/styles.css"
import "@/styles/globals.scss"
import Layout from "@/components/base/Layout"

const components = {
  h1: (props: any) => <h1 {...props} className="my-3" />,
  h2: (props: any) => <h2 {...props} className="my-3" />,
  ul: (props: any) => <ul {...props} className="list-disc list-inside" />,
  a: (props: any) => <a {...props} className="hover:underline text-green-700" />
}

config.autoAddCss = false
library.add(fas)
library.add(fab)

export default function PandaPacoStatsApp({ Component, pageProps }: AppProps) {
  return (
    <>
      <Head>
        <meta charSet="utf-8" />
        {/* prettier-ignore */}
        <meta name="viewport" content="user-scalable=no, width=device-width, initial-scale=1, maximum-scale=1" />
        <meta httpEquiv="X-UA-Compatible" content="IE=edge" />
      </Head>
      <Layout>
        <MDXProvider components={components}>
          <Component {...pageProps} />
        </MDXProvider>
      </Layout>
    </>
  )
}
