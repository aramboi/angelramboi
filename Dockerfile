FROM alpine:latest

RUN apk add --no-cache nginx
ADD nginx.conf /

WORKDIR /app
ADD ./output ./

EXPOSE 5000
CMD nginx -c /nginx.conf
