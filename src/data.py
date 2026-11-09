# Ses yükleme ve spektrogram dönüşümleri
import librosa
import numpy as np

def load_audio(path, sr=32000):
    y, _ = librosa.load(path, sr=sr)
    return y, sr

def compute_melspec(y, sr=32000, n_mels=128, fmin=50, fmax=14000):
    melspec = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=n_mels, fmin=fmin, fmax=fmax)
    return librosa.power_to_db(melspec, ref=np.max)

def extract_features(y, sr=32000):
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)
    return np.mean(mfcc, axis=1)
