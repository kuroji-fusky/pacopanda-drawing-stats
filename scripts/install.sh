#!/bin/bash

function pythonInstall() {
  echo "Installing dependencies..."
  pip install -r requirements.txt
  echo "Installing dependencies... Done."
}

function nodeInstall() {
  echo "Install with npm or yarn?"
  read -p "[npm/yarn]: " npm_or_yarn
  if [ "$npm_or_yarn" == "npm" ]; then
    echo "Installing dependencies..."
    npm install
    echo "Installing dependencies... Done!"

  elif [ "$npm_or_yarn" == "yarn" ]; then
  # It's not possible to install dependencies with yarn, so install the yarn package globally
  if [ `npm list -g | grep -c yarn` -eq 0 ]; then
    echo "It looks like the yarn package is not installed globally, installing..."
    npm install -g yarn
    yarn install
    echo "Installing dependencies... Done!"

    else
      echo "Installing dependencies..."
      yarn install
      echo "Installing dependencies... Done!"
    fi

  else
    echo "Invalid input lmao"
  fi
}

# Check if python3 or pip is installed
if [ ! command -v python3 || ! command -v pip ]; then
  echo "Python and pip are required to install the project."
  # install with linux
  if [ -f /etc/debian_version ]; then
    sudo apt-get install python3 python3-pip
  pythonInstall()

else
  pythonInstall()
fi

# Check if Node.js is installed
if [ ! command -v node ]; then
  echo "Node.js aint found fam. Installing NVM..."

  # install Node Version Manager
  curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash
  export NVM_DIR="$HOME/.nvm" && [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" && [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"

  nvm install --lts
  nodeInstall()

else
  nodeInstall()
fi