# Changelog

## 2023

### August 20

- Removed Fastify app in favor of FastAPI

### August 3

- Massive project purge
- Switching web frameworks from Nuxt 3 to Next.js 13.4.12

### May 25

- Revert from Supabase to Redis
- Purge Python and admin Tauri app for a rewrite

### May 15

- Revert from FastAPI to Fastify (in other words, build the API back to Node.js)
- Change database from Redis to Supabase as a Baas (Backend as a Service)

### April 20

- Remove Fastify API in replacement for FastAPI
- Re-add Tauri app for admin dashboard

### April 19

- Utilize Poetry package manager

### April 18

- Removed admin dashboard; will use Python for efficency
- Renamed package from `paco_utils` to `parinton`

### April 3

- Add Paco Utils Python package

### March 16

- Change codebase license back to MIT

### March 14

- Re-add Python codebase for scraping and parse drawing data
  - I've had second thoughts about this being only an JS-only codebase and just
    realized that Python might be a best use cases for stuff like this
  - Added the "soup" easter egg in `utils.py` because why not

### February 17

- Ditched Tauri app for a simple Vue Vite app
  - With auto import functionality with `unplugin-*`
  - I changed my mind (again) and sticking to a strictly JS codebase only
- Downgrade Node version to ^16

### February 13

- Bump Node version from ^16 to ^18
- Add Turborepo for remote caching
- Add Cheerio library for web scraping with static sites like FurAffinity

### February 10

- Add Tauri admin app for managing characters via UI
  - P.S. I lied about the project being entirely JavaScript, you'll need Rust
    now lol

### February 5

- Change license from MIT to GPL-3.0 to finally GPL-2.0

### January 22

- Axed over ~200 commits and restart project entirely in JavaScript

  - Reason: Handling Node and Python environments can be a hassle and require a
    lot of tooling and resources on each individual environments.

  - The only solution is to use one environment for overall maintainability and
    for sharable code using the monorepo approach.

  - For previous Python codebase, it has been replaced from beautifulsoup with
    Puppeteer library.

  - For the frontend, it was previously written with Vue CLI on December 4,
    2021, with the long-awaited Nuxt 3 Stable release, the website will be
    rewritten back to Vue.

## 2022

### December 17

- Initialized Nextron app for manually managing drawn characters via Redis

### December 15

- Reroute VS Code intellsense from root directory
- Organize UI component types

### November 26

- Restructured project structure as a _true_ monorepo via Yarn workspaces
  - Decoupled both Node and Python with `packages` and `python` directories
    respectively
- Readded FastAPI w/ GraphQL using ~~Majira~~ Strawberry
- Add pre-commit git hooks with Husky

### October 22

- Rewrote both Python and Node codebases, retired FastAPI backend
- Added Dockerfile for testing

### July 27

- Decommission Go backend, Python is good and fast enough - Go might be an
  overkill

### July 26

- Added Cypress for Unit and E2E (end-to-end) testing, making sure the app is
  bug-free!
- Finally regex'd the date in the scraper script!

### July 16

- Working on Gin web server and Colly scraper in the Go programming language for
  even faster performance.
- Moved the new project to this repo and kept all the previous commits from
  April from the
  [initial archived repository](https://github.com/skepfusky/pandapaco-drawing-stats-old)
  maintaining the previous commits and branches.

### June 29

- Added the ability to find all the pages available from the scraper script.

### June 12

- Removed `data` folder, including the Jupyter Notebook file (it's bad trust me)
- Added CC-BY-SA 4.0 license

### June 01

- Changing backend infrastructure from Flask to FastAPI!

### April 17

- Removed all past commits via rebase

### April 09

- Restarted the whole project with Next.js + TypeScript

### April 07

- Moved all old Vue 3 files to the `vue-3-legacy` branch.

### January 01

- Went back from Vue 3 CLI.

## 2021

### December 29

- Added a `paco-drawing-data.ipynb` file in an attempt to explain the dataset
  I've gathered manually, it was pain lol - at this time, I didn't have any
  automation tools to make gathering data less laborious lol

### December 23

- Tried Vue 3 + Vite. I've had issues with setting the images prop from a
  component. There really wasn't a clear way to do this when building for
  production.

### December 04

- Rewrite project generated via Vue 3 CLI!

### October 31

- Initiated project with plain HTML. Imported libraries such as D3.js and
  Chart.js.
