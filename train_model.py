import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
import pickle

# Mean Absolute Error: 861519.7672479624
# The predicted price for the given house is: 4790586.666666667
# Load the data
# data = pd.read_csv('evler_analizi_model.csv')
# data['price'] /= 1000000

data = pd.read_csv('cleaned_data.csv')

# Preprocess the data
for column in data.columns:
    if data[column].dtype == type(object):
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column])

# Split the data into features and target
X = data.drop('price', axis=1)
y = data['price']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
predictions = model.predict(X_test)
print(f"Mean Absolute Error: {mean_absolute_error(y_test, predictions)}")

# Export the trained model using pickle
with open('trained_model.pkl', 'wb') as f:
    pickle.dump(model, f)

# 'Net Metrekare': 300,    int
# 'Oda Sayısı': 5.0,  float 5.0 -> 5+1 -> 5
# 'Bulunduğu Kat': 2,  int -> 2.Kat -> 2
# 'Banyo Sayısı': 1,  int
# 'Binanın Yaşı': '0 (Yeni)',  int -> 0 (Yeni) -> 0
# 'Binanın Kat Sayısı': 3,  int
# 'Site İçerisinde': 'Hayır'  int -> Hayır -> 0, Evet -> 1
# 'latitude': 40.7401164,  float
# 'longitude': 29.9581538,  float


# Test the model with the given house data
house_data = {'Net Metrekare': 130,
            'Oda Sayısı': 3.0,
            'Bulunduğu Kat': 1,
            'Banyo Sayısı': 1,
            'Binanın Yaşı':21,
            'Binanın Kat Sayısı': 3,
            'Site İçerisinde': 0,
            'latitude': 40.7401164,
            'longitude':29.9581538,
            }
house_data = pd.DataFrame(house_data, index=[0])

# Preprocess the house data
for column in house_data.columns:
    if house_data[column].dtype == type(object):
        le = LabelEncoder()
        house_data[column] = le.fit_transform(house_data[column])

# Predict the house price
predicted_price = model.predict(house_data)

# Evaluate the model
# mse = mean_squared_error(y_test, predictions)
# print(f'Mean Squared Error: {mse}')
print(f"The predicted price for the given house is: {predicted_price[0]}")


