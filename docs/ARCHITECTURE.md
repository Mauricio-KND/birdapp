# Architectural Decisions

## Core Design-Stack
1. **Backend - API Framework**: FastAPI for async support and OpenAPI docs.
2. **Audio Processing**: Librosa for spectrogram extraction (industry-standard FFT).
3. **Testing**: pytest with 100% endpoint coverage.
4. **Error Handling**:
   - 400 for invalid files
   - 500 for server errors with cleanup

## Next Steps
- Integrate BirdNET model
- Add noise reduction

## Key Branches
- `main` - Production-ready code only
- `dev` - Integration branch
- `feature/*` - Short-lived feature branches

## Week 1 Choices
- Used raw FastAPI over Flask for:
  - Native async support
  - Automatic OpenAPI docs
- Temporary file handling instead of in-memory processing:
  - Better for large audio files
  - Easier debugging