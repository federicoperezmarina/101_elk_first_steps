# Kibana
Here we have some examples to learn how to use kibana

## Table of Contents
* [Kibana with docker](#kibana-with-docker)
* [How to connect](#how-to-connect)

## Kibana with docker
In order to use Kibana with docker we are going to use docker compose to start a elasticsearch container and a kibana container.

docker-compose.yml file:
```sh
services:
  elasticsearch:
    image: elasticsearch:8.3.3
    container_name: my_elasticsearch_8
    environment:
      discovery.type: single-node
      ES_JAVA_OPTS: "-Xms512m -Xmx512m"
    ports:
      - "9200:9200"
      - "9300:9300"
    healthcheck:
      test: ["CMD-SHELL", "curl --silent --fail localhost:9200/_cluster/health || exit 1"]
      interval: 10s
      timeout: 10s
      retries: 3
    networks:
      - elastic
  kibana:
    image: kibana:8.3.3
    container_name: my_kibana_8
    ports:
      - "5601:5601"
    depends_on:
      - elasticsearch
    networks:
      - elastic
networks:
  elastic:
    driver: bridge
```

To launch the docker compose we can use this command:
```sh
docker compose up
```

Output:
```sh
[+] Running 2/1
 ⠿ Container my_elasticsearch_8  Created                                                                                                                           0.1s
 ⠿ Container my_kibana_8         Created                                                                                                                           0.1s
Attaching to my_elasticsearch_8, my_kibana_8
my_elasticsearch_8  | {"@timestamp":"2022-08-18T21:46:23.967Z", "log.level": "INFO", "message":"version[8.3.3], pid[72], build[docker/801fed82df74dbe537f89b71b098ccaff88d2c56/2022-07-23T19:30:09.227964828Z], OS[Linux/5.10.47-linuxkit/amd64], JVM[Oracle Corporation/OpenJDK 64-Bit Server VM/18.0.2/18.0.2+9-61]", "ecs.version": "1.2.0","service.name":"ES_ECS","event.dataset":"elasticsearch.server","process.thread.name":"main","log.logger":"org.elasticsearch.node.Node","elasticsearch.node.name":"d77d916e58de","elasticsearch.cluster.name":"docker-cluster"}
my_elasticsearch_8  | {"@timestamp":"2022-08-18T21:46:23.979Z", "log.level": "INFO", "message":"JVM home [/usr/share/elasticsearch/jdk], using bundled JDK [true]", "ecs.version": "1.2.0","service.name":"ES_ECS","event.dataset":"elasticsearch.server","process.thread.name":"main","log.logger":"org.elasticsearch.node.Node","elasticsearch.node.name":"d77d916e58de","elasticsearch.cluster.name":"docker-cluster"}
...
```

Now we are able to go to "http://localhost:5601/" in order to use kibana. In this section we are going to continue with the configuration. We are going to see a page to insert our enrollment token:

![Kibana enrollment token](img/kibana_enrollment_token.png)

How to get the enrollment token? We have to go to my_elasticsearch_8 container and ask for it
```sh
docker exec -it my_elasticsearch_8 /bin/bash
```

And after execute this command inside my_elasticsearch_8 container
```sh
in/elasticsearch-create-enrollment-token --scope kibana
```

Output:
```sh
WARNING: Owner of file [/usr/share/elasticsearch/config/users] used to be [root], but now is [elasticsearch]
WARNING: Owner of file [/usr/share/elasticsearch/config/users_roles] used to be [root], but now is [elasticsearch]
eyJ2ZXIiOiI4LjMuMyIsImFkciI6WyIxNzIuMjEuMC4yOjkyMDAiXSwiZmdyIjoiZjZhNWRmZjQ2ZjZkZjAyZjZkNjdhOGY4YTc4ZDc5ZjY0ZTgwYzQzZGM3Yjc0MTAzMjUwZTNlN2ZlMjdhNThkMiIsImtleSI6IkNBSDRzb0lCbDktUU9mUHFDbkRJOmJTdndPRlZNVE5XUHVtOXhZcEtjZ1EifQ==
```

![Kibana verification required](img/kibana_verification_required.png)

After introducing the token in the input, we will see a modal with the title verification required. In this step we have to enter in my_kibana_8 container and execute:
```sh
docker exec -it my_kibana_8 /bin/bash
bin/kibana-verification-code
```

Output:
```sh
Your verification code is:  XXX XXX
```

![Kibana configure elastic](img/kibana_configure_elastic.png)
![Kibana login](img/kibana_login.png)
