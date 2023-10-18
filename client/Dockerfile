FROM node:20-alpine3.17

WORKDIR /

RUN npm i -g yarn

COPY . .

RUN yarn install --frozen-lockfile
RUN yarn build 

EXPOSE 3000
CMD ["node", "build"]
