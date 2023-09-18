# Beans Leaf Disease Classification App

## About : 

This is a Streamlit web application that utilizes a fine-tuned Vision Transformer (ViT) model to classify images of bean leaves into three categories: Angular Leaf Spot, Bean Rust, and Healthy. The model has been trained on the Beans leaf dataset, which contains images of diseased and healthy bean leaves.

## Model Information
* **Model Name**: VIT_Beans_Leaf_Disease_Classifier
* **Base Model**: Google/ViT-base-patch16-224-in21k
* **Task**: Image Classification (Beans Leaf Disease Classification)
* **Dataset**: Beans leaf dataset with images of diseased and healthy leaves.

## Problem Statement
The goal of this model is to classify leaf images into three categories:
```
{
  "angular_leaf_spot": 0,
  "bean_rust": 1,
  "healthy": 2,
}
```
![download](https://github.com/Kirouane-Ayoub/Beans-Leaf-Disease-Classification-App/assets/99510125/d9af6f48-f094-4264-b8d7-3fe7c7390fda)

### Training results : 

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.1495        | 1.54  | 100  | 0.0910          | 0.9774   |
| 0.0121        | 3.08  | 200  | 0.0155          | 1.0      |

## APP Usage : 

```
pip install -r requirements.txt
streamlit run app.py
```
