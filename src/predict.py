import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

model = tf.keras.models.load_model("../models/best_model.keras")

class_names = [
    "Enfeksiyonel",
    "Ekzama",
    "Akne",
    "Pigment",
    "Benign",
    "Malign",
    "Normal"
]

image_path = "../dataset/test/3. Akne/1.png"  # Replace with the path to your image
img = image.load_img(
    image_path,
    target_size = (128,128)
)
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array,axis=0)

prediction = model.predict(img_array)
predicted_class = np.argmax(prediction)

confidence = np.max(prediction)
confidence = confidence * 100

print("Prediction :", class_names[predicted_class])
print("Confidence : {:.2f}%".format(confidence))