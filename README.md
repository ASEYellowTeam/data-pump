# data-pump
_Get data from Strava_

[![Build Status](https://travis-ci.org/ASEYellowTeam/data-pump.svg?branch=master)](https://travis-ci.org/ASEYellowTeam/data-pump)
[![Coverage Status](https://coveralls.io/repos/github/ASEYellowTeam/data-pump/badge.svg?branch=master)](https://coveralls.io/github/ASEYellowTeam/data-pump?branch=master)

## First setup

#### 1. Create a Strava API application
- https://strava.github.io/api/#access
- https://www.strava.com/settings/api

Export the variables you have obtained by registering your application.

Export also the address and the port of the [data-service](https://github.com/ASEYellowTeam/data-service) microservice,
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
python setup.py develop
```

#### 4. Install [Redis](https://redis.io/download#installation)
In a folder of your choice (outside this repository):
```
wget http://download.redis.io/releases/redis-5.0.0.tar.gz
tar xzf redis-5.0.0.tar.gz
cd redis-5.0.0
make install
```

<br>

## Run the microservice

##### Terminal #1
Start redis: `redis-server`

##### Terminal #2
1. Load environment variables:  
   `source variables.sh`

3. Start a celery worker:  
   `celery worker -A datapump.datapump -B`
