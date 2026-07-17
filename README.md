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

---
