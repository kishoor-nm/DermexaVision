from model import build_model
from tensorflow.keras.optimizers import Adam
from preprocess import train_dataset,val_dataset
import matplotlib.pyplot as plt
from callbacks import callbacks
from config import EPOCHS, LEARNING_RATE

model = build_model()

model.compile(
    optimizer=Adam(learning_rate=LEARNING_RATE),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)



history = model.fit(
    train_dataset,
    validation_data=val_dataset,
    epochs=EPOCHS,
    callbacks=callbacks
)

# Accuracy
plt.figure(figsize=(8, 6))
plt.plot(history.history["accuracy"], label="Training Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
plt.title("Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.savefig("../outputs/graphs/accuracy.png",dpi=300)
plt.show()
plt.close()

# Loss
plt.figure(figsize=(8, 6))
plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.title("Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.savefig("../outputs/graphs/loss.png",dpi=300)
plt.show()
plt.close()