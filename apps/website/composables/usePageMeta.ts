import { UseSeoMetaInput } from "@unhead/vue"

interface PageMetaProps {
	title: string
	description?: string
}

export function usePageMeta({ title, description }: PageMetaProps) {
	const router = useRoute()
	const SITE_NAME = "Paco Drawing Stats"

	const parseTitle = router.fullPath !== "/" ? `${title} - ${SITE_NAME}` : title

	const metaTags: UseSeoMetaInput = {
		title: parseTitle,
		description: description,
		ogTitle: title,
		ogDescription: description,
		ogType: "website",
		twitterTitle: title,
		twitterDescription: description,
	}

	useSeoMeta(metaTags)
}
