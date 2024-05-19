import joblib
import os
# from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import pandas as pd

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'genre_classifier_rf.pkl')
model_loaded = joblib.load(MODEL_PATH) #change the suffix to knn or dt accordingly

clf_loaded = model_loaded['model']
label_encoder_loaded = model_loaded['label_encoder']
scaler_loaded = model_loaded['scaler']

def index(request):
    return HttpResponse("Hello, world. This is the index view.")

def predict(request):
    output=""
    try:
        data={
        'danceability':float(request.GET['danceability']),
        'energy':float(request.GET['energy']),
        'speechiness':float(request.GET['speechiness']),
        'acousticness':float(request.GET['acousticness']),
        'instrumentalness':float(request.GET['instrumentalness']),
        'valence':float(request.GET['valence']),
        'tempo':float(request.GET['tempo']),
        'duration_ms':float(request.GET['duration']),
        }

        single_input_df = pd.DataFrame([data])
        print(single_input_df)

        single_input_scaled = scaler_loaded.transform(single_input_df)
        print(single_input_scaled)
        single_prediction = clf_loaded.predict(single_input_scaled)

        decoded_prediction = label_encoder_loaded.inverse_transform(single_prediction)
        print(decoded_prediction[0])
        output=decoded_prediction[0]

    except:
        pass
    return JsonResponse({'genre':output})


#http://127.0.0.1:8000/genreApp/predict/?danceability=0.41&energy=0.65&acousticness=0.22&speechiness=0.21&instrumentalness=0.55&tempo=120&valence=0.43&duration=12400