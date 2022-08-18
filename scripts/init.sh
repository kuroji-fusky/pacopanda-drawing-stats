#!/bin/sh

yarn install
yarn concurrently "cd server && pip install -r requirements.txt" "yarn --cwd ./app install"