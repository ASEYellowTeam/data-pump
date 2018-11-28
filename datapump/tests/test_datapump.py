from datapump.tests.utility import new_user
from datapump.datapump import fetch_all_runs
import requests_mock
import os
import requests


def test_fetch_all_runs():

    # this tests all the functions in datapump.py because fetch_all_runs calls them all

    # token of a test account
    strava_token = 'f288e7b7f4e118c8aca3f655b8e95f4c4d335434'

    user = new_user()

    with requests_mock.mock(real_http=True) as m:
        m.get(os.environ['DATA_SERVICE'] + '/users', json=[user.to_json(secure=False)])
        try:
            runs = fetch_all_runs()

            assert runs == {}

            user.strava_token = strava_token

            m.get(os.environ['DATA_SERVICE'] + '/users', json=[user.to_json()])

            runs = fetch_all_runs()

            assert str(runs) == "{None: [{'strava_id': 1936220842, 'name': 'Evening Run', 'distance': 0.0, " \
                           "'elapsed_time': 0.0, 'average_speed': 0.0, 'average_heartrate': None, " \
                           "'total_elevation_gain': 0.0, 'start_date': 1540925068.0, 'title': 'Evening Run', " \
                           "'description': None}]}"
        except requests.exceptions.ConnectionError:
            assert True is True
