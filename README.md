<h1 align="center">Paco Panda Drawing Stats</h1>

![Banner for Paco Panda Drawing Stats](https://user-images.githubusercontent.com/94678583/208869784-c68b5483-8e18-4d01-9163-d502b4cb40c5.png)

![license - pacopanda-drawing-stats](https://img.shields.io/github/license/kuroji-fusky/pacopanda-drawing-stats?color=336600)
[![issues - pacopanda-drawing-stats](https://img.shields.io/github/issues/kuroji-fusky/pacopanda-drawing-stats)](https://github.com/kuroji-fusky/pacopanda-drawing-stats/issues)
![](https://img.shields.io/github/last-commit/kuroji-fusky/pacopanda-drawing-stats)
![](https://img.shields.io/github/contributors/kuroji-fusky/pacopanda-drawing-stats)

**Paco Panda Drawing Stats** is a data analysis and data visualization project
that collects and parses drawing data from a furry artist and illustrator Paco
Panda.

Initially made simply out of curiousity - it has expanded to provide its own
REST and GraphQL APIs, and utilizes Redis as the main and in-memory database for
its speed and persistency.

## Project structure

This project is a [**monorepo**](https://monorepo.tools/#what-is-a-monorepo), it
uses Yarn workspaces and Turborepo to install and manage dependencies in each
subdirectory and remotely cache builds on the cloud. The entire project uses the
ES Module syntax, with some files utilize the `.cjs` for Tailwind and PostCSS
configs.

- `.github` - CI Workflow stuff such as type-checking, linting, etc.
- `apps`
  - `admin` - A Tauri admin app for managing stuff (Rust required)
  - `api` - API for both REST and GraphQL
  - `website` - The website written in Nuxt 3 + Tailwind CSS
- `shared`
  - `config` - Other configs like Tailwind and others
  - `types` - Shared TypeScript declarations
  - `tsconfig` - Shared TypeScript config
- `scripts` - Script(s) for reinstalling packages
  - `scraper` - For scraping public data using Puppeteer and Cheerio, previously
    used Python with BeautifulSoup

## Setup and Installation

### Prerequisites

- Node.js versions 18 or higher (LTS recommended)
- Rust (for running and compiling admin app; `cargo 1.65.0` or higher)
- Yarn Package Manager
- [Optional] WSL/Git Bash (for Windows users required to execute Shell scripts)

### Installation

Install dependencies with Yarn

```console
yarn install
```

Clone the .env files

```console
cp apps/website/.env.example apps/website/.env
cp apps/admin/.env.example apps/admin/.env
```

### Scripts

| Command       | Descrption                      | Directory         |
| ------------- | ------------------------------- | ----------------- |
| `dev:web`     | Open a website local dev server | `apps/website`    |
| `build:web`   | Build the website               | `apps/website`    |
| `preview:web` | Preview the website             | `apps/website`    |
| `puppeteer`   | Execute the Puppeteer script    | `scripts/scraper` |

## API

![API banner](https://user-images.githubusercontent.com/94678583/203912229-9b6c2479-e999-4b36-9d54-205037691d18.png)

> Section WIP

### Planned Endpoints

- `/character/:character?={query}`
- `/characters/?={query}`
- `/artwork/:year/:title?={query}`

## About this project

The project began on October 31, 2021, and the possible inspiration from this
project is through McBroken (basically a McDonald's broken ice cream machine
site) and it'd be interesting to see in all of his drawings to see said data and
it's various datasets.

This project collects the following:

- The title and date of the piece
- Number of character(s) species and names
- Media type (either drawn digital or traditional)
- Programs/mediums used (i.e. Photoshop, Procreate, etc.)
- The source where I got the data from (i.e. FurAffinity, DeviantArt, InkBunny,
  Weasyl, etc.)

Previously, I have to manually source it through FurAffinity and DeviantArt for
his draft drawings (including his _Art & Biro_ comics). Unfortunately, drawings
from Twitter won't be counted in order to ease the load on my end and the
dataset as well since all the data gathered will be hardcoded to the site.

### Why did you create this project?

Believe it or not, it's not my intention to impress him in general. I'm just a
huge fan of his artwork and his unique and adorable art style that I'd want to
see how many characters he's drawn since the early to mid-2000s but he'd for
sure find it interesting as it's more of a fun project to a new hobby of mine,
learning not only JavaScript but also learning a bit of back-end and basic data
management in the process of other projects I do.

Initially, I wanted to show realtime data from Google Sheets and render data via
a chart library from a website and I'd thought I'll take one of my favorite
artists and run it through this process.

In the early stages of this project - I have limited backend knowledge and I
needed a help with [@thatITfox][it] for setting up a Flask web server, and now
currently working with Redis stuff!

### Isn't this taking it too far?

As someone who admires his art, yes... to some extent. Well, sure - it may feel
like I watch him on every step, but trust me, I only use them for analytical and
informational purposes; parsing drawing data on his Twitter profile would be
difficult and will require more work.

It's more of a serious, yet passion side-project of mine to show various kinds
of drawing data from his.

### Are the images/drawings stored in the database?

No, most image requests are coming from FurAffinity since they use Cloudflare as
their CDN under the hood to cache media types.

## License

GPL-2.0

[it]: https://github.com/thatITfox
