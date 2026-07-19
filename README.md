# 🩺 DermexaVision

> **AI-Powered Skin Condition Classification using a Custom Convolutional Neural Network (CNN)**

![Python](https://img.shields.io/badge/Python-3.11-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![Keras](https://img.shields.io/badge/Keras-Deep%20Learning-red)
![License](https://img.shields.io/badge/License-MIT-green)
![Version](https://img.shields.io/badge/Version-v1.1.0-blueviolet)

---

# 📖 Overview

DermexaVision is a deep learning project that classifies human skin conditions from images using a **Custom Convolutional Neural Network (CNN)** built entirely from scratch with **TensorFlow** and **Keras**.

The project demonstrates an end-to-end deep learning workflow, including image preprocessing, data augmentation, CNN model development, model training, evaluation, and prediction. It follows a modular project structure to improve readability, maintainability, and scalability.

This project was developed for educational, research, and portfolio purposes while following clean coding practices and semantic versioning.

---

# ✨ Features

- Custom CNN built from scratch
- Image preprocessing pipeline
- Data augmentation
- Modular project architecture
- Configuration management (`config.py`)
- EarlyStopping callback
- ModelCheckpoint callback
- ReduceLROnPlateau callback
- Model evaluation pipeline
- Classification report generation
- Confusion matrix generation
- Image prediction with confidence score
- Professional project structure

---

# 📂 Project Structure

```text
DermexaVision/
│
├── dataset/
│   └── test/                 # Sample dataset (5 images × 7 classes)
│
├── models/                   # Generated after training
│
├── outputs/                  # Generated after evaluation
│
├── src/
│   ├── callbacks.py
│   ├── config.py
│   ├── evaluate.py
│   ├── metrics.py
│   ├── model.py
│   ├── predict.py
│   ├── preprocess.py
│   ├── train.py
│   └── visualization.py
│
├── CHANGELOG.md
├── LICENSE
├── README.md
├── VERSION
├── requirements.txt
└── .gitignore
```

---

# 📊 Dataset

The complete processed dataset used in this project is publicly available on Kaggle.

## Processed Dataset

https://www.kaggle.com/datasets/kishoornm/dermexavision-skin-condition-image-dataset

The dataset has been:

- Cleaned
- Reorganized
- Split into Training, Validation, and Testing sets

To keep this repository lightweight, only a **sample testing dataset** is included.

The repository contains:

- **7 Skin Condition Classes**
- **5 Sample Test Images for Each Class**

The complete dataset can be downloaded from the Kaggle link above.

---

# 📚 Original Dataset Credits

The processed dataset was created by combining and reorganizing images from the following publicly available Kaggle datasets.

### Skin Diseases

https://www.kaggle.com/datasets/ascanipek/skin-diseases

### Human Skin Diseases (Image)

https://www.kaggle.com/datasets/youssefmohmmed/human-skin-diseases-image

The images were cleaned, reorganized, and divided into training, validation, and testing folders for educational and research purposes.

**Image copyrights remain with the original dataset creators.**

---

# 🧠 CNN Architecture

```text
Input Image
      │
      ▼
Rescaling
      │
      ▼
Conv2D (32)
      │
      ▼
MaxPooling2D
      │
      ▼
Conv2D (64)
      │
      ▼
MaxPooling2D
      │
      ▼
Conv2D (128)
      │
      ▼
Flatten
      │
      ▼
Dense (128)
      │
      ▼
Dropout
      │
      ▼
Output Layer (Softmax)
```

---

# ⚙️ Training Configuration

| Parameter | Value |
|-----------|-------|
| Image Size | 128 × 128 |
| Batch Size | 32 |
| Optimizer | Adam |
| Learning Rate | 0.001 |
| Epochs | 20 |
| Loss Function | Sparse Categorical Crossentropy |

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/kishoor-nm/DermexaVision.git
```

Navigate to the project

```bash
cd DermexaVision
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🏋️ Train the Model

```bash
python src/train.py
```

The trained model will automatically be saved inside the `models/` directory.

> **Note:** Trained model files are not included in this repository because they are generated after training.

---

# 📈 Evaluate the Model

```bash
python src/evaluate.py
```

The evaluation pipeline generates:

- Test Accuracy
- Classification Report
- Confusion Matrix
- Prediction Visualizations

---

# 🔍 Predict an Image

```bash
python src/predict.py
```

The prediction script outputs:

- Predicted Skin Condition
- Confidence Score

---

# 🛠 Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib
- Scikit-learn
- Pillow

---

# 🗺 Roadmap

## ✅ Version 1.0.0

- Dataset Preparation
- Custom CNN Development
- Model Training
- Model Evaluation

---

## ✅ Version 1.1.0

- Modular Project Structure
- Configuration Management
- Callback Integration
- Improved Evaluation Pipeline
- Improved Prediction Pipeline
- Code Refactoring

---

## 🚧 Version 1.2.0 (Planned)

- Explainable AI (Grad-CAM)
- CNN Architecture Improvements
- Enhanced Performance
- Better Visualization

---

## 🚀 Version 2.0.0 (Future)

- Web Application
- REST API
- Real-Time Prediction
- Cloud Deployment
- User Authentication

---

# 📄 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for more information.

---

# 👨‍💻 Author

**Kishoor NM**

Artificial Intelligence & Machine Learning Student

GitHub: https://github.com/kishoor-nm

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

Your support motivates future development and helps improve the project.
