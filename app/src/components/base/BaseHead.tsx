import Head from "next/head"
import { useRouter } from "next/router"

export default function BaseHead({ title, description }: IBaseHeadProps) {
  const router = useRouter()
  const SITE_TITLE = "Paco Drawing Stats"
  const TITLE_ROOT = `${title} | ${SITE_TITLE}`
  const url = `https://pacopanda-drawing-stats.skepfusky.xyz${router.pathname}`

  return (
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
  )
}
