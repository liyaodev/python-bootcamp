#!/bin/bash

if [ "${1-}" = "up" ]; then
    mkdir -p "${PYTHON_BOOTCAMP_ROOT_DIR:-.}/volumes/vscode-extensions"
    chmod -R 777 "${PYTHON_BOOTCAMP_ROOT_DIR:-.}/volumes"

    docker-compose -f ${PYTHON_BOOTCAMP_ROOT_DIR:-.}/docker-compose-devcontainer.yml up -d
fi

if [ "${1-}" = "down" ]; then
    docker-compose -f ${PYTHON_BOOTCAMP_ROOT_DIR:-.}/docker-compose-devcontainer.yml down
    rm -rf "${PYTHON_BOOTCAMP_ROOT_DIR:-.}/volumes"
fi
