# BirdApp :bird: 

Identify bird species from their songs using AI.

## Week 1 Progress
✅ Audio upload API  
✅ Species identification mock  
✅ Unit tests

### Quick Start
```bash
git clone https://github.com/yourname/birdapp
cd birdapp/backend
pip install -e .
uvicorn app.main:app --reload

### Test

# With test audio (from project root)
http --multipart POST http://localhost:8000/identify-bird/ \
  audio@backend/tests/test_data/bird_sample.mp3

## Project Tree (Key Files)

tree -I "venv|__pycache__|*.egg-info" --dirsfirst
