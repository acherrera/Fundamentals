# LEARNING DOCKER!

I have very little idea how to use docker. So I am going to check that. Here
are my notes for you to use if you would like. Note that everything with !!
before it is a variable that be changed out and the name is only a placeholder


Tutorial: https://docs.docker.com/get-started/



# Part 1: Basic Primer
## Installation

Okay, this is rather complicated, look it up. Might be able to use snap but I
followed their instructions to get it working


3# Running

    docker run !!hello-world : runs hello world
    docker container --help : shows help
    docker container ls : shows containers
    docker container ls --all 
    docker container ls -aq


# Part 2 - Containers: Building, Running and Uploading
    
Need to have a few things set up to begin
* Dockerfile
* requirements.txt
* app.py


## Building
Now can build with with your own name using

    docker build -t !!dockername


## Running
This command will remap a port while running

    docker run -p 4000:80 !!dockername

This will detach the image to the background

    docker run -d -p 4000:80 !!dockername


### Stopping the docker image
Now that the image is running in the background you need to find it:

    docker container ls

And stop it using the id

    docker container stop !!12asd345sfdg67

# Adding the image to docker hub
First you need to log into the docker container service
    
    docker login

Tag image. This essentially gives the image a version and highly reccomended.
Where username, reposititory and tag is the respective information

    docker tag image !!username/!!repository:!!tag
    docker tag image anthonyh24/cool_repo:v1.1

See the image with the tag

    docker image ls

Add the image to your repo

    docker push !!username/!!repository:!!tag
    docker tag image anthonyh24/cool_repo:v1.1
    


# Part3 - Services
We are going to scale our app the to the MOON!!! Well, we'll set it up so we
can scale it using service. Services are just containers that are controlled.
They can control themselve and make more or less depending on what they need.


## Creating a handler
Need to create a docker-compose.yml file to specify how the service should
handle the container. For an example, here is the .yml used here

version: "3"
services:
  web:
    # replace username/repo:tag with your name and image details
    image: !!username/!!repo:!!tag
    deploy:
      replicas: 5
      resources:
        limits:
          cpus: "0.1"
          memory: 50M
      restart_policy:
        condition: on-failure
    ports:
      - "4000:80"
    networks:
      - webnet
networks:
  webnet:

What this does:
* Pull the image we uploaded
* Run 5 instances of the image and called 'web'. Limit each to 10% of the total
  CPU
* Restart if a container fails
* Map port 4000 of host to 80
* Share port 80 via load-balanced network called 'webnet'.


## Initializing and Running
Need to start the handler with

    docker swam init

Now we can actually run the app
