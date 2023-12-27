---
title: About
---

::Leading
stuff
::

## How it works

The main gist of the project is that it uses a web scraper written in Python to get new
drawing submission from his socials; then cleans up the data and adds it to the
database. And using that to build this website and the underlying APIs on it!

For a super nerdy explanation: it uses a combination of [BeautifulSoup4](<https://en.wikipedia.org/wiki/Beautiful_Soup_(HTML_parser)>) and [Selenium WebDriver](https://www.selenium.dev/) to scrap
drawing data from Paco's socials and adds it to a Redis database that pushes the image binary
and the JSON data along with it.

Once we got the scraped data, it uses FastAPI to provide a REST API and does the data science
stuff on the fly.

## Why I started this project

When I was learning the basics of web development in 2021, I've always wanted see how many times
Paco has drawn foxes, wolves, etc. and also if he has drawn any protogens too.

It was a challenging from the start since I haven't learn Python yet and used Google Sheets to
manually handwrite the data, which was slow, error-prone, and an ineffficient approach to
something like this especially when dealing with realtime updates, which I was aiming for.

I've been working on and off for this project for 3 whole years as I progressively learn
now things such as APIs and databases, and to finally get it up and running.
