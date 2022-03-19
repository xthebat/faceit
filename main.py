import time
from datetime import datetime

import faceit


def main():
    nickname = "-mblw-"

    player_details = faceit.get_player_details(nickname)

    player_id = player_details["payload"]["id"]

    while True:
        player_state = faceit.get_player_state(player_id)
        if player_state["payload"]:
            payload = player_state["payload"]
            if "CHECK_IN" in payload:
                match_id = payload["CHECK_IN"][0]["id"]
            elif "VOTING" in payload:
                match_id = payload["VOTING"][0]["id"]
            elif "READY" in payload:
                match_id = payload["READY"][0]["id"]
            elif "ONGOING" in payload:
                match_id = payload["ONGOING"][0]["id"]
            else:
                print(f"{player_state}")
                raise Exception(f"Unknown match state!")

            break

        time.sleep(1)

    while True:
        match_details = faceit.get_match_details(match_id)
        payload = match_details["payload"]
        state = payload["state"]
        match_id = payload["state"]
        print(f"Player {nickname} is {state} in match {match_id}")
        if state == "FINISHED":
            break

    matches_stats = faceit.get_match_stats(match_id)
    for match_stats in matches_stats:
        map_name = match_stats["i1"]
        date = datetime.fromtimestamp(match_stats['date'] // 1000)
        print(f"Player {nickname} finished map {map_name} at {date}")
    else:
        print(f"Match not started")


if __name__ == '__main__':
    main()

