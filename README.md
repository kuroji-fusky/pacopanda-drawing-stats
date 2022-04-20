<h1 align="center">Panda Paco Analytics Site</h1>

> All raw data is stored in [this Google Sheet spreadsheet][sheet].

> For more in-depth and thorough explanation on how I gather, render, and manage
> data, click [here!][notebook]

<p align="center">
  <img src="https://github.com/skepfusky/pandapaco-art-statistics/blob/main/docs/project-banner-new.png?raw=true" alt="Repo banner">
</p>

This is a project that collects all 1.8K+ drawings from a furry artist and
illustrator *pandapaco*. It displays different types of data (i.e species
drawn, expressions, number of characters drawn, etc, which are, for now,
probably, hard-coded unfortunately and have to be updated manually)

## Technology stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=nextjs,ts,tailwind,sass,py,flask,firebase">
</p>

I use a Python scripts to do gather a bunch of data, while Flask and Firebase (probably) for the back-end
thanks to [@thatITfox](https://github.com/thatITfox) and Next.js for the website
as a whole. Previously Vue.js, but will be switched back to Vue once Nuxt 3 has a stable
release.

## About this project

This project began in October 31, 2021, and the possible inspiration from this
project is through McBroken (basically a McDonald's broken ice cream machine site)
and it'd be interesting to see in all of his drawings to see said data and it's various
datasets.

As mentioned previously, this project collects the following:

- The title and date of the piece
- Number of character(s) species and names
- Media type (either drawn digital or traditional)
- Programs/mediums used (i.e. Photoshop, Procreate, etc.)
- The source where I got the data from (either from FurAffinity or from DeviantArt)

I have to manually source it through FurAffinity and DeviantArt for his draft
drawings (including his *Art & Biro* comics). Unfortunately, drawings from
Twitter won't be counted in order to ease the load on my end and the dataset
as well since all the data gathered will be hardcoded to the site.

## Why did you create this project?

It's really not my intention to impress him in general, I'm just a big fan of his
artwork and his unique and adorable art style that I'd want to see how many characters
he's drawn since mid-2000s but he'd for sure find it interesting as it's more of a fun
project to a new hobby of mine, learning not only JavaScript, but also learning
a bit of back-end and basic data management in the process of other projects I do.

Initially, I wanted to show realtime data from Google Sheets and render data via a chart
library from a website and I'd thought I'll take one of my favorite artists and run it
through this process, but I'm kinda lacking backend knowledge and I needed a help with
[@thatITfox](https://github.com/thatITfox) for setting up a Flask web server.

## Other related projects

- [Art & Biro Recreated](https://github.com/skepfusky/art-and-biro-comic-vue3)

[notebook]: https://github.com/skepfusky/pandapaco-art-statistics/blob/main/data/paco-drawing-data.ipynb
[sheet]: https://docs.google.com/spreadsheets/d/1fpNL-qbfZ53H-6WdqEB2X9rwn9QmM1porJqKgBC7rPk/edit?usp=sharing
