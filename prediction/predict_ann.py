import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder, StandardScaler
from tensorflow.keras.models import load_model

model = load_model('genre_classification_model.h5')
model_bundle_loaded = joblib.load('models/model_bundle.pkl')

label_encoder_loaded = model_bundle_loaded['label_encoder']     #importing trained encoder and scaler
scaler_loaded = model_bundle_loaded['scaler']


single_feature_set = {                  #example feature set, change accordingly
    'danceability': 0.3,
    'energy': 0.2,
    'loudness': -5.0,
    'speechiness': 0.05,
    'acousticness': 0.9,
    'liveness': 0.1,
    'instrumentalness': 0.0,
    'valence': 0.6,
    'tempo': 120.0,
    'duration_ms': 210000
}

single_feature_df = pd.DataFrame([single_feature_set])
features = ['danceability', 'energy','loudness', 'speechiness', 'acousticness', 'liveness', 'instrumentalness', 'valence', 'tempo', 'duration_ms']

single_feature_values = single_feature_df[features].values

single_input_scaled = scaler_loaded.transform(single_feature_values)




single_prediction_probabilities = model.predict(single_input_scaled)
single_prediction = single_prediction_probabilities.argmax(axis=1)

decoded_prediction = label_encoder_loaded.inverse_transform(single_prediction)

print(decoded_prediction[0])
