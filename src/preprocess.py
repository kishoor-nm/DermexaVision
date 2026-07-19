import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras import layers
from config import (
    IMAGE_SIZE,
    BATCH_SIZE,
    TRAIN_DIR,
    VAL_DIR,
    TEST_DIR,
    SEED
)

data_augmentation = tf.keras.Sequential([
    layers.RandomFlip("horizontal"),
    layers.RandomRotation(0.05),
    layers.RandomZoom(0.10),
    layers.RandomContrast(0.10),
])

#load training dataset
train_dataset = tf.keras.utils.image_dataset_from_directory(
    TRAIN_DIR,
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=True,
    seed = SEED
)

class_names = train_dataset.class_names

AUTOTUNE = tf.data.AUTOTUNE   # Automatically optimizes data loading

train_dataset = train_dataset.map(
    lambda images,labels:(
        data_augmentation(images,training=True),
        labels
    ),
    num_parallel_calls=AUTOTUNE
)

#load validation dataset
val_dataset = tf.keras.utils.image_dataset_from_directory(
    VAL_DIR,
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=False
)
#load testing dataset
test_dataset = tf.keras.utils.image_dataset_from_directory(
    TEST_DIR,
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=False
)

train_dataset = train_dataset.prefetch(AUTOTUNE)
val_dataset = val_dataset.prefetch(AUTOTUNE)
test_dataset = test_dataset.prefetch(AUTOTUNE)   

def show_sample_images():
    for images, labels in train_dataset.take(1):
        plt.figure(figsize=(10,10))

        for i in range(9):
            ax = plt.subplot(3,3,i+1)

            plt.imshow(images[i].numpy().astype("uint8"))
            plt.title(class_names[labels[i]])
            plt.axis("off")

        plt.show()