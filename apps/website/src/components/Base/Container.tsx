import Head from "next/head"
import { useRouter } from "next/router"
import { LayoutProps } from "./Layout"

interface ContainerProps extends LayoutProps {
  t: string
  d: string
  wrap?: boolean
}

export default function Container(props: ContainerProps) {
  const router = useRouter()

  const SITE_TITLE = "Paco Drawing Stats by Kuroji Fusky"

  const titleParser = `${props.t} | ${SITE_TITLE}`
  const parseUrl = `https://pandapaco-drawing-stats.kurofusky.xyz${router.asPath}`

  return (
    <>
      <Head>
        <title>{titleParser}</title>
        <meta name="description" content={props.d} />
        <meta property="og:title" content={titleParser} />
        <meta property="og:description" content={props.d} />
        <meta name="twitter:title" content={titleParser} />
        <meta name="twitter:description" content={props.d} />
        <meta name="twitter:url" content={parseUrl} />
        <meta property="og:url" content={parseUrl} />
        <link rel="canonical" href={parseUrl} />
      </Head>
      <main>{props.children}</main>
    </>
  )
}
