# Use a pipeline as a high-level helper
from transformers import pipeline
from PIL import Image
pipe = pipeline("image-classification", model="ayoubkirouane/VIT_Beans_Leaf_Disease_Classifier")

def run(image_path) : 
    image = Image.open(image_path)
    result = pipe(image)
    predicted_label = result[0]['label']
    confidence_score = result[0]['score']
    return [{"Predicted Label" : predicted_label } , {"Confidence Score" : confidence_score}]
