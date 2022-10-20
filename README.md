<h1 align="center">Paco Panda Drawing Stats</h1>

![Repo banner](https://user-images.githubusercontent.com/94678583/172738303-a8bd2b6c-4f8f-49e1-ade1-ce7225d636b4.png)

![MIT License](https://img.shields.io/badge/license-MIT-336600)
[![issues - pacopanda-drawing-stats](https://img.shields.io/github/issues/skepfusky/pacopanda-drawing-stats)](https://github.com/skepfusky/pacopanda-drawing-stats/issues)
![](https://img.shields.io/github/last-commit/skepfusky/pacopanda-drawing-stats)
![](https://img.shields.io/github/contributors/skepfusky/pacopanda-drawing-stats)

> 🆕 [Changelog](https://github.com/skepfusky/pacopanda-drawing-stats/blob/main/CHANGELOG.md)

__Paco Panda Drawing Stats__ is an open source data visualization project that collects all 1.8K+
drawings from a furry artist and illustrator *pandapaco*, written in
TypeScript and Python.

This project currently uses Next.js with Sass and Tailwind CSS, it previously
uses Vue 3 and had to be rewritten entirely in React because of the wide range of libraries
available and its widespead support.

The backend consists Python for scraping data with FastAPI.

It iss deployed on Vercel and DigitalOcean respectively.

## Project structure

- `.github` - For GitHub automation stuff for updating npm packages, update drawing
data, etc.
- `.idea` and `.vscode` - IDE configs for VS Code and IntelliJ IDEA
- `app` - The website, written in Next.js + TypeScript, Sass, and Tailwind CSS
- `script` - Bash scripts for setting up, bulk linting and for deployment
- `server` - FastAPI backend

## About this project

This project began on October 31, 2021, and the possible inspiration from this
project is through McBroken (basically a McDonald's broken ice cream machine site)
and it'd be interesting to see in all of his drawings to see said data and it's various
datasets.

This project collects the following:

- The title and date of the piece
- Number of character(s) species and names
- Media type (either drawn digital or traditional)
- Programs/mediums used (i.e. Photoshop, Procreate, etc.)
- The source where I got the data from (either from FurAffinity or from DeviantArt)

Previously, I have to manually source it through FurAffinity and DeviantArt for his draft
drawings (including his *Art & Biro* comics). Unfortunately, drawings from
Twitter won't be counted in order to ease the load on my end and the dataset
as well since all the data gathered will be hardcoded to the site.

### Why did you create this project?

It's really not my intention to impress him in general, I'm just a huge fan of his
artwork and his unique and adorable art style that I'd want to see how many characters
he's drawn since early to mid 2000s but he'd for sure find it interesting as it's more of
a fun project to a new hobby of mine, learning not only JavaScript, but also learning
a bit of back-end and basic data management in the process of other projects I do.

Initially, I wanted to show realtime data from Google Sheets and render data via
a chart library from a website and I'd thought I'll take one of my favorite
artists and run it through this process, but I'm kinda lacking backend knowledge
 and I needed a help with [@thatITfox][it] for setting up a Flask web server.

### Isn't this taking it too far?

Well, as someone who admires his art, yes... to some extent. Well, sure - it may feel
like I watch him on every step, but trust me, I only use them for analytical and
informational purposes; parsing drawing data on his Twitter profile would be difficult
and will require more work.

To be honest, it's more of a serious, yet passion project of mine to show various
kinds of drawing data from his.

## Installation and setup

### Prerequisites

- Node.js v16 or higher (LTS recommended)
- Python 3.9 or higher
- WSL/Git Bash (for Windows users required to execute Bash scripts)

### Running the dev server

- Install both Node and Python environments by executing `sh scripts/setup.sh`.
- Run both servers by `yarn dev` or `npm run dev`.
  - Run them seperately by running `yarn dev:next` for the Next.js app or
    `yarn dev:fastapi` for the FastAPI back-end.

## Generating data locally

From the `server/fa-scraper.py` file, there are two parameters you can pass:

> **Warning**
> Remember that you should __always__ run the script in the `server`
> directory! That way, the `api.py` can read the JSON file - as opposed to
> running it directly from VS Code.

- `-p <number>`, `--pages <number>`: Specify what pages to scrape, each page
contains 48 items. If this parameter isn't set, it will scan through all the
pages available.
- `-nv`, `--no-verbose`: Keep the logs as minimal and clean as possible, making
the requests go by faster.

## License

Source code licensed under MIT; Other third-party content licensed under CC-BY-SA 4.0

[it]: https://github.com/thatITfox
