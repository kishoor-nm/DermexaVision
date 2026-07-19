import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from config import MODEL_PATH,IMAGE_SIZE
from preprocess import class_names

model = tf.keras.models.load_model(MODEL_PATH)

def predict_image(image_path):
    img = image.load_img(image_path, target_size=IMAGE_SIZE)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array, verbose=0)

    predicted_index = np.argmax(prediction)
    predicted_class = class_names[predicted_index]
    confidence = np.max(prediction) * 100

    return predicted_class, confidence
def main():
    image_path = "../dataset/test/3. Akne/10.jpg"

    predicted_class, confidence = predict_image(image_path)

    print(f"Prediction : {predicted_class}")
    print(f"Confidence : {confidence:.2f}%")

if __name__ == "__main__":
    main()