import os
import pandas as pd

def clean_data(raw_path="data/raw/spotify_tracks.csv", output_path="data/processed/spotify_clean.csv", threshold=50):
    df = pd.read_csv(raw_path)
    
    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])
    df = df.dropna().reset_index(drop=True)
    
    df['is_popular'] = (df['popularity'] >= threshold).astype(int)
    
    cols_to_drop = ['popularity', 'artists', 'album_name', 'track_name']
    df = df.drop(columns=[c for c in cols_to_drop if c in df.columns])
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Succès ! Fichier propre sauvegardé dans {output_path} ({df.shape[0]} lignes, {df.shape[1]} colonnes)")

if __name__ == "__main__":
    clean_data()