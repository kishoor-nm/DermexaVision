# ==========================================
# DermexaVision Configuration File
# Version : 1.1.0
# ==========================================
from pathlib import Path

#Image Settings
IMAGE_SIZE = (128,128)

#Training Settings
BATCH_SIZE = 32
EPOCHS = 30
LEARNING_RATE = 0.001

#Dataset Paths
BASE_DIR = Path(__file__).resolve().parent.parent
TRAIN_DIR = BASE_DIR/"dataset"/"train"
VAL_DIR = '../dataset/val'    
TEST_DIR = '../dataset/test'

# Model Path
MODEL_PATH = BASE_DIR/"models"/"v1.1.0_ablation_no_bn_ep30.keras"

# Random Seed
SEED = 42