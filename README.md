![Banner for Paco Panda Drawing Stats](https://user-images.githubusercontent.com/94678583/208869784-c68b5483-8e18-4d01-9163-d502b4cb40c5.png)

<div align="center">
  <a href="https://opensource.org/licenses/MIT">
		<img src="https://img.shields.io/github/license/kuroji-fusky/pacopanda-drawing-stats?style=flat-square">
	</a>
  <a href="https://www.codefactor.io/repository/github/kuroji-fusky/pacopanda-drawing-stats">
    <img alt="CodeFactor Grade" src="https://img.shields.io/codefactor/grade/github/kuroji-fusky/pacopanda-drawing-stats?style=flat-square">
  </a>
</div>
	
**Paco Panda Drawing Stats** is a data analysis and visualization project
that collects and parses drawing data from a furry artist and illustrator
[Paco Panda][paco].

## Project structure

- `client` - Website written in SvelteKit and Tailwind CSS
- `python` - The FastAPI server, image generation, and utilities to
  retrieve drawing data

## Tech stack

- SvelteKit
- Tailwind CSS
- FastAPI
- Turborepo
- Docker
- Vercel

## Setup and Installation

### Prerequisites

- Node.js 20 or higher (LTS recommended)
- Python 3.11 or higher
- Yarn
- Docker (optional)

### Frontend

Install Node dependencies with Yarn:

```console
yarn install
```

Run the dev server:

```console
yarn dev
```

### Backend/Data Analysis

Go to the `python` directory:

```console
cd python
```

Create a virtual environment and install the required libraries:

```console
python -m venv venv

.\venv\Scripts\activate

pip install -r requirements.txt
```

### Docker

TBD

## API

![API banner](https://user-images.githubusercontent.com/94678583/203912229-9b6c2479-e999-4b36-9d54-205037691d18.png)

> **Note**
> Section WIP

## About this project

The project began on October 31, 2021, and the possible inspiration from this
project is through McBroken (basically a McDonald's broken ice cream machine
site) and it'd be interesting to see in all of his drawings to see said data,
and its various datasets.

This project collects the following:

- The title and date of the piece
- Number of character(s) appearances, including species and names
- Media type (either drawn digital or traditional)
- Programs/mediums used (i.e. Photoshop, Procreate, etc.)
- The source where I got the data (i.e. FurAffinity, DeviantArt, InkBunny,
  Weasyl, etc.)

Previously, I had to manually source it through FurAffinity and DeviantArt for
his draft drawings (including his _Art & Biro_ comics). Unfortunately, drawings
from Twitter won't be counted to ease the load on my end and the
dataset since all the data gathered will be hard coded to the site.

### Why did you create this project?

Believe it or not, it's not my intention to impress him in general.

I'm just a huge fan of his artwork and his unique and adorable art style that
I'd want to see how many characters he's drawn since the early to mid-2000s.

### Isn't this taking it too far?

As someone who admires his art, yes... to some extent. Well, sure - it may feel
like I watch him on every step, but I only use them for analytical and
informational purposes; parsing drawing data on his Twitter profile would be
difficult and will require more work.

It's more of a serious yet passionate side-project of mine to show various kinds of
drawing data from his.

## License

Paco Panda Drawing Stats' source code is open source and is licensed under
[MIT](https://opensource.org/licenses/MIT).

[paco]: https://twitter.com/PacoPanda
