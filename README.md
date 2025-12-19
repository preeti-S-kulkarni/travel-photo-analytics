# AI-Powered Travel Photo Analytics

## 📌 Project Overview
This project analyzes personal travel photos using **data engineering, data analytics, and AI** techniques.  
Raw image files are transformed into **structured, analytics-ready datasets** by extracting EXIF metadata such as timestamps, camera details, and GPS information.

The long-term goal of the project is to apply:
- Computer Vision
- Machine Learning
- Generative AI  
to understand travel behavior, detect trips automatically, and generate AI-driven travel insights.

✅ **Current status:** Step 1 – Advanced Data Ingestion (Completed)

---

## 🎯 Objectives
- Convert unstructured photo files into structured data
- Handle missing or corrupted metadata gracefully
- Build an industry-grade data ingestion pipeline
- Prepare the dataset for downstream analytics and ML

---

## 🏗️ Project Structure
Travel-photo-analytics/
├── data/
│ ├── raw_photos/ # Raw photos (excluded from Git)
│ └── metadata/
│ └── metadata_public_sample.csv
│
├── notebooks/
│ └── 01_exif_extraction.ipynb # Data ingestion notebook
│
├── utils/
│ └── exif_utils.py # Reusable EXIF extraction logic
│
├── requirements.txt
├── .gitignore
└── README.md
