type CombinedArray<T> = T | T[]

export type ExplicitSpecies = Capitalize<
	| "pup"
	| "cat"
	| "dog"
	| "fox"
	| "raccoon"
	| "wolf"
	| "otter"
	| "ferret"
	| "hyena"
	| "coyote"
	| "bear"
	| "panda"
	| "mouse"
	| "lion"
	| "tiger"
	| "Snow Leopard"
	| "rabbit"
>

type Species = CombinedArray<ExplicitSpecies> & CombinedArray<string>

export interface Character {
	name: string
	fullName: string
	species: Species
	hybrid?: boolean
	appearances: {
		count: number
		artworks: Array<{
			title: string
			slug: string
		}>
	}
}

export interface Artwork {
	title: string
	description?: string
	publishDate: string
	year: number
	characters: Array<{
		name: string
		species: Species
		slug: string
	}>
	sources: {
		deviantArt: string
		furAffinity: string
		weasyl: string
		[key: string]: string
	}
}
