# Docker Installation Guide

This guide provides step-by-step instructions on how to use
Docker to install files on your host machine.

## Prerequisites

Before proceeding, ensure that you have Docker and Docker Compose installed on your host machine. 
If you haven't installed them yet, you can follow the instructions provided in the links below:

- [Install Docker](https://docs.docker.com/get-docker/)
- [Install Docker Compose](https://docs.docker.com/compose/install/)

Make sure that the Docker daemon is running on your machine.

## Setup

1. Clone the package to a directory on your host machine.

2. Inside the package, you will find a `docker-compose.yml` file. This file 
    contains mount bind directories as volumes for the services. 
    For the `web` volume, provide the absolute path of the `api_app`
    directory as follows: `absolute_path/api_app`.
    Do not remove `:/code/ro` after the absolute path.

3. All the required installations are listed in the `requirements.txt` file.
   These installations will be automatically installed when the Docker containers are set up.

4. Set up the MongoDB username and password as environment variables in the `docker-compose.yml` file.

## Starting Docker Containers

To start the Docker containers, execute the following command:

```bash
docker compose up -d
```
To stop the Docker containers, execute the following command:
```bash
docker compose down
```

Please note that the commands `docker-compose up -d` and `docker-compose down`
should be executed in the terminal or command prompt. 
Make sure you have navigated to the directory where your `docker-compose.yml` 
file is located before running these commands.

[__Home Page__](README.md)  |   [__Previous Page__](page2.md) | [__Next Page__](page4.md)

