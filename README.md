# GROUP22_CENG313
# CENG313 Data Science Project - GROUP22

## Proje Bilgileri
* **Yarışma:** BirdCLEF 2025 (Kaggle)
* **Öğrenci Adı Soyadı:** Mehmet Emin Arık
* **Öğrenci Numarası:** 24118080092
* **GitHub Kullanıcı Adı:** emnnark
* **Kaggle Profili:** https://www.kaggle.com/emnark

## Proje Tanımı
Bu projede Kolombiya El Silencio bölgesindeki 200'den fazla hayvan türünün ses kayıtları üzerinden tür tespiti yapılması hedeflenmektedir.

## Repository Yapısı
* `assignment1.ipynb`: Keşifçi Veri Analizi (EDA) ve Temel Model (Baseline)
* `src/`: Veri işleme, model ve yardımcı scriptler
  
## Assignment 1 Results (EDA & Baseline)
* **EDA Analysis:**
  * Analyzed metadata class imbalance (top species like grekis, compau vs rare classes).
  * Evaluated recording quality ratings and audio duration distributions.
  * Extracted and visualized waveforms and Mel-spectrograms at 32 kHz sampling rate.
* **Baseline Model:** Random Forest Classifier (`n_estimators=100`)
* **Evaluation Metric:** Macro ROC-AUC
* **Validation Score:** 0.7599
