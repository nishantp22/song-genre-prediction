import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from dotenv import load_dotenv
import time
import os

load_dotenv()

client_id = os.getenv('CLIENT_ID')          #client id and client secret from spotify account
client_secret = os.getenv('CLIENT_secret')

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

search_query = 'genre:hip-hop year:2021'    #change it to get tracks from different genres and different years
results_per_request = 50
total_results_needed = 1000     

offset = 0
songs = []
audio_features = []

while len(songs) < total_results_needed:
    results = sp.search(q=search_query, type='track', limit=results_per_request, offset=offset)
    tracks = results['tracks']['items']
    songs.extend(tracks)
    
    track_ids = [track['id'] for track in tracks]
    
    for i in range(0, len(track_ids), 100):
        print(i)
        track_ids_batch = track_ids[i:i+100]
        features_batch = sp.audio_features(track_ids_batch)
        time.sleep(1)
        for features in features_batch:
            features['genre'] = 'hip-hop'  # appending genre information with tracks
            audio_features.append(features)
    
    offset += results_per_request
    
    if not tracks:
        break

new_df = pd.DataFrame(audio_features)           #merging the new dataframe with the old dataset

existing_df = pd.read_csv('datasets/dataset.csv')

merged_df = pd.concat([existing_df, new_df], ignore_index=True)

merged_df.drop_duplicates(inplace=True)

merged_df.to_csv('dataset/dataset.csv', index=False)

print("Merged dataset saved successfully.")
