# TFT Post-Game Analytics

This project focuses on analyzing post-game data for Teamfight Tactics (TFT) using various machine learning and deep learning techniques. The goal is to explore the relationship between game features and player performance, optimize models using TensorRT, and compare performance metrics between PyTorch and TensorRT models.

## Table of Contents
- [Environment Setup](#environment-setup)
- [Data Preprocessing](#data-preprocessing)
- [Exploratory Data Analysis and Feature Engineering](#exploratory-data-analysis-and-feature-engineering)
- [Model Training](#model-training)
- [Model Optimization and Inference](#model-optimization-and-inference)
- [Model Comparison](#model-comparison)
- [Results](#results)

## Environment Setup

Ensure you have the following dependencies installed:
- Python 3.8 or later
- PyTorch
- TensorRT
- PyCUDA
- NumPy
- pandas
- matplotlib
- seaborn
- scikit-learn
- onnx
- onnxruntime
- psutil

You can install the dependencies using pip:

```bash
pip install torch torchvision torchaudio tensorrt pycuda numpy pandas matplotlib seaborn scikit-learn onnx onnxruntime psutil
```

Create an .env file and add in your RIOT_API_KEY:

```.env
RIOT_API_KEY = "ENTER YOUR RIOT API KEY HERE"
```

## Data Collection

Run the collection script:

```bash
python src/data_collection/data_collection.py <Riot ID> <Riot Tag>
```

## Data Preprocessing

Data preprocessing involves loading raw match data, extracting relevant features, and saving the processed data for further analysis. The preprocessing.py script handles this.

### Steps:
1. Load raw JSON data files.
2. Extract relevant participant information.
3. Add traits and units information.
4. Save the processed data to a CSV file.

Run the preprocessing script:

```bash
python src/data_preprocessing/preprocessing.py
```



