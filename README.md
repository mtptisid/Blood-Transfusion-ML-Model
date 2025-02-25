# 🩸 Blood Donation Prediction

This project builds a machine learning model to predict whether a person will donate blood. It uses a **Random Forest classifier** and a **Streamlit app** for user interaction.

## 📂 Dataset Information

The dataset is based on blood donation records from a **Blood Transfusion Service Center** in Taiwan.

### **Features:**
- **Recency**: Months since last donation
- **Frequency**: Total number of donations
- **Monetary**: Total blood donated in c.c.
- **Time**: Months since the first donation
- **Target**:  
  - `1`: Donated blood in March 2007  
  - `0`: Did not donate blood in March 2007  

---

## 🚀 Installation

First, install the required dependencies:

```bash
pip install pandas numpy scikit-learn streamlit joblib xgboost
```

---

## 📌 Train and Save the Model

- Load the dataset and preprocess it.
- Train a **Random Forest classifier**.
- Save the model using `joblib`.

---

## 🎨 Streamlit App

- Load the saved model and scaler.
- Create a **Streamlit UI** for user input.
- Predict blood donation likelihood.

---

## 🏃‍♂️ Run the App

Execute the following command to launch the Streamlit app:

```bash
streamlit run app.py
```

---

## 📈 Model Performance

- Model: **Random Forest Classifier**
- Accuracy: **(To be updated after training)**
- Evaluation Metrics: **Precision, Recall, F1-score**
  
---

## 🛠 Future Improvements

- Improve model accuracy with **Hyperparameter Tuning**
- Add support for **XGBoost** for better predictions
- Deploy the app using **Docker or Streamlit Cloud**

---

## 📜 License

This project is open-source and available for modifications.

---

🔥 **Happy Coding!** 🚀