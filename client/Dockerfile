FROM node

RUN mkdir /client
WORKDIR /client

COPY ./client/package.json .
RUN npm install

COPY ./client/src ./src
COPY ./client/public ./public

EXPOSE 3000
CMD ["npm", "build"]
CMD ["npm", "start"]
