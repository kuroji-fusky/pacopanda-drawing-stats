type CombinedArray<T> = T | T[]

export type ExplicitCommonSpecies = Capitalize<
  | "pup"
  | "cat"
  | "dog"
  | "fox"
  | "raccoon"
  | "wolf"
  | "hyena"
  | "coyote"
  | "bat"
  | "weasel"
  | "otter"
  | "ferret"
  | "bear"
  | "panda"
  | "mouse"
  | "lion"
  | "tiger"
  | "rabbit"
>

type Species = CombinedArray<ExplicitCommonSpecies> & CombinedArray<string>
type ArrayAppendSlug<T> = (T & { slug: string })[]

export interface Character {
  name: string
  fullName: string
  species: Species
  hybrid?: boolean
  appearances?: {
    count: number
    artworks: ArrayAppendSlug<{ title: string }>
  }
}

export interface Artwork {
  title: string
  description?: string
  publishDate: string
  year: number
  characters: ArrayAppendSlug<{
    name: string
    species: Species
    hybrid: boolean
  }>
  sources: {
    deviantArt: string
    furAffinity: string
    weasyl: string
    inkbunny: string
  } & Partial<{
    [key: string]: string
  }>
}
