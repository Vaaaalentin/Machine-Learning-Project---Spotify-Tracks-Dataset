import os
import shutil
import kagglehub

def download_spotify_data():
    path = kagglehub.dataset_download("maharshipandya/-spotify-tracks-dataset")

    raw_dir = os.path.join("data", "raw")
    os.makedirs(raw_dir, exist_ok=True)

    source_csv = os.path.join(path, "dataset.csv")
    destination_csv = os.path.join(raw_dir, "spotify_tracks.csv")
    shutil.copy(source_csv, destination_csv)
    
    print(f"Succès ! Le fichier CSV brut est prêt ici : {destination_csv}")

if __name__ == "__main__":
    download_spotify_data()