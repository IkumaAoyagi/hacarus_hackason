FROM ubuntu:20.04

RUN apt-get update \
    && apt-get install --no-install-recommends -y python3 python3-pip \
    && pip3 install --upgrade pip \
    && pip3 install slackbot slackclient slacker \
    && apt-get clean
