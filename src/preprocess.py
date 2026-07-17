import tensorflow as tf
import matplotlib.pyplot as plt

#image size
IMAGE_SIZE = (128,128)

#batch size
BATCH_SIZE = 32

#dataset path
TRAINING_DIR = '../dataset/train'
VALIDATION_DIR = '../dataset/val'
TESTING_DIR = '../dataset/test'

#load training dataset
train_dataset = tf.keras.utils.image_dataset_from_directory(
    TRAINING_DIR,
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=True
)
#load validation dataset
val_dataset = tf.keras.utils.image_dataset_from_directory(
    VALIDATION_DIR,
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=False
)
#load testing dataset
test_dataset = tf.keras.utils.image_dataset_from_directory(
    TESTING_DIR,
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=False
)

for images,labels in train_dataset.take(1):
    plt.figure(figsize=(10,10))
    for i in range(9):
        ax = plt.subplot(3,3,i+1)
        ax.imshow(images[i].numpy().astype("uint8"))
        plt.title(train_dataset.class_names[labels[i]])
        plt.axis("off")
    plt.show()