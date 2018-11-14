# data-pump

Microservice for getting data from Strava

## Setup the environment

First, create the virtual environment and install the requirements:

```bash

python3.6 -m venv venv
source venv/bin/activate
pip3.6 install -r requirements.txt

```

Then, be sure that the environment variables STRAVA_CLIENT_ID and STRAVA_CLIENT_SECRET are set.

## Running the pump

To run the pump, open a terminal and run:

```bash

celery worker -A datapump.datapump

```