#!/bin/bash

echo "Docker 빌드를 시작합니다."

PROJECT_NAME="homekeeper_api"

IMG_NAME="${PROJECT_NAME}_img"
IMG_VER="0.5"

CONT_EXPORT_PORT=8000

CONT_NAME="${PROJECT_NAME}_cont"
DOCKER_NETWORK_NAME="docker_network"

DIR=$(pwd)

# if not exist image will be build
if ["$(docker images -q "${IMG_NAME}:${IMG_VER}" 2> /dev/null)" == ""]; then
  docker build -t "${IMG_NAME}:${IMG_VER}" .
fi

# check docker container exist if exist will be remove
if ["$(docker ps -a | grep $CONT_NAME 2> /dev/null)" != ""]; then
  docker rm -f $CONT_NAME
fi

#run script
#add docker container config
#docker run -itd --name $CONT_NAME -v "${DIR}/log:/data/log" --network $DOCKER_NETWORK_NAME "${IMG_NAME}:${IMG_VER}"
docker run -itd --name $CONT_NAME  -p "${CONT_EXPORT_PORT}:${CONT_EXPORT_PORT}" "${IMG_NAME}:${IMG_VER}"
