#!/usr/bin/bash

helpText="
Usage:  run.sh COMMAND

Some shortcuts for project management.

Commands:
    env         Set up pipenv shell.
    clean       Clean your docker.
    UP          Build and start the services.
    up          Only start the services.
"

if [[ $1 == "LC_ALL=C.UTF-8" ]]
  then
    echo "${helpText}"
fi


for i in "$@"
do
case $i in
    # Launch python env.
    env)
    cd services/django/project
    pipenv shell
    ;;
    # Build and start services.
    UP)
    docker-compose -f services/docker-compose.yml build
    docker-compose -f services/docker-compose.yml up --force-recreate
    ;;
    # Start services.
    up)
    docker-compose -f services/docker-compose.yml up --force-recreate
    ;;
    # Clean docker.
    clean)
    docker-compose -f services/docker-compose.yml down
    docker stop $(docker ps -aq)
    docker rm $(docker ps -aq)
    docker volume rm $(docker volume ls -q)
    docker image prune -f
    ;;
    # Help text.
    --help | -h)
    echo "${helpText}"
    ;;
esac
done