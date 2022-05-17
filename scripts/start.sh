#!/bin/sh

cd ..

yarn install

yarn --cwd ./app install

cd server

pip install -r requirements.txt