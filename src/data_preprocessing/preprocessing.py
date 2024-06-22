import os
import json
import pandas as pd
from itertools import chain


def preprocess_data(raw_data_path='data/raw/', processed_data_path='data/processed/'):
    all_data = []

    for filename in os.listdir(raw_data_path):
        if filename.endswith('.json'):
            with open(os.path.join(raw_data_path, filename), 'r') as f:
                match_data = json.load(f)

                for participant in match_data['info']['participants']:                       
                    data = {
                        'match_id': match_data['metadata']['match_id'],
                        'puuid': participant['puuid'],
                        'placement': participant['placement'],
                        'total_damage_to_players': participant['total_damage_to_players'],
                        'time_eliminated': participant['time_eliminated'],
                        'gold_left': participant['gold_left'],
                        'last_round': participant['last_round'],
                        'level': participant['level'],
                        'augments': ', '.join(participant['augments']),
                    }

                    event_check = False

                    # Adding traits with their style level
                    for trait in participant['traits']:
                        if 'TFTEvent5YR' in trait['name']:
                            event_check = True
                            break
                        data[f"{trait['name']}_style"] = trait['style']

                    if event_check:
                        break

                    # Adding units with their tiers, rarity, and value
                    for unit in participant['units']:
                        data[f"{unit['character_id']}_tier"] = unit['tier']
                        data[f"{unit['character_id']}_rarity"] = unit['rarity'] + 1
                        data[f"{unit['character_id']}_value"] = (unit['rarity'] + 1) * (3 ** unit['tier'])

                    all_data.append(data)

                

    df = pd.DataFrame(all_data)
    df.fillna(0, inplace=True)
    df.to_csv(os.path.join(processed_data_path, 'tft_match_data.csv'), index=False)

if __name__ == "__main__":
    preprocess_data()