import joblib
import pandas as pd

single_input = {            #example feature set, change accordingly
    'danceability': 0.9,
    'energy': 0.3,
    'loudness': -12.0,
    'speechiness': 0.1,
    'acousticness': 0.2,
    'instrumentalness': 0.7,
    'valence': 0.3,
    'tempo': 120.0,
    'duration_ms': 210000
}

single_input_df = pd.DataFrame([single_input])

model_loaded = joblib.load('models/genre_classifier_knn.pkl') #change the suffix to knn or dt accordingly

clf_loaded = model_loaded['model']
label_encoder_loaded = model_loaded['label_encoder']
scaler_loaded = model_loaded['scaler']

single_input_scaled = scaler_loaded.transform(single_input_df)

single_prediction = clf_loaded.predict(single_input_scaled)

decoded_prediction = label_encoder_loaded.inverse_transform(single_prediction)

print(decoded_prediction[0])
