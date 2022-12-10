![Banner for Paco Panda Drawing Stats](https://user-images.githubusercontent.com/94678583/203912229-9b6c2479-e999-4b36-9d54-205037691d18.png)

<h1 align="center">Paco Panda Drawing Stats</h1>

![MIT License](https://img.shields.io/badge/license-MIT-336600)
[![issues - pacopanda-drawing-stats](https://img.shields.io/github/issues/skepfusky/pacopanda-drawing-stats)](https://github.com/skepfusky/pacopanda-drawing-stats/issues)
![](https://img.shields.io/github/last-commit/skepfusky/pacopanda-drawing-stats)
![](https://img.shields.io/github/contributors/skepfusky/pacopanda-drawing-stats)

**Paco Panda Drawing Stats** is a data visualization project that collects
drawings from a furry artist and illustrator Paco Panda.

Made simply out of curiousity - it also has standalone libraries for both
JavaScript and Python including its own REST and GraphQL APIs, and utilizes Redis
as the main and in-memory database for its speed and persistency.

## Project structure

> **Note**
> This project is a **monorepo**; it has nested directories to isolate Python and
> Node.js codebases separately.

- `.github` - For GitHub automation stuff for updating npm packages, update drawing
  data, etc.
- `apps`
  - `website` - The website written in Next.js w/ TypeScript + Tailwind CSS
- `python`
  - `gql` - The GraphQL API
  - `scraper` - A web scraper to gather new data

## Setup and Installation

### Prerequisites

- Node.js v16 or higher (LTS recommended)
- Yarn Package Manager
- Python 3.10 or higher
- WSL/Git Bash (for Windows users required to execute Bash Shell scripts)

### Installation (Node)

- Install Node dependencies with `yarn install` or just simply `yarn`, that's it!

### Installation (Python)

- Go to the `python` directory and set up a virtual environment

```bash
# Setup venv
python -m venv env

# FOR WINDOWS
./env/Scripts/activate

# FOR LINUX
source env/bin/activate
```

- Then install its dependencies

```bash
pip install -r requirements.txt
```

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
drawings (including his _Art & Biro_ comics). Unfortunately, drawings from
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

To be honest, it's more of a serious, yet passion side-project of mine to show various
kinds of drawing data from his.

## License

Its source code licensed under MIT; Other third-party content licensed under CC-BY-SA 4.0

[it]: https://github.com/thatITfox
