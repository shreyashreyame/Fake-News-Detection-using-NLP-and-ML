from django.shortcuts import render
import joblib
import os
from django.conf import settings
print("BASE_DIR →", settings.BASE_DIR)

# --- 1. Load the Model and Vectorizer ---
# We try to load the saved "brains" from the joblib files
try:
    MODEL_PATH = os.path.join(settings.BASE_DIR, 'pac_model.joblib')
    VEC_PATH = os.path.join(settings.BASE_DIR, 'tfidf_vectorizer.joblib')

    print("Looking for model at:", MODEL_PATH)
    print("Looking for vectorizer at:", VEC_PATH)

    pac_model = joblib.load(MODEL_PATH)
    tfidf_vectorizer = joblib.load(VEC_PATH)
    MODEL_LOADED = True
    print("✅ Model loaded successfully!")
except Exception as e:
    print("❌ Error loading model:", e)
    MODEL_LOADED = False



# --- 2. Prediction Function: Takes news text and gives a result ---
def predict_fake_news(news_text):
    if not MODEL_LOADED:
        return "ERROR: Model files not found. Check Step 4."

    # Convert the text into numbers the model understands
    tfidf_test = tfidf_vectorizer.transform([news_text])

    # Get the prediction (0 or 1)
    prediction = pac_model.predict(tfidf_test)[0]

    if prediction == 0:
        return "REAL ✅"
    else:
        return "FAKE ❌"


# --- 3. Homepage Function: Handles the web page display and button clicks ---
def homepage(request):
    prediction_result = None
    news_input = ""

    if request.method == 'POST':
        # This runs when the user clicks the "Check News!" button
        news_article = request.POST.get('news_text', '')
        news_input = news_article

        if news_article:
            prediction_result = predict_fake_news(news_article)

    # Prepare data to send to the HTML template
    context = {
        'prediction': prediction_result,
        'news_input': news_input
    }

    # Tell Django to show the index.html page
    return render(request, 'index.html', context)

MODEL_PATH = os.path.join(settings.BASE_DIR, 'pac_model.joblib')
VEC_PATH = os.path.join(settings.BASE_DIR, 'tfidf_vectorizer.joblib')
