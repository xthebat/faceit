import json

import requests

from urls import FACEIT_MATCH_URL, FACEIT_STATS_URL, FACEIT_USER_URL


def do_faceit_request(base_url: str, version: str, endpoint: str, ):
    api_url = f"{base_url}/{version}/{endpoint}"
    headers = {'accept': 'application/json'}
    res = requests.get(api_url, headers=headers)
    return json.loads(res.content.decode('utf-8')) if res.status_code == 200 else None


def get_player_state(player_id: str):
    return do_faceit_request(FACEIT_MATCH_URL, "v1", f"matches/groupByState?userId={player_id}")


def get_match_details(match_id: str):
    return do_faceit_request(FACEIT_MATCH_URL, "v2", f"match/{match_id}")


def get_player_details(nicknames: str):
    return do_faceit_request(FACEIT_USER_URL, "v1", f"nicknames/{nicknames}")


def get_match_stats(match_id: str):
    return do_faceit_request(FACEIT_STATS_URL, "v1", f"stats/matches/{match_id}")