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

  return (
    <>
      <Head>
        <title>{titleParser}</title>
        <meta name="description" content={props.d} />
        <meta property="og:title" content={titleParser} />
        <meta property="og:description" content={props.d} />
        <meta name="twitter:title" content={titleParser} />
        <meta name="twitter:description" content={props.d} />
      </Head>
      <main>{props.children}</main>
    </>
  )
}
