import Head from "next/head"
import { BaseHeadProps } from "@/models/Interfaces"

export default function BaseHead({ title, description }: BaseHeadProps) {
  const siteTitle = "Paco Drawing Stats"
  const titleGlobal = `${title} | ${siteTitle}`
  
  return (
    <Head>
      <meta name="title"content={titleGlobal} />
      <meta name="description" content={description} />
      <meta property="og:type" content="website" />
      <meta property="og:title" content={titleGlobal} />
      <meta property="og:description" content={description} />
      <meta name="twitter:card" content="summary_large_image" />
      <meta name="twitter:title" content={titleGlobal} />
      <meta name="twitter:description" content={description} />
      <title>{titleGlobal}</title>
    </Head>
  )
}
