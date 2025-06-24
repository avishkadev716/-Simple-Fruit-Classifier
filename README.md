# -Simple-Fruit-Classifier
My First  simple AI/ ML project
 🍎 Simple Fruit Classifier 

This is a beginner-friendly machine learning project that classifies fruit images (Apple or Banana) using a Convolutional Neural Network (CNN).

🔍 Project Overview
- A lightweight CNN is trained on a small custom dataset with two classes: `Apple` and `Banana`.
- Built using TensorFlow/Keras and easily runnable on **Google Colab**.
- Includes an optional **Streamlit UI app** to test predictions with uploaded images.

 📦 Features
- Image classification with CNN
- Small dataset (ideal for practice)
- Ready-to-run Colab notebook
- Streamlit web interface (optional)

 🗂 Dataset
The dataset contains a small set of labeled fruit images:

```
apple-banana-small/
  ├── Apple/
  └── Banana/
```

(Each folder contains ~20–50 JPG images)

🚀 How to Run

🧠 Train the Model (in Google Colab)
```python
model.fit(X_train, y_train, epochs=5, validation_data=(X_test, y_test))
```
💾 Save the Model
```python
model.save("simple_fruit_model.h5")
```

 🌐 Run the Streamlit App (Optional)
```bash
streamlit run fruit_ui.py
```
 📁 Files Included
- `fruit_classifier.ipynb`: Google Colab notebook
- `fruit_ui.py`: Streamlit app for testing
- `simple_fruit_model.h5`: Trained model file (optional upload)

 🧠 Skills Practiced
- Image preprocessing
- CNN model creation
- Binary classification
- Streamlit app development
