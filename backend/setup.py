from setuptools import setup, find_packages

setup(
    name="birdapp-backend",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.115.12",
        "librosa>=0.11.0",
        "numpy>=2.1.3",
        "uvicorn>=0.34.0",
    ],
)