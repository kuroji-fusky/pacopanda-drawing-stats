export default function useSEO({
  title,
  description,
  image,
}: {
  title: string
  description: string
  image?: string
}) {
  useSeoMeta({
    title,
    description,
    ogTitle: title,
    ogDescription: description,
  })

  useHead({
    link: [{ rel: "canonical", href: "something" }],
  })
}
