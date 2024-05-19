import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization, Input
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.optimizers import Adam
import pandas as pd
import joblib
import os


df=pd.read_csv('datasets/dataset.csv')


features = ['danceability', 'energy', 'speechiness', 'acousticness', 'instrumentalness', 'valence', 'tempo', 'duration_ms']
X = df[features]
y = df['genre']

label_encoder = LabelEncoder()          # Encode the target classes
y_encoded = label_encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

scaler = StandardScaler()           # Standardization of the features
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


model = Sequential([            #neural network with 4 layers
    Dense(300, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    BatchNormalization(),
    Dropout(0.4),
    Dense(216, activation='relu'),
    BatchNormalization(),
    Dropout(0.4),
    Dense(128, activation='relu'),
    BatchNormalization(),
    Dropout(0.4),
    Dense(len(label_encoder.classes_), activation='softmax')
])


optimizer = Adam(learning_rate=0.001)
model.compile(optimizer=optimizer,
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)   # Early stopping callback to prevent overfitting

history = model.fit(X_train_scaled, y_train, epochs=100, batch_size=32, validation_split=0.2, callbacks=[early_stopping], verbose=1)


test_loss, test_accuracy = model.evaluate(X_test_scaled, y_test, verbose=0)
print("Test Accuracy:", test_accuracy)

os.makedirs('models', exist_ok=True)

model_bundle = {
    'scaler_ann': scaler,
    'label_encoder_ann': label_encoder,
}

model.save('models/genre_classification_model.h5')
joblib.dump(model_bundle, 'models/model_bundle.pkl')


y_pred_probabilities = model.predict(X_test_scaled)         #for prediction and evaluation
y_pred = y_pred_probabilities.argmax(axis=1)
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))
