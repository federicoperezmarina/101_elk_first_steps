# Kibana
Here we have some examples to learn how to use kibana

## Table of Contents
* [Kibana with docker](#kibana-with-docker)
* [How to connect](#how-to-connect)

## Kibanawith docker
This is the Dockerfile that we want to use to build the image of kibana.
```sh
FROM kibana:7.17.5

```

In the second step we show how to build the image having the dockerfile
```sh
docker build -t kibana_7 .
```

In the third step we are going to run the the docker build image
```sh
docker run -d --name my_kibana_7 -p 5601:5601 kibana_7
```

Output:
```sh

```

Now we are able to enter into the running image in order to execute some examples
```sh

```