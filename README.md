# data-pump
_Get data from Strava_

[![Build Status](https://travis-ci.org/ytbeepbeep/data-pump.svg?branch=master)](https://travis-ci.org/ytbeepbeep/data-pump)
[![Coverage Status](https://coveralls.io/repos/github/ytbeepbeep/data-pump/badge.svg?branch=master)](https://coveralls.io/github/ytbeepbeep/data-pump?branch=master)

## First setup

#### 1. Create a Strava API application
- https://strava.github.io/api/#access
- https://www.strava.com/settings/api

Export the variables you have obtained by registering your application.

Export also the address and the port of the [data-service](https://github.com/ytbeepbeep/data-service) microservice,
the default is `127.0.0.1:5002`.

A smart way to do this is to create a file `variables.sh` in the project root, as follows.

```
#!/bin/bash
export STRAVA_CLIENT_ID=<ID>
export STRAVA_CLIENT_SECRET=<SECRET>
export DATA_SERVICE="127.0.0.1:5002"
```

You can load the variables with `source variables.sh`.

#### 2. Install
```
pip install -r requirements.txt
```

#### 3. Install [Redis](https://redis.io/download#installation)
In a folder of your choice (outside this repository):
```
wget http://download.redis.io/releases/redis-5.0.0.tar.gz
tar xzf redis-5.0.0.tar.gz
cd redis-5.0.0
make install
```


## Run the microservice

##### Terminal #1
Start the [data-service](https://github.com/ytbeepbeep/data-service) microservice.

##### Terminal #2
Start redis: `redis-server`

##### Terminal #3
1. Load environment variables:  
   `source variables.sh`

3. Start a celery worker:  
   `celery worker -A datapump.datapump -B`


## Docker
[![Image size](https://images.microbadger.com/badges/image/ytbeepbeep/data-pump.svg)](https://microbadger.com/images/ytbeepbeep/data-pump)
[![Latest version](https://images.microbadger.com/badges/version/ytbeepbeep/data-pump.svg)](https://microbadger.com/images/ytbeepbeep/data-pump)

A Docker Image is available on the public Docker Hub registry. You can run it with the command below.
- Run the [data-service](https://github.com/ytbeepbeep/data-service#docker) container
- Run redis with `docker run -d --name redis redis`
- Run data-pump with `docker run -d --name data-pump
-e STRAVA_CLIENT_ID=<ID> -e STRAVA_CLIENT_SECRET=<SECRET> -e DATA_SERVICE="data-service:5002" -e BROKER="redis://redis:6379"
--link redis:redis --link data-service:data-service ytbeepbeep/data-pump`

**Important note:** if the `data-service` container is running on another Docker installation,
replace `data-service` with the host, as follows: `-e DATA_SERVICE="<myhost-name-or-address>:5002"`

#### Locally
You can also build your own image from this repository.
- Build with `docker build -t ytbeepbeep/data-pump .`
- Run as usually, with the commands specified above
