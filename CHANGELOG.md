# Changelog

## 2022

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

- Decommission Go backend, Python is good and fast enough - Go might be
  an overkill

### July 26

- Added Cypress for Unit and E2E (end-to-end) testing, making sure the app
  is bug-free!
- Finally regex'd the date in the scraper script!

### July 16

- Working on Gin web server and Colly scraper in the Go programming language
  for even faster performance.
- Moved the new project to this repo and kept all the previous commits from
  April from the [initial archived repository](https://github.com/skepfusky/pandapaco-drawing-stats-old)
  maintaining the previous commits and branches.

### June 29

- Added the ability to find all the pages available from the scraper script.

### June 12

- Removed `data` folder, including the Jupyter Notebook file (it's bad trust
  me)
- Added CC-BY-SA 4.0 license

### June 01

- Changing backend infrastructure from Flask to FastAPI!

### April 17

- Removed all past commits via rebase

### April 09

- Restarted the whole project with Next.js + TypeScript

### April 07

- Moved all old Vue 3 files to the `vue-3-legacy` branch.

### Jan 01

- Went back from Vue 3 CLI.

## 2021

### Dec 29

- Added a `paco-drawing-data.ipynb` file in an attempt to explain the dataset
  I've gathered manually, it was pain lol - at this time, I didn't have any
  automation tools to make gathering data less laborious lol

### Dec 23

- Tried Vue 3 + Vite. I've had issues with setting the images prop from
  a component. There really wasn't a clear way to do this when building
  for production.

### Dec 04

- Rewrite project generated via Vue 3 CLI!

### Oct 31

- Initiated project with plain HTML. Imported libraries such as D3.js and Chart.js.
