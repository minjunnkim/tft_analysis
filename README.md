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
- Python 3.8 or later (Used 3.11.9)
- CUDA (Used, 11.8) : https://developer.nvidia.com/cuda-11-8-0-download-archive
- TensorRT (Used, 10.1.0) : https://developer.nvidia.com/tensorrt/download/10x
- cuDNN (Optional, 8.9.7) : https://developer.nvidia.com/rdp/cudnn-archive 

You can install the dependencies using pip:

```bash
pip install -r requirements.txt
```

## Riot API

Go to Riot Games Developer Website, https://developer.riotgames.com/, and obtain a Development API Key.

Create an .env file and add in your RIOT_API_KEY:

```.env
RIOT_API_KEY = "ENTER YOUR RIOT API KEY HERE"
```

## Data Collection

Run the collection script with the Riot ID of the player you want to collect data from:

```bash
python src/data_collection/data_collection.py <Game Name> <Riot Tag>
```

The match data files in .json format will be saved under ``` data/raw/ ```

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



