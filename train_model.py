import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


# Mean Absolute Error: 861519.7672479624
# The predicted price for the given house is: 4790586.666666667
# Load the data
data = pd.read_csv('evler_analizi_model.csv')

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

# Test the model with the given house data
house_data = {'Net Metrekare': 150, 'Oda Sayısı': '3+2', 'Bulunduğu Kat': '3.Kat', 'Banyo Sayısı': 1, 'Binanın Yaşı': '0 (Yeni)', 'Binanın Kat Sayısı': 3, 'Site İçerisinde': 'Hayır'}
house_data = pd.DataFrame(house_data, index=[0])

# Preprocess the house data
for column in house_data.columns:
    if house_data[column].dtype == type(object):
        le = LabelEncoder()
        house_data[column] = le.fit_transform(house_data[column])

# Predict the house price
predicted_price = model.predict(house_data)
print(f"The predicted price for the given house is: {predicted_price[0]}")
