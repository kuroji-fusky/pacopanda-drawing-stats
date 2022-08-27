import Head from "next/head"
import { useRouter } from "next/router"
import styles from "@/styles/base/Layout.module.scss"

export default function BaseHead({
  title,
  description,
  children,
  wrap
}: IBaseHeadProps) {
  const router = useRouter()
  const SITE_TITLE = "Paco Drawing Stats"
  let TITLE_ROOT = `${title} | ${SITE_TITLE}`
  const url = `https://pacopanda-drawing-stats.skepfusky.xyz${router.pathname}`

  if (router.pathname === "/") TITLE_ROOT = SITE_TITLE

  return (
    <>
      <Head>
        <meta name="title" content={TITLE_ROOT} />
        <meta name="description" content={description} />
        <meta property="og:type" content="website" />
        <meta property="og:title" content={TITLE_ROOT} />
        <meta property="og:description" content={description} />
        <meta property="og:url" content={url} />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content={TITLE_ROOT} />
        <meta name="twitter:description" content={description} />
        <meta name="twitter:url" content={url} />
        <link rel="canonical" href={url} />
        <title>{TITLE_ROOT}</title>
      </Head>
      {wrap ? (
        <main id={styles.wrap}>{children}</main>
      ) : (
        <main>{children}</main>
      )}
    </>
  )
}
