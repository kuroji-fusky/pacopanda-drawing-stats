export default function useSEO({
  title,
  description,
  image,
  card,
  type,
}: {
  title: string
  description: string
  image?: string
  card?: "summary" | "summary_large_image"
  type?: "website" | "article"
}) {
  const route = useRoute()
  const host = useRuntimeConfig().public.siteUrl || "http://localhost:3000"

  const parsedUrl = `${host}${route.fullPath}`

  useSeoMeta({
    title,
    description,
    ogTitle: title,
    ogDescription: description,
    ogImage: image,
    ogUrl: parsedUrl,
    ogType: type ?? "website",
    twitterCard: card ?? "summary",
    twitterCreator: "@kurojifusky",
  })

  useHead({
    link: [{ rel: "canonical", href: parsedUrl }],
  })
}
