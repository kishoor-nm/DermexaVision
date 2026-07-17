import tensorflow as tf
from tensorflow.keras import layers,models

def build_model():
    model = models.Sequential([
       #Input layer
       layers.Input(shape=(128,128,3)),
       #Normalization layer
       layers.Rescaling(1./255),
       #First CNN Block
       layers.Conv2D(32, (3,3), activation='relu'),
       layers.MaxPooling2D(pool_size=(2,2)),
       #Second CNN Block
       layers.Conv2D(64,(3,3),activation='relu'),
       layers.MaxPooling2D(pool_size=(2,2)),
       #Third CNN Block
       layers.Conv2D(128,(3,3),activation='relu'),
       #Convert feature maps to a 1D vector
       layers.Flatten(),
       #Fully connected layer
       layers.Dense(128,activation='relu'),
       #reduce overfitting
       layers.Dropout(0.5),
       #Output layer
       layers.Dense(7,activation='softmax')  
    ])
    
    return model

if __name__ == "__main__":
    model = build_model()
    model.summary()