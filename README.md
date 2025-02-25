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

## Screeshots

<img width="1440" alt="Screenshot 2025-02-25 at 3 27 29 PM" src="https://github.com/user-attachments/assets/4f466516-cbd3-4298-bbf2-ef5335a87d8b" />

<img width="1440" alt="Screenshot 2025-02-25 at 3 27 20 PM" src="https://github.com/user-attachments/assets/9d9b8dae-f0e2-46a6-ac44-f3139789f0ae" />

<img width="1440" alt="Screenshot 2025-02-25 at 3 28 27 PM" src="https://github.com/user-attachments/assets/aafd5669-e990-414f-9842-180b2496696d" />

<img width="1440" alt="Screenshot 2025-02-25 at 3 29 14 PM" src="https://github.com/user-attachments/assets/2f32c725-746f-409c-811a-18a95e6017fe" />

---

🔥 **Happy Coding!** 🚀
