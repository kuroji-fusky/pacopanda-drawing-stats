#!/bin/bash
# TODO: check if python, node, and yarn is installed (make rust optional)

# Copy env stuff
cp .env.node ./apps/website/.env
cp .env.node ./apps/admin/.env
cp .env.python ./python/.env

yarn install