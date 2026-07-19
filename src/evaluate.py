import tensorflow as tf
import numpy as np
from sklearn.metrics import classification_report,confusion_matrix
from preprocess import test_dataset, class_names
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
from config import MODEL_PATH

def main():

    model = tf.keras.models.load_model(MODEL_PATH)

    test_loss,test_accuracy = model.evaluate(test_dataset)
    print("\nTest Accuracy : ",test_accuracy)
    print("\nTest Loss : ",test_loss)

    #predict on test dataset
    predictions = model.predict(test_dataset)

    #convert probabilities to class labels
    predicted_labels = np.argmax(predictions,axis=1)

    true_labels = []
    all_images = []
    for images,labels in test_dataset:
        true_labels.extend(labels.numpy())
        all_images.extend(images.numpy())
    
    cm = confusion_matrix(true_labels,predicted_labels)
    print("\nConfusion Matrix : ")
    print(cm)

    report = classification_report(
        true_labels,
        predicted_labels,   
        target_names=class_names
    )
    print("\nClassification Report :\n")
    print(report)

    wrong_count = 1
    correct_count = 1
    MAX_CORRECT_IMAGES = 20
    MAX_WRONG_IMAGES = 50

    for i in range(len(true_labels)):
       true_label = true_labels[i]
       predicted_label = predicted_labels[i]   
       image =  np.clip(all_images[i], 0, 255).astype(np.uint8)
       if true_label != predicted_label and wrong_count <= MAX_WRONG_IMAGES:
          plt.figure(figsize=(4, 4))
          plt.imshow(image)
          plt.title(
            f"True : {class_names[true_label]}\n"
            f"Pred : {class_names[predicted_label]}"
          )
          plt.axis("off")
          plt.savefig(
              f"../outputs/predictions/wrong/"
              f"{class_names[true_label]}_to_{class_names[predicted_label]}_{wrong_count:03d}.png",
              dpi=300
            )
          plt.close()
          wrong_count += 1
       else:
          if correct_count <= MAX_CORRECT_IMAGES:
            plt.figure(figsize=(4, 4))
            plt.imshow(image)
            plt.title(
               f"True : {class_names[true_label]}\n"
               f"Pred : {class_names[predicted_label]}"
            )
            plt.axis("off")
            plt.savefig(
               f"../outputs/predictions/correct/correct_{correct_count:03d}.png",
               dpi=300
            )
            plt.close()
            correct_count += 1


    with open("../outputs/reports/classification_report.txt", "w") as file:
       file.write(report)

    # Plot confusion matrix
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=class_names)
    disp.plot(
       cmap="Blues",
       xticks_rotation=45,
       values_format="d"
    )
    plt.tight_layout()
    plt.savefig(
       "../outputs/confusion_matrix/confusion_matrix.png",
       dpi=300
    )
    plt.show()
    plt.close()

    print("\nEvaluation completed successfully.")

    print("Classification report saved to:")
    print("../outputs/reports/classification_report.txt")

    print("Confusion matrix saved to:")
    print("../outputs/confusion_matrix/confusion_matrix.png")

    print("\nPrediction images saved successfully.")
    print(f"Wrong Predictions   : {wrong_count - 1}")
    print(f"Correct Predictions : {min(correct_count - 1, MAX_CORRECT_IMAGES)}")
    
if __name__ == "__main__":
    main()