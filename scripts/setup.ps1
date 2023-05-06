# TODO: check if python, node, and yarn is installed (make rust optional)

# Copy env stuff
Copy-Item '/scripts/.env.node' -Destination "/apps/website/.env"
Copy-Item '/scripts/.env.node' -Destination "/apps/admin/.env"
Copy-Item '/scripts/.env.python' -Destination "/python/.env"

yarn install
