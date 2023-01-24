<template>
    <footer>
        <div id="wrapper">
            <article>
                <p>
                    <strong>DISCLAIMER:</strong>
                    This is an passion open source project created by an individual; I do not own nor claim any of the
                    third-party
                    content from this site - neither it is stored from the database whatsoever. Before 2019, he stopped
                    licensing his work under Creative Commons on DeviantArt. Most of
                    the artwork
                    presented on this website is primarily for informational and analytical purposes.
                </p>
            </article>
            <div class="grid py-5 text-center place-items-center">
                <span>
                    Copyright &copy;
                    2021-{{ year }}
                    Kuroji Fusky; project source code licensed under
                    <nuxt-link to="https://opensource.org/licenses/MIT">MIT</nuxt-link>
                </span>
            </div>
        </div>
    </footer>
</template>

<script setup lang="ts">
const year = new Date().getFullYear()
</script>

<style scoped>
#wrapper {
    @apply px-12;
}
</style>