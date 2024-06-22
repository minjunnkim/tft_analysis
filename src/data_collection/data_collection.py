import json
import argparse
from api import RiotAPI

import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('RIOT_API_KEY') 

def fetch_and_save_data(game_name, tag_line, start=0, count=20, save_path='data/raw/'):
    api = RiotAPI(API_KEY)
    puuid = api.get_puuid(game_name, tag_line)
    match_ids = api.get_match_ids(puuid, start=start, count=count)

    for match_id in match_ids:
        match_data = api.get_match_data(match_id)
        with open(f"{save_path}{match_id}.json", 'w') as f:
            json.dump(match_data, f, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch and save TFT match data")
    parser.add_argument('game_name', type=str, help='Riot game name')
    parser.add_argument('tag_line', type=str, help='Riot tag line')
    parser.add_argument('--start', type=int, default=0, help='Starting index for match retrieval')
    parser.add_argument('--count', type=int, default=20, help='Number of matches to retrieve')
    parser.add_argument('--save_path', type=str, default='data/raw/', help='Path to save match data')

    args = parser.parse_args()
    fetch_and_save_data(args.game_name, args.tag_line, args.start, args.count, args.save_path)