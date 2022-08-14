FROM elasticsearch:7.17.5

COPY . .

USER root:root

RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip && \    
    pip3 install elasticsearch

USER elasticsearch:root