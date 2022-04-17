import Head from 'next/head'

interface BaseHeadProps {
  title: string;
  description: string;
}

const siteTitle = "pandapaco stats thing"

export default function BaseHead({ 
  title = "Title",
  description = "lol"
}: BaseHeadProps) {
  return (
    <Head>
      <meta name="description" content={description} />
      <meta property="og:site_name" content={siteTitle} />
      <meta property="og:title" content={title} />
      <meta property="og:description" content={description} />
      <meta name="twitter:card" content="summary_large_image" />
      <meta name="twitter:title" content={title} />
      <meta name="twitter:description" content={description} />
      <link rel="preconnect" href="https://fonts.gstatic.com/" />
      <link rel="preconnect" href="https://fonts.googleapis.com/" />
      <title>{title} • {siteTitle}</title>
    </Head>
  ); 
};