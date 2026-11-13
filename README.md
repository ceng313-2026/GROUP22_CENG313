# GROUP22_CENG313
# CENG313 Data Science Project - GROUP22

## Proje Bilgileri
* **Yarışma:** BirdCLEF 2025 (Kaggle)(https://www.kaggle.com/competitions/birdclef-2025)
* **Öğrenci Adı Soyadı:** Mehmet Emin Arık
* **Öğrenci Numarası:** 24118080092
* **GitHub Kullanıcı Adı:** emnark
* **Kaggle Profili:** https://www.kaggle.com/emnark

## Proje Tanımı
Bu projede Kolombiya El Silencio bölgesindeki 200'den fazla hayvan türünün ses kayıtları üzerinden tür tespiti yapılması hedeflenmektedir.

## Repository Yapısı
* `assignment1_eda_baseline.ipynb`: Keşifçi Veri Analizi (EDA) ve Temel Model (Baseline)
* `src/`: Veri işleme (`data.py`), model (`models.py`) ve yardımcı metrik (`utils.py`) scriptleri
* `requirements.txt`: Proje bağımlılıkları
* `submissions/`: Değerlendirme ve skor çıktıları

## Kurulum ve Veri İndirme (How to Download & Run)
Veri dosyaları boyut ve Kaggle kuralları gereği repoya dahil edilmemiştir.

1. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install -r requirements.txt
  
## Assignment 1 Results (EDA & Baseline)
* **Competition Status:** Competition closed — evaluated on a held-out split.
* **EDA Analysis:**
  * Analyzed metadata class imbalance (top species like `grekis`, `compau` vs rare classes).
  * Evaluated recording quality ratings and audio duration distributions.
  * Extracted and visualized waveforms and Mel-spectrograms at 32 kHz sampling rate.
* **Baseline Model:** Random Forest Classifier (`n_estimators=100`)
* **Evaluation Metric:** Macro ROC-AUC
* **Validation / Held-out Score:** 0.7599
