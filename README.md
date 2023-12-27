![Banner for Paco Panda Drawing Stats](https://user-images.githubusercontent.com/94678583/208869784-c68b5483-8e18-4d01-9163-d502b4cb40c5.png)

<div align="center">
  <h1 align="center">Paco Drawing Stats</h1>

  <a href="https://opensource.org/licenses/apache-2-0">
		<img src="https://img.shields.io/github/license/kuroji-fusky/pacopanda-drawing-stats?style=flat-square">
	</a>
  <a href="https://www.codefactor.io/repository/github/kuroji-fusky/pacopanda-drawing-stats">
    <img alt="CodeFactor Grade" src="https://img.shields.io/codefactor/grade/github/kuroji-fusky/pacopanda-drawing-stats?style=flat-square">
  </a>
</div>

> [!IMPORTANT]
> Machine Learning/AI is not utilized in this project! It's nothing but simple math
> to parse collected data.

A data analysis and case study created by Kuroji Fusky that collects
and parses drawing data from a furry artist and illustrator [Paco Panda][paco].

## How it works

The main gist of the project is that it uses a web scraper written in Python to get new
drawing submission from his socials; then cleans up the data and adds it to the
database. And using that to build this website and the underlying APIs on it!

It uses a combination of [BeautifulSoup4](<https://en.wikipedia.org/wiki/Beautiful_Soup_(HTML_parser)>)
and [Selenium WebDriver](https://www.selenium.dev/) to scrap drawing data from Paco's
socials and adds it to a Redis database that pushes the image binary and the JSON data
along with it.

Once we got the scraped data, it uses FastAPI to provide a REST API and does the data science
stuff on the fly.

## Setup and Installation

### Prerequisites

- Node.js 20 or higher (LTS recommended)
- Python 3.11 or higher
- Yarn
- Docker

### Installation

Install the packages from both directories

```sh
# Install client website
yarn install

# Go to server
cd src/python

# Setup venv
python -m venv venv

# Linux
source venv/Scripts/activate

# Windows
.\venv\Scripts\activate

# Then install the goodies
pip install -r requirements.txt
```

**[Optional]** This project uses both [`husky`](https://github.com/typicode/husky) and [`pre-commit`](https://pre-commit.com), `pre-commit` needs to be installed first.

```sh
pip install pre-commit
```

### Docker

TBA

## API

> [!NOTE]
> Currently, the public APIs only accept `GET` requests. Any
> other request method will respond with `405 Method Not Allowed`
> or `403 Forbidden`.
>
> `👑` - only allowed to be pushed with an auth token

### Endpoints

- `GET /stats{?filters}`
- `GET /artworks`
- `GET /artwork{/title}`
- `GET /characters`
- `GET /character{?names}`
- `POST /new/character/` 👑
- `POST /new/artwork/` 👑

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

[Apache License, Version 2.0](https://opensource.org/license/apache-2-0)

[paco]: https://twitter.com/panda_paco
