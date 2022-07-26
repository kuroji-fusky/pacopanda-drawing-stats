#!/bin/sh

cd ..

yarn install

concurrently -k nextjs,python \
"yarn --cwd ./app install" \
"cd ./server/python-backend && pip install -r requirements.txt"

echo "Done"
