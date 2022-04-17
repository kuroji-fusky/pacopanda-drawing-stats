import '../styles/globals.scss'
import type { AppProps } from 'next/app'
import Layout from '../components/Layout'

export default function PandaPacoStatsApp({ Component, pageProps }: AppProps) {
  return (
    <Layout>
      <Component {...pageProps} />
    </Layout>
  )
}
