FROM node:14.15.5-alpine3.12 as develop-stage
WORKDIR /app
RUN yarn global add @quasar/cli

FROM develop-stage
COPY . .
RUN yarn
RUN quasar build -m ssr
