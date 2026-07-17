# DermexaVision

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?logo=tensorflow)
![Keras](https://img.shields.io/badge/Keras-Deep%20Learning-D00000?logo=keras)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![Version](https://img.shields.io/badge/Version-v1.0.0-blue)

</p>

---

## AI-Powered Skin Disease Classification using Custom CNN

DermexaVision is a deep learning project developed to classify skin diseases from dermatoscopic images using a **Custom Convolutional Neural Network (CNN)** built completely from scratch with **TensorFlow** and **Keras**.

Unlike many image classification projects that rely on transfer learning models such as MobileNet, ResNet, or EfficientNet, DermexaVision demonstrates how a CNN can be designed, trained, and evaluated from the ground up.

The project covers the complete deep learning workflow, including:

- Image preprocessing
- Dataset preparation
- CNN architecture design
- Model training
- Validation
- Performance evaluation
- Disease prediction

This repository is intended for educational purposes, research, and learning deep learning fundamentals through medical image classification.

---

# Features

- Custom CNN built from scratch
- TensorFlow & Keras implementation
- Image preprocessing pipeline
- Dataset normalization
- Data augmentation
- ModelCheckpoint for saving the best model
- Performance evaluation
- Classification Report
- Confusion Matrix
- Prediction on unseen images
- Organized project structure
- Kaggle dataset support
- GitHub Release with trained model

---

# Supported Skin Conditions

The model classifies the following seven skin conditions:

| Class | Disease |
|--------|----------|
| 0 | Acne |
| 1 | Chickenpox |
| 2 | Eczema |
| 3 | Healthy Skin |
| 4 | Monkeypox |
| 5 | Psoriasis |
| 6 | Vitiligo |

---

# Project Structure

```text
DermexaVision/
│
├── dataset/
│   ├── train/
│   ├── valid/
│   └── test/
│
├── models/
│   └── README.md
│
├── outputs/
│
├── src/
│   ├── model.py
│   ├── train.py
│   ├── evaluate.py
│   ├── predict.py
│   └── preprocess.py
│
├── requirements.txt
├── README.md
├── CHANGELOG.md
├── LICENSE
└── .gitignore
```

---

# CNN Workflow

```text
Skin Image
      │
      ▼
Image Preprocessing
      │
      ▼
Data Augmentation
      │
      ▼
Custom CNN
      │
      ▼
Training
      │
      ▼
Validation
      │
      ▼
Best Model Saved
      │
      ▼
Evaluation
      │
      ▼
Prediction
```
# Dataset

DermexaVision uses a curated skin disease image dataset organized according to the standard deep learning directory structure.

```text
dataset/
├── train/
├── valid/
└── test/
```

The dataset contains images from seven skin condition classes and is split into training, validation, and testing subsets for model development and evaluation.

---

# Dataset Availability

The processed dataset is available on Kaggle:

**DermexaVision Skin Condition Image Dataset**

https://www.kaggle.com/datasets/kishoornm/dermexavision-skin-condition-image-dataset

---

# Original Dataset Attribution

This dataset was created by combining and reorganizing images from the following publicly available Kaggle datasets:

- Skin Diseases  
  https://www.kaggle.com/datasets/ascanipek/skin-diseases

- Human Skin Diseases (Image)  
  https://www.kaggle.com/datasets/youssefmohmmed/human-skin-diseases-image

The images were cleaned, reorganized, and split into training, validation, and testing sets for educational and research purposes.

**Image copyrights remain with the original dataset authors.**

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/kishoor-nm/DermexaVision.git

cd DermexaVision
```

---

## Create a Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Requirements

- Python 3.10+
- TensorFlow
- Keras
- NumPy
- Matplotlib
- Pillow
- OpenCV
- Scikit-learn

---

# Training

Start training by running:

```bash
python src/train.py
```

The training pipeline automatically:

- Loads the training and validation datasets
- Applies preprocessing and normalization
- Performs data augmentation
- Builds the custom CNN architecture
- Trains the model
- Validates the model after every epoch
- Saves the best-performing model using the built-in `ModelCheckpoint` callback

The trained model is saved as:

```text
models/
└── best_model.keras
```

---

# Model Evaluation

Evaluate the trained model using:

```bash
python src/evaluate.py
```

The evaluation script reports:

- Test Accuracy
- Test Loss
- Classification Report
- Confusion Matrix

---

# Prediction

Predict the skin condition for a new image using:

```bash
python src/predict.py
```

The script loads the trained model (`best_model.keras`) and returns the predicted skin disease class.

---

# Trained Model

The trained model is **not stored directly in the repository** because it exceeds GitHub's 100 MB file size limit.

You can download the latest trained model from the repository's **Releases** page.

After downloading, place the model in:

```text
models/
└── best_model.keras
```

The prediction and evaluation scripts will automatically load the model from this location.

---

---
