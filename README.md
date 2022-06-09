<h1 align="center">Panda Paco Drawing Stats</h1>

![MIT License](https://img.shields.io/badge/license-MIT-336600)
[![issues - pandapaco-drawing-stats](https://img.shields.io/github/issues/skepfusky/pandapaco-drawing-stats)](https://github.com/skepfusky/pandapaco-drawing-stats/issues)

This is an open source data visualization project that collects all 1.8K+
drawings from a furry artist and illustrator *pandapaco*, written in
TypeScript and Python.

For more in-depth and thorough explanation on how I gather, render, and manage
data, go [here!][notebook]

![Repo banner](https://user-images.githubusercontent.com/94678583/172738303-a8bd2b6c-4f8f-49e1-ade1-ce7225d636b4.png)

## Technology stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=react,nextjs,ts,tailwind,sass,py,fastapi,redis">
</p>

I use Python to gather a bunch of data, while FastAPI for the back-end, and
special thanks to [@thatITfox][it] for initially setting up the backend with Flask!
And Next.js for the website as a whole. Previously written in Vue.js.

## Project structure

- `app` - The website, written in Next.js + TypeScript, Sass, and TailwindCSS
- `data` - An old folder used to parse data and is used for [notebook][notebook] output
only
- `script` - Bash scripts for bulk linting and for deployment
- `server` - Python FastAPI back-end

## About this project

This project began in October 31, 2021, and the possible inspiration from this
project is through McBroken (basically a McDonald's broken ice cream machine site)
and it'd be interesting to see in all of his drawings to see said data and it's various
datasets.

This project collects the following:

- The title and date of the piece
- Number of character(s) species and names
- Media type (either drawn digital or traditional)
- Programs/mediums used (i.e. Photoshop, Procreate, etc.)
- The source where I got the data from (either from FurAffinity or from DeviantArt)

I have to manually source it through FurAffinity and DeviantArt for his draft
drawings (including his *Art & Biro* comics). Unfortunately, drawings from
Twitter won't be counted in order to ease the load on my end and the dataset
as well since all the data gathered will be hardcoded to the site.

## Stuff you might be wondering

### Why did you create this project?

It's really not my intention to impress him in general, I'm just a huge fan of his
artwork and his unique and adorable art style that I'd want to see how many characters
he's drawn since mid-2000s but he'd for sure find it interesting as it's more of
a fun project to a new hobby of mine, learning not only JavaScript, but also learning
a bit of back-end and basic data management in the process of other projects I do.

Initially, I wanted to show realtime data from Google Sheets and render data via
a chart library from a website and I'd thought I'll take one of my favorite
artists and run it through this process, but I'm kinda lacking backend knowledge
 and I needed a help with [@thatITfox][it] for setting up a Flask web server.

### Isn't this taking it too far?

Well, as someone who admires his art, yes - to some extent. Well, sure - it may feel
like I watch him on every step, but trust me, I only use them for analytical and
informational purposes; parsing drawing data on his Twitter profile would be difficult.

To be honest, it's more of a serious, yet passion project of mine to show various
kinds of drawing data from his.

## Related projects

- [Art & Biro Comic Recreated](https://github.com/skepfusky/art-and-biro-comic-remastered)

## License

MIT

[it]: https://github.com/thatITfox
[notebook]: https://github.com/skepfusky/pandapaco-drawing-stats/blob/main/data/paco-drawing-data.ipynb
