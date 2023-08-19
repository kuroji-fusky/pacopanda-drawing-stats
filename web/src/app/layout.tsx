import "./globals.css"
import type { Metadata } from "next"
import { Inter, Open_Sans } from "next/font/google"

const inter = Inter({
  subsets: ["latin-ext", "cyrillic-ext"],
  variable: "--heading",
  preload: true
})

const open_sans = Open_Sans({
  subsets: ["latin-ext", "cyrillic-ext"],
  variable: "--body",
  preload: true
})

export const metadata: Metadata = {
  title: {
    template: "%s - Paco Drawing Stats by Kuroji Fusky",
    default: "Home"
  },
  description: "...something here",
  robots: "noai, noimageai"
}

export default function RootLayout({
  children
}: {
  children: React.ReactNode
}) {
  return (
    <html
      lang="en"
      dir="ltr"
      className={`${inter.variable} ${open_sans.variable}`}
    >
      <body>{children}</body>
    </html>
  )
}
