FROM node:lts

WORKDIR /app

# Enables hot reloading
# Also had to disable gRPC FUSE in Docker
ENV CHOKIDAR_USEPOLLING=true

COPY package.json package-lock.json .
RUN npm install

COPY . .

CMD ["npm", "start"]
