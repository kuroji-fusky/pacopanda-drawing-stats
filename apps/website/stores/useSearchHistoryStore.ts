import { defineStore } from "pinia"

interface SearchHistoryStore {
	items: Array<{
		query: string
		character?: string[]
		artwork?: string
		date: string
	}> &
	never[]
}

export const useSearchHistoryStore = defineStore("history", () => {
	state: (): SearchHistoryStore => {
		return {
			items: []
		}
	}
})
