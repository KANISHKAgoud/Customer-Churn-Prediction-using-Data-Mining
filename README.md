# Customer-Churn-Prediction-using-Data-Mining

# 📊 Customer Churn Prediction - BI Mini Project

## 📌 Project Overview

This project focuses on predicting whether a customer will **churn (leave the service)** or not using historical data. It is a **classification problem** in data mining and is an important application in **Business Intelligence (BI)**.

The insights from this project help businesses take proactive decisions to **retain customers**.

---

## 🎯 Problem Statement

To identify customers who are likely to churn using a standard dataset and apply data mining techniques to support business decision-making.

---

## 🧠 Data Mining Task

* **Type:** Classification
* **Goal:** Predict churn (Yes/No)

---

## 📂 Project Structure

```
BI_Project/
│
├── data/
│   └── churn.csv
│
├── notebooks/
│   └── analysis.ipynb
│
├── src/
│   ├── preprocess.py
│   ├── train_model.py
│   └── evaluate.py
│
├── requirements.txt
└── main.py
```

---

## 📊 Dataset

* Dataset used: **Telco Customer Churn Dataset**
* Contains customer details such as:

  * Gender
  * Tenure
  * Monthly Charges
  * Total Charges
  * Churn (Target variable)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone or Download the Project

```
git clone <your-repo-link>
cd BI_Project
```

---

### 2️⃣ Install Required Libraries

```
pip install -r requirements.txt
```

---

### 3️⃣ Add Dataset

* Download dataset from Kaggle
* Rename file to:

```
churn.csv
```

* Place it inside:

```
data/
```

---

## 🚀 How to Run the Project

Run the main file:

```
python main.py
```

---

## 📈 Output

The model will display:

* Accuracy Score
* Classification Report including:

  * Precision
  * Recall
  * F1-score

---

## 📊 Sample Result

* Accuracy: ~74%
* Model performs better on **non-churn customers**
* Lower recall for churn indicates improvement area

---

## 💡 Business Insights

* Helps identify customers likely to leave
* Enables companies to take preventive actions
* Improves customer retention strategies

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn

---

## 🔍 Conclusion

This project successfully demonstrates how **data mining (classification)** can be applied in Business Intelligence to predict customer churn. While the model performs reasonably well, improving prediction of churn customers remains a key area for enhancement.

---

## 🚀 Future Improvements

* Improve model accuracy using advanced algorithms
* Handle data imbalance
* Deploy as a web application

---

## 👨‍💻 Author

Kanishka Goud

---
