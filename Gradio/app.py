# Load model directly
from transformers import AutoFeatureExtractor, AutoModelForImageClassification
import torch
import gradio as gr

extractor = AutoFeatureExtractor.from_pretrained("ayoubkirouane/VIT_Beans_Leaf_Disease_Classifier")
model = AutoModelForImageClassification.from_pretrained("ayoubkirouane/VIT_Beans_Leaf_Disease_Classifier")

labels = ['angular_leaf_spot', 'bean_rust', 'healthy']

def classify(im):
  features = extractor(im, return_tensors='pt')
  logits = model(features["pixel_values"])[-1]
  probability = torch.nn.functional.softmax(logits, dim=-1)
  probs = probability[0].detach().numpy()
  confidences = {label: float(probs[i]) for i, label in enumerate(labels)} 
  return confidences
  
interface = gr.Interface(
    classify,
    inputs='image',
    outputs='label')

interface.launch(debug=True)
  
