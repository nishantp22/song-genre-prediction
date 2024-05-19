import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

df=pd.read_csv('datasets/dataset.csv')

features = ['danceability', 'energy','loudness', 'speechiness', 'acousticness', 'instrumentalness', 'valence', 'tempo', 'duration_ms']
X = df[features]
y = df['genre']

label_encoder = LabelEncoder()          #encoding the target classses(output)
y_encoded = label_encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.3, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


clf = RandomForestClassifier(n_estimators=181, random_state=42)
clf.fit(X_train_scaled, y_train)


os.makedirs('models', exist_ok=True)

genre_classifier_rf = {
    'model': clf,
    'label_encoder': label_encoder,
    'scaler': scaler
}

joblib.dump(genre_classifier_rf, 'models/genre_classifier_rf.pkl')



y_pred = clf.predict(X_test_scaled)     # for predictions and evaluating the model
from sklearn.metrics import accuracy_score, classification_report
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))


