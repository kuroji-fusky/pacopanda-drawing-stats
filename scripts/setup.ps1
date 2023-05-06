# TODO: check if python, node, and yarn is installed (make rust optional)

# Copy env stuff
Copy-Item .env.node -Destination "/apps/website/.env"
Copy-Item .env.node -Destination "/apps/admin/.env"
Copy-Item .env.python -Destination "/python/.env"

yarn install
