![Banner for Paco Panda Drawing Stats](https://user-images.githubusercontent.com/94678583/208869784-c68b5483-8e18-4d01-9163-d502b4cb40c5.png)

<div align="center">
  <h1 align="center">Paco Drawing Stats</h1>

  <a href="https://opensource.org/licenses/MIT">
		<img src="https://img.shields.io/github/license/kuroji-fusky/pacopanda-drawing-stats?style=flat-square">
	</a>
  <a href="https://www.codefactor.io/repository/github/kuroji-fusky/pacopanda-drawing-stats">
    <img alt="CodeFactor Grade" src="https://img.shields.io/codefactor/grade/github/kuroji-fusky/pacopanda-drawing-stats?style=flat-square">
  </a>
</div>

A data analysis and case study created by Kuroji Fusky that collects
and parses drawing data from a furry artist and illustrator [Paco Panda][paco].

Using Python to gather said data and a dedicated API using a web scraper,
BeautifulSoup4 and web framework, FastAPI.

The website is written in Nuxt 3 and Tailwind CSS.

> [!IMPORTANT]
> Machine Learning/AI is not utilized in this project! It's nothing but simple math
> to parse collected data.

## Setup and Installation

### Prerequisites

- Node.js 20 or higher (LTS recommended)
- Python 3.11 or higher
- Yarn
- Docker (optional)

### Installation

This project uses a combination of [`husky`](https://github.com/typicode/husky) and [`pre-commit`](https://pre-commit.com),
`pre-commit` needs to be installed first.

```sh
pip install pre-commit
```

Then, install the packages from both directories

```sh
# Install client website
yarn install

# Go to server
cd src/server

# Setup venv
python -m venv venv

# Linux
source venv/Scripts/activate

# Windows
.\venv\Scripts\activate

# Then install the goodies
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

Paco Drawing Stats' source code is open source and is licensed under
[MIT](https://opensource.org/licenses/MIT).

[paco]: https://twitter.com/panda_paco
