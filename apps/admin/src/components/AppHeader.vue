<script setup lang="ts">
import { ref } from "vue"

const currentDataSource = ref<string>("Redis")
const connectionSources = ["Redis", "Local JSON", "Docker"]
</script>

<template>
	<div
		class="w-full flex justify-between items-center px-6 py-4 bg-neutral-950"
		:aria-label="`Admin dashboard, current connected source: ${currentDataSource}`"
	>
		<span class="font-inter text-2xl select-none">Admin Dashboard</span>
		<div class="flex gap-x-5 text-lg">
			<span class="py-1.5"> Data Source </span>
			<div
				class="relative group py-1.5 rounded-md px-4 border-neutral-600 border"
			>
				{{ currentDataSource }}
				<div
					class="py-4 right-0 opacity-0 transition-all group-hover:opacity-100 absolute top-10 pointer-events-none group-hover:pointer-events-auto"
				>
					<ul class="bg-neutral-700 rounded-md w-max">
						<li
							class="px-4 py-2.5"
							v-for="(item, index) in connectionSources"
							:key="index"
						>
							{{ item }}
						</li>
					</ul>
				</div>
			</div>
		</div>
	</div>
</template>
