import tensorflow as tf
import numpy as np
from sklearn.metrics import classification_report,confusion_matrix
from model import build_model
from preprocess import test_dataset
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

model = tf.keras.models.load_model("../models/best_model.keras")

test_loss,test_accuracy = model.evaluate(test_dataset)
print("\nTest Accuracy : ",test_accuracy)
print("\nTest Loss : ",test_loss)

#predict on test dataset
predictions = model.predict(test_dataset)

#convert probabilities to class labels
predicted_labels = np.argmax(predictions,axis=1)

true_labels = []
for images,labels in test_dataset:
    true_labels.extend(labels.numpy())
    
cm = confusion_matrix(true_labels,predicted_labels)
print("\nConfusion Matrix : ")
print(cm)

class_names = test_dataset.class_names
print("\nClassification Report :\n")
print(
    classification_report(
        true_labels,
        predicted_labels,   
        target_names=class_names
    )
)


# Plot confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=class_names)
disp.plot(cmap="Blues")
plt.xticks(rotation=45)
plt.show()

