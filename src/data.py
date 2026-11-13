# Ses yükleme ve spektrogram dönüşümleri
import librosa
import numpy as np
import pandas as pd

def load_data(csv_path='train.csv'):
    return pd.read_csv(csv_path)

def preprocess_metadata(df, top_n=5):
    top_species = df['primary_label'].value_counts().head(top_n).index.tolist()
    df_sub = df[df['primary_label'].isin(top_species)].copy()
    features = ['latitude', 'longitude', 'rating']
    df_sub = df_sub.dropna(subset=features)
    return df_sub[features], df_sub['primary_label']

def compute_melspec(audio_path, sr=32000, n_mels=128, fmin=50, fmax=14000):
    y, _ = librosa.load(audio_path, sr=sr)
    melspec = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=n_mels, fmin=fmin, fmax=fmax)
    return y, sr, librosa.power_to_db(melspec, ref=np.max)
