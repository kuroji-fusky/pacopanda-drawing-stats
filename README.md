<h1 align="center">Panda Paco Analytics Site</h1>

> Spanish translation of this README is available [here][es].
>
> La traducción española de este README está disponible [aquí][es].

> All raw data is stored in [this Google Sheet spreadsheet][sheet].

> For more in-depth and thorough explanation on how I gather, render, and manage
> data, refer to the [`paco-drawing-data.ipynb`][notebook] file.

<p align="center">
  <img src="https://github.com/skepfusky/pandapaco-art-statistics/blob/main/docs/project-banner-new.png?raw=true" alt="Repo banner">
</p>

This is a project that collects all 1.9K (and counting) drawings from a furry artist and
illustrator *pandapaco*. It displays different types of data (i.e species
drawn, expressions, number of characters drawn, etc, which are, for now,
probably, hard-coded unfortunately and have to be updated manually)

I use Google Sheets and some Python scripts to manage, parse, and plot
data and Next.js for the website as a whole.

## About this project

This project began in October 31, 2021, and the possible inspiration from this
project is through the McDonald's broken ice cream machine site and it'd be
interesting to see in all of his drawings to see said data and it's various
datasets.

As mentioned previously, this project collects the following:

- The title and date of the piece
- Number of character(s) species and names
- ~~Facial expressions~~ (dataset removed on March 13, 2022 because it was deemed too ambiguous and hard to distinguish a facial expression)
- Media type (either drawn digital or traditional)
- Programs/mediums used (added Feb 6, 2022)
- The source where I got the data from (either from FurAffinity or from DeviantArt)

I have to manually source it through FurAffinity and DeviantArt for his draft
drawings (including his *Art & Biro* comics). Unfortunately, drawings from
Twitter won't be counted in order to ease the load on my end and the dataset
as well since all the data gathered will be hardcoded to the site.

## Why did you create this project?

It's really not my intention to impress him in general, I'm just a big fan of his
artwork and his unique and adorable art style that I'd want to see how many characters
he's drawn since mid-2000s but he'd for sure find it interesting as it's more of a fun
project to a new hobby of mine, learning not only JavaScript, Vue.js, but also learning
a bit of back-end and basic data management in the process of other projects I do.

Previously, I wanted to show realtime data from Google Sheets and render data via a chart
library from a website and I'd thought I'll take one of my favorite artists and run it
through this process, but I'm kinda lacking backend knowledge.

## Other related projects

- [Art & Biro Recreated](https://github.com/skepfusky/art-and-biro-comic-vue3)

[es]: https://github.com/skepfusky/pandapaco-art-statistics/docs/readme_es.md
[pancon]: https://www.youtube.com/channel/UCTI9uf8OMcIo7QQMFS0Sfzw
[notebook]: https://github.com/skepfusky/pandapaco-art-statistics/blob/main/data/paco-drawing-data.ipynb
[sheet]: https://docs.google.com/spreadsheets/d/1fpNL-qbfZ53H-6WdqEB2X9rwn9QmM1porJqKgBC7rPk/edit?usp=sharing
