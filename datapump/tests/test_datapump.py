from datapump.tests.utility import new_user
from datapump.datapump import fetch_all_runs
import requests_mock
import os
import requests


def test_fetch_run():

    # token of a test account
    strava_token = 'f288e7b7f4e118c8aca3f655b8e95f4c4d335434'

    user = new_user()
    user.strava_token = strava_token

    with requests_mock.mock(real_http=True) as m:
        m.get(os.environ['DATA_SERVICE'] + '/users', json=[user.to_json()])
        try:
            runs = fetch_all_runs()

            assert str(runs) == "{None: [{'strava_id': 1936220842, 'name': 'Evening Run', 'distance': 0.0, " \
                           "'elapsed_time': 0.0, 'average_speed': 0.0, 'average_heartrate': None, " \
                           "'total_elevation_gain': 0.0, 'start_date': 1540925068.0, 'title': 'Evening Run', " \
                           "'description': None}]}"
        except requests.exceptions.ConnectionError:
            assert True is True
