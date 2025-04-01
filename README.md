# BirdApp - Avian Audio Identification

![Project Logo](misc/logo.png) *(optional)*

Identify bird species from their songs using machine learning.

## Features
- 🎵 Audio analysis via Librosa
- 🐦 Mock species detection (BirdNET integration coming soon)
- ✅ Tested API endpoints

## Quick Start
```bash
git clone https://github.com/your_username/birdapp.git
cd birdapp/backend
pip install -e .
uvicorn app.main:app --reload

API Docs: http://localhost:8000/docs
Test: pytest tests/ -v