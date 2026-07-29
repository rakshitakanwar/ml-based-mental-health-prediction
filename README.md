## 🧠 ML-Based Mental Health Prediction

##📌 Project Overview

Mental health has become one of the most important concerns in today's digital world. Excessive screen time, poor sleep habits, social isolation, and high stress levels can negatively impact an individual's mental well-being.

This project is a Machine Learning-based web application that predicts whether a person is likely to experience depression based on several lifestyle and mental health-related factors. The application provides instant predictions through a user-friendly Flask web interface.

The objective of this project is to demonstrate how Machine Learning can be integrated with a web application to build an intelligent prediction system.

---

## 🎯 Objectives

- Predict the likelihood of depression using Machine Learning.
- Analyze mental health-related user inputs.
- Provide instant predictions through a web interface.
- Demonstrate end-to-end ML model deployment using Flask.
- Create a simple, responsive, and easy-to-use application.

---

## ✨ Features

- 🧠 Machine Learning-based prediction
- 🌐 Flask Web Application
- 📊 Real-time prediction
- 📱 Responsive User Interface
- ⚡ Fast prediction response
- 💻 Easy to run locally
- 🔍 Clean project structure

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- Pandas
- NumPy
- Joblib

### Web Development
- Flask
- HTML5
- CSS3

### Version Control
- Git
- GitHub

---

## 📂 Project Structure

```
ml-based-mental-health-prediction/
│
├── templates/
│   └── index.html
│
├── app.py
├── model.pkl
├── screen_time_mental_health.csv
├── requirements.txt
├── Dockerfile
├── README.md
└── Untitled-1.ipynb
```

---

## 📊 Dataset

The project uses a Mental Health dataset containing information related to users' lifestyle and mental health indicators.

The dataset includes various features that help the Machine Learning model learn patterns associated with depression prediction.

Examples of features may include:

- Age
- Gender
- Screen Time
- Sleep Duration
- Stress Level
- Physical Activity
- Social Interaction
- Other mental health-related attributes

---

## ⚙️ Machine Learning Workflow

### Step 1 – Data Collection

The dataset is loaded into a Pandas DataFrame.

### Step 2 – Data Preprocessing

- Handling missing values
- Removing unnecessary columns
- Feature selection
- Data cleaning

### Step 3 – Model Training

The processed dataset is used to train a Machine Learning classification model.

### Step 4 – Model Evaluation

The model is evaluated using performance metrics such as:

- Accuracy
- Precision
- Recall
- F1 Score

### Step 5 – Model Saving

The trained model is saved as:

```
model.pkl
```

using Joblib.

### Step 6 – Flask Integration

The saved model is loaded inside the Flask application.

### Step 7 – Prediction

The user enters the required details through the web interface, and the trained model predicts whether the person is likely to be at risk of depression.

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/rakshitakanwar/ml-based-mental-health-prediction.git
```

### Move into Project Folder

```bash
cd ml-based-mental-health-prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Flask Application

```bash
python app.py
```

The application will start on

```
http://127.0.0.1:5000
```

Open the above URL in your browser.

---

## 💻 How It Works

```
User Inputs
      │
      ▼
HTML Form
      │
      ▼
Flask Backend
      │
      ▼
Load Trained Model
      │
      ▼
Prediction
      │
      ▼
Display Result
```

---

## 📈 Future Enhancements

- User Authentication
- Prediction History
- Better UI/UX
- Model Explainability
- Dashboard & Analytics
- Cloud Deployment
- Docker & Kubernetes Deployment
- REST API Support

---

## 📷 Application Screenshot

> Add screenshots of your application here.

Example:

```
Home Page

Prediction Result

Input Form
```

---

## 📌 Requirements

- Python 3.x
- Flask
- Pandas
- NumPy
- Scikit-learn
- Joblib

Install using

```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

Contributions are welcome!

If you'd like to improve this project:

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

## 👩‍💻 Author

**Rakshita Kanwar**

B.Tech (Computer Science - Artificial Intelligence)

GitHub:
https://github.com/rakshitakanwar

---

## ⭐ If you like this project

Give this repository a ⭐ on GitHub if you found it useful.
