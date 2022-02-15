FROM golang:buster as builder

WORKDIR /app
ADD . .
RUN apt-get update
RUN apt-get install php -y
RUN echo 'php -S 0.0.0.0:8080' > /usr/local/bin/hello-world.sh
RUN chmod +x /usr/local/bin/hello-world.sh

EXPOSE 8080
CMD ["/usr/local/bin/hello-world.sh"]
