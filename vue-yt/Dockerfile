FROM node:16-buster

WORKDIR /app/vue-yt

COPY package*.json ./

# RUN npm install -g vite

RUN npm install

# RUN npm run lint

# If you are building your code for production
# RUN npm ci --only=production

CMD [ "npm", "run", "dev" ]