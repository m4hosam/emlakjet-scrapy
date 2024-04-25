from flask import Flask, render_template, request
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
import pickle

app = Flask(__name__)

# Load the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model_path = 'trained_model.pkl'
# Predict the house price using the trained model
with open('trained_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)
# predicted_price = loaded_model.predict(house_data)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = ['Net Metrekare', 'Oda Sayısı', 'Bulunduğu Kat', 'Banyo Sayısı', 'Binanın Yaşı', 'Binanın Kat Sayısı', 'Site İçerisinde']
    house_data = {}
    for feature in features:
        house_data[feature] = float(request.form[feature])

    house_data = pd.DataFrame(house_data, index=[0])

    # print(house_data)

    # Preprocess the house data
    for column in house_data.columns:
        if house_data[column].dtype == 'object':
            le = LabelEncoder()
            house_data[column] = le.fit_transform(house_data[column])

    # Predict the house price
    predicted_price = loaded_model.predict(house_data)
    # round the price to 6 points
    predicted_price_round = round(predicted_price[0], 6)

    return str(predicted_price_round)

if __name__ == '__main__':
    app.run(debug=True)
