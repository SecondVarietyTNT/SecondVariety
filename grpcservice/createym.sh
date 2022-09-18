#!/bin/sh

yc compute instance create-with-container \
  --name grpcserv1 \
  --zone ru-central1-b \
  --ssh-key ~/.ssh/yandex.pub \
  --network-interface subnet-name=default-ru-central1-b,nat-ip-version=ipv4 \
  --service-account-name grpcweb \
  --docker-compose-file ./docker-compose.yaml