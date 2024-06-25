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

The processed match data will be saved in ``` data/processed/tft_match_data.csv ```

## Exploratory Data Analysis and Feature Engineering

Exploratory Data Analysis (EDA) involves understanding the data distribution, correlations, and feature engineering to create new meaningful features.

### Steps:
1. Load the processed data.
2. Perform data cleaning and fill missing values.
3. Analyze popular activated traits.
4. Create new features such as num_activated_traits, total_unit_values, avg_unit_tiers, avg_unit_rarities.
5. Save the engineered data.

Run the EDA and feature engineering notebook: 
```bash
notebooks/eda/eda_feature_eng.ipynb 
```

The engineered data will be saved in ``` data/processed/tft_match_data_with_features.csv ```

## Model Training
Train a Deep Q-Network (DQN) agent to predict player performance based on the game features.

### Steps:
1. Define the TFT environment.
2. Implement the DQN model using PyTorch.
3. Train the model.
4. Save the trained model.

Run the model training notebook:
```bash
notebooks/model_training/train_model.ipynb
```

## Model Optimization, Inference, Comparison
Optimize the trained PyTorch model using TensorRT for faster inference. Then, compare the performance of the PyTorch and TensorRT models across various metrics.

### Steps:
1. Convert the PyTorch model to ONNX format.
2. Optimize the ONNX model using TensorRT.
3. Allocate buffers and perform inference using TensorRT.

### Comparison Metrics:
- Throughput (inferences per second)
- Memory usage (current and peak)
- Latency (mean and standard deviation)
- Power consumption
- Accuracy comparison (mean absolute error and mean squared error)

Run the model optimization notebook:
```bash
notebooks/model_optimizing/model_optimization.ipynb
```

## Conclusion

This project demonstrates the end-to-end process of analyzing TFT post-game data, training a DQN agent, optimizing the model using TensorRT, and comparing performance metrics. The optimized TensorRT model shows improvements in throughput and latency, making it suitable for deployment in real-time systems.

Feel free to contribute to this project by opening issues or submitting pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.