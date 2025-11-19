📌 Fake News Detection using NLP (Django Web App)
Authors: Shreya, Bhumika, Rah, Ishan

You can paste this directly into your GitHub repository.

📰 Fake News Detection using NLP (Django Web App)

This project is a web-based Fake News Detection system built using Django and Natural Language Processing (NLP).
It allows users to submit a news headline or full article and instantly receive a prediction:
✔ REAL
✔ FAKE

The system uses a trained machine learning model with TF-IDF vectorization + Passive Aggressive Classifier, optimized for text classification tasks.

🚀 Features

🔍 Detects whether entered news text is real or fake

🧹 End-to-end text preprocessing

🤖 Machine learning model trained on real-world dataset

🌐 Simple and responsive Django-based web interface

💾 Includes model training script and dataset

⚡ Fast predictions using pre-trained .joblib model files

📁 Project Structure
Fake-News-Detection-Django/
│── fakenews/                     # Django project settings
│── detector/                     # Main app
│   ├── templates/
│   │   └── index.html            # Frontend UI
│   ├── models.py
│   ├── views.py                  # Prediction logic
│   ├── urls.py
│── pac_model.joblib              # Trained ML model
│── tfidf_vectorizer.joblib       # TF-IDF vectorizer
│── model_trainer.py              # ML model training script
│── news.csv                      # Dataset used for training
│── manage.py
│── README.md
│── requirements.txt

🧠 How the Model Works

The Fake News Classifier uses:

🔡 Feature Extraction

TF-IDF Vectorizer

Converts text into numerical vectors

Removes stop words, normalizes text, etc.

🤖 Machine Learning Algorithm

Passive Aggressive Classifier (PAC)

Ideal for online & real-time classification

Handles large datasets efficiently

📊 Dataset

The model is trained on a labeled news dataset (news.csv) containing:

News text/content

Labels: REAL or FAKE

You may replace the dataset with your own for retraining.

🧪 Training the Model

To retrain the model, run:

python model_trainer.py


This will:
✔ Preprocess the dataset
✔ Train TF-IDF Vectorizer
✔ Train PAC model
✔ Save both as .joblib files

💻 Running the Django Web App
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run migrations
python manage.py migrate

3️⃣ Start the server
python manage.py runserver

4️⃣ Open the app

Visit:
👉 http://127.0.0.1:8000/

🧭 How to Use

Open the web app

Enter any news headline or paragraph

Click Predict

Output will show whether the news is REAL or FAKE

🛠️ Technologies Used
Backend

Django

Python

Machine Learning / NLP

Scikit-learn

TF-IDF

Passive Aggressive Classifier

Frontend

HTML5

CSS (basic)

🙌 Authors

Shreya Madne
Bhumika Shah
Raj Chaudhari
Ishan Saraf

📌 Future Improvements

Add news URL-based detection

Improve UI using Bootstrap

Add Explainable AI (why a news is fake)

Deploy model on AWS/Heroku

Add user login and history tracking
