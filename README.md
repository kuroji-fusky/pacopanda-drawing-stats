> **Important**
> I'm putting this project on hold as I usually go on and off working on this data viz project all by
> myself. And plus, despite starting this project 2 years ago, there hasn't been any significant
> changes in terms of working on the website - so I'm leaving it be for now, maybe I'll work on this
> in the forseeable future.

![Banner for Paco Panda Drawing Stats](https://github.com/kuroji-fusky/pacopanda-drawing-stats/assets/94678583/e36ea6e1-78fa-4ff7-9488-d151bd9caf11)

<h1 align="center">Paco Panda Drawing Stats</h1>

<p align="center">
	<a href="https://opensource.org/licenses/MIT">
		<img src="https://img.shields.io/github/license/kuroji-fusky/pacopanda-drawing-stats?style=flat-square" />
	</a>
</p>
	
**Paco Panda Drawing Stats** is a data analysis and data visualization project
that collects and parses drawing data from a furry artist and illustrator Paco
Panda.

Initially made simply out of curiosity - it has expanded to provide its own REST
and GraphQL APIs, and utilizes Supabase as the database.

## Project structure

This project is structured as a
[**monorepo**](https://monorepo.tools/#what-is-a-monorepo), it uses Yarn
workspaces and Turborepo to install and manage dependencies in each subdirectory
and remotely cache builds on the cloud via Turborepo.

Written in TypeScript and Python - it utilizes the ES Module syntax, with some
files utilize the `.cjs` file type for Prettier, ESLint configs.

- `server` - Server hosted using FastAPI; local scraper and parser library for
  manipulating public drawing data with Python
- `client` - Website written in Next.js and Tailwind CSS

## Setup and Installation

### Prerequisites

- Node.js 19 or higher (LTS recommended)
- Python 3.11 or higher
- Yarn

### Installation

Install Node dependencies with Yarn:

```console
yarn install
```

For Python, go to the `server` directory:

```console
cd server
```

Create a virtual environment and install the required libraries:

```console
py -m venv venv
.\venv\Scripts\activate

pip install -r requirements.txt
```

## API

![API banner](https://user-images.githubusercontent.com/94678583/203912229-9b6c2479-e999-4b36-9d54-205037691d18.png)

> **Note**
> Section WIP

## About this project

![](https://user-images.githubusercontent.com/94678583/208869784-c68b5483-8e18-4d01-9163-d502b4cb40c5.png)

The project began on October 31, 2021, and the possible inspiration from this
project is through McBroken (basically a McDonald's broken ice cream machine
site) and it'd be interesting to see in all of his drawings to see said data,
and its various datasets.

This project collects the following:

- The title and date of the piece
- Number of character(s) species and names
- Media type (either drawn digital or traditional)
- Programs/mediums used (i.e. Photoshop, Procreate, etc.)
- The source where I got the data (i.e. FurAffinity, DeviantArt, InkBunny,
  Weasyl, etc.)

Previously, I have to manually source it through FurAffinity and DeviantArt for
his draft drawings (including his _Art & Biro_ comics). Unfortunately, drawings
from Twitter won't be counted in order to ease the load on my end and the
dataset as well since all the data gathered will be hard coded to the site.

### Why did you create this project?

Believe it or not, it's not my intention to impress him in general.

I'm just a huge fan of his artwork and his unique and adorable art style that
I'd want to see how many characters he's drawn since the early to mid-2000s, but
he'd for sure find it interesting as it's more of a fun project than a new hobby
of mine, learning not only JavaScript but also learning a bit of back-end and
basic data management in the process of other projects I do.

During the early stages of this project - I have limited backend knowledge and I
needed help with [@thatITfox][it] for setting up a Flask web server, and now
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

Paco Panda Drawing Stats' source code is open source and is licensed under
[MIT](https://opensource.org/licenses/MIT).

[it]: https://github.com/thatITfox

```

```
