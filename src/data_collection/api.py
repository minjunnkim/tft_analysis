import requests

class RiotAPI:
    def __init__(self, api_key, region='americas'):
        self.api_key = api_key
        self.region = region
        self.base_url = f"https://{region}.api.riotgames.com"

    def get_puuid(self, game_name, tag_line):
        url = f"{self.base_url}/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
        headers = {"X-Riot-Token": self.api_key}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json().get('puuid')
        else:
            response.raise_for_status()

    def get_match_ids(self, puuid, start=0, count=20):
        url = f"{self.base_url}/tft/match/v1/matches/by-puuid/{puuid}/ids?start={start}&count={count}"
        headers = {"X-Riot-Token": self.api_key}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def get_match_data(self, match_id):
        url = f"{self.base_url}/tft/match/v1/matches/{match_id}"
        headers = {"X-Riot-Token": self.api_key}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()