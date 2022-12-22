import "@styles/globals.scss"
import { Layout } from "@components/Base"
import type { AppProps } from "next/app"

import "@fortawesome/fontawesome-svg-core/styles.css"
import { config } from "@fortawesome/fontawesome-svg-core"
config.autoAddCss = false

import { Inter, JetBrains_Mono, Open_Sans } from "@next/font/google"
import useAppendHTML from "hooks/useAppendHTML"

const inter = Inter({
  variable: "--font-inter",
  subsets: ["latin"],
  preload: true
})

const sans = Open_Sans({
  variable: "--font-open-sans",
  subsets: ["latin"],
  preload: true
})

const jetbrains = JetBrains_Mono({
  variable: "--font-jetbrains",
  subsets: ["latin"]
})

export default function App({ Component, pageProps }: AppProps) {
  useAppendHTML(inter.variable, sans.variable, jetbrains.variable)
  return (
    <Layout>
      <Component {...pageProps} />
    </Layout>
  )
}
