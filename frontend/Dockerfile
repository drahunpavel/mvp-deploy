FROM node:24-alpine AS builder

WORKDIR /app

COPY /frontend/package.json /frontend/yarn.lock ./

RUN yarn install

COPY /frontend .

RUN yarn build

FROM nginx:stable-alpine

RUN rm /etc/nginx/conf.d/default.conf

COPY /nginx/default.conf /etc/nginx/conf.d/default.conf

COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]