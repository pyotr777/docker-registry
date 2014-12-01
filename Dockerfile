# VERSION 0.1
# DOCKER-VERSION  0.7.3
# AUTHOR:         Sam Alba <sam@docker.com>
# DESCRIPTION:    Image with docker-registry project and dependecies
# TO_BUILD:       docker build -rm -t registry .
# TO_RUN:         docker run -p 5000:5000 registry

# Latest Ubuntu LTS
FROM peter/dev:latest

# Update
RUN apt-get update \
# Install pip
    && apt-get install -y \
        python-pip \
# Install deps for backports.lmza (python2 requires it)
        python-dev \
        liblzma-dev \
        libevent1-dev \
    && rm -rf /var/lib/apt/lists/*

COPY . /docker-registry
COPY ./config/boto.cfg /etc/boto.cfg

# Install core
RUN pip install /docker-registry/depends/docker-registry-core

# Install registry
RUN pip install file:///docker-registry#egg=docker-registry[bugsnag,newrelic,cors]
RUN pip install nose
RUN pip install mock

RUN patch \
 $(python -c 'import boto; import os; print os.path.dirname(boto.__file__)')/connection.py \
 < /docker-registry/contrib/boto_header_patch.diff

RUN pip install  /docker-registry/git-driver

ENV DOCKER_REGISTRY_CONFIG /docker-registry/config/config.yml
ENV SETTINGS_FLAVOR dev

EXPOSE 5000

CMD ["docker-registry"]
