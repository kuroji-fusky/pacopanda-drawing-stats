![Banner for Paco Panda Drawing Stats](https://user-images.githubusercontent.com/94678583/220274497-18b6a944-a759-469e-a10e-1d9b1ec6a95b.png)

![license - pacopanda-drawing-stats](https://img.shields.io/github/license/kuroji-fusky/pacopanda-drawing-stats?color=336600)
[![issues - pacopanda-drawing-stats](https://img.shields.io/github/issues/kuroji-fusky/pacopanda-drawing-stats)](https://github.com/kuroji-fusky/pacopanda-drawing-stats/issues)
![](https://img.shields.io/github/last-commit/kuroji-fusky/pacopanda-drawing-stats)
![](https://img.shields.io/github/contributors/kuroji-fusky/pacopanda-drawing-stats)

**Paco Panda Drawing Stats** is a data analysis and data visualization project
that collects and parses drawing data from a furry artist and illustrator Paco
Panda.

Initially made simply out of curiosity - it has expanded to provide its own
REST and GraphQL APIs, and utilizes Redis as the main and in-memory database for
its speed and persistence.

## Project structure

This codebase is written in TypeScript and Python; it utilizes the ES Module
syntax, with some files utilize the `.cjs` file type for Prettier, Tailwind, and
PostCSS configs.

This project is a [**monorepo**](https://monorepo.tools/#what-is-a-monorepo), it
uses Yarn workspaces and Turborepo to install and manage dependencies in each
subdirectory and remotely cache builds on the cloud via Turborepo.

- `.github` - CI/CD Workflow stuff
- `.husky` - Pre-commit hooks for lint-staging
- `apps`
	- `admin-vite` - A web admin app in Vite and Vue 3
	- `api` - API for both REST and GraphQL
	- `website` - The website written in Nuxt 3 + Tailwind CSS
- `python` - For scraping and parsing public drawing data using Python with
	BeautifulSoup
- `shared`
	- `config` - Other configs like Tailwind and others like styles
	- `types` - Shared TypeScript declarations
	- `tsconfig` - Shared TypeScript config
	- `ui` - Shared `.vue` components
- `scripts` - scripts for cleaning up node stuff

## Setup and Installation

### Prerequisites

- **Required**
  - Node.js 16 or higher (LTS recommended)
  - Python 3.10 or higher
  - Yarn Package Manager
- **Optional**
  - WSL/Git Bash
  - GNU Make

### Installation

If you have the `make` tool installed on your system, run the command to install all libraries
from Node and Python:

```console
make setup
```

For manual installation, first: Node dependencies with Yarn:

```console
yarn install
```

Install Python packages:

```console
pip install -r requirements.txt
```

Then, clone the `.env` files:

```console
cp apps/website/.env.example apps/website/.env
cp apps/admin-vite/.env.example apps/admin-vite/.env
```

### Scripts

> Any changes to the files when running the `build` command will run the builds
> usually, then get remotely cached via Turborepo.

#### Running in bulk

Run both the website and admin dashboard, opening ports 3000 and 5173 w/o
needing to rely on the `concurrently` library:

```console
yarn dev
```

Build both the website and admin dashboard:

```console
yarn build
```

#### Running separately

Run the website only, this will open port 3000 on `localhost`:

```console
yarn dev:web
```

Run the admin dashboard only, this will open port 5173 on `localhost`:

```console
yarn dev:admin
```

Build the website only:

```console
yarn build:web
```

Build the admin dashboard:

```console
yarn build:admin
```

## API

![API banner](https://user-images.githubusercontent.com/94678583/203912229-9b6c2479-e999-4b36-9d54-205037691d18.png)

> **Note** Section WIP

### Planned Endpoints

- `/character/:character?={query}`
- `/characters/?={query}`
- `/artwork/:year/:title?={query}`

## About this project

![](https://user-images.githubusercontent.com/94678583/208869784-c68b5483-8e18-4d01-9163-d502b4cb40c5.png)

The project began on October 31, 2021, and the possible inspiration from this
project is through McBroken (basically a McDonald's broken ice cream machine
site) and it'd be interesting to see in all of his drawings to see said data, and
its various datasets.

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

Believe it or not, it's not my intention to impress him in general.

I'm just a huge fan of his artwork and his unique and adorable art style that
I'd want to see how many characters he's drawn since the early to mid-2000s, but
he'd for sure find it interesting as it's more of a fun project to a new hobby
of mine, learning not only JavaScript but also learning a bit of back-end and
basic data management in the process of other projects I do.

During the early stages of this project - I have limited backend knowledge and I
needed a help with [@thatITfox][it] for setting up a Flask web server, and now
currently working with Redis stuff!

### Isn't this taking it too far?

As someone who admires his art, yes... to some extent. Well, sure - it may feel
like I watch him on every step, but I only use them for analytical and
informational purposes; parsing drawing data on his Twitter profile would be
difficult and will require more work.

It's more of a serious yet passion side-project of mine to show various kinds of
drawing data from his.

### Are the images/drawings stored in the database?

No, most image requests are coming from FurAffinity since they use Cloudflare as
their CDN under the hood to cache media types.

## License

MIT

[it]: https://github.com/thatITfox
