![Banner for Paco Panda Drawing Stats](https://user-images.githubusercontent.com/94678583/208869784-c68b5483-8e18-4d01-9163-d502b4cb40c5.png)

<div align="center">
  <a href="https://opensource.org/licenses/MIT">
		<img src="https://img.shields.io/github/license/kuroji-fusky/pacopanda-drawing-stats?style=flat-square">
	</a>
  <a href="https://www.codefactor.io/repository/github/kuroji-fusky/pacopanda-drawing-stats">
    <img alt="CodeFactor Grade" src="https://img.shields.io/codefactor/grade/github/kuroji-fusky/pacopanda-drawing-stats?style=flat-square">
  </a>
</div>

# Paco Drawing Stats

A data analysis and case study created by Kuroji Fusky that collect
and parses drawing data from a furry artist and illustrator [Paco Panda][paco].

Using Python to gather said data and a dedicated API using a web scraper,
BeautifulSoup4 and web framework, FastAPI.

> **Important**
> Machine Learning/AI is not used in this project! I used nothing but math
> to parse collected data.

## Project structure

- `client` - Website written in SvelteKit and Tailwind CSS
- `python` - The FastAPI server, image generation, and utilities to
  retrieve drawing data

## Tech stack

![](https://skillicons.dev/icons?i=js,ts,py,tailwind,svelte,fastapi,redis,docker,vercel,cloudflare)

## Setup and Installation

### Prerequisites

- Node.js 20 or higher (LTS recommended)
- Python 3.11 or higher
- Yarn
- Docker (optional)

### `client`

Install Node dependencies with Yarn:

```console
yarn install
```

Run the dev server:

```console
yarn dev
```

### `python`

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

TBA

## About this project

The project began on October 31st 2021. The possible inspiration from this
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

## License

Paco Panda Drawing Stats' source code is open source and is licensed under
[MIT](https://opensource.org/licenses/MIT).

[paco]: https://twitter.com/panda_paco
