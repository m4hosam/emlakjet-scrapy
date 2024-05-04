import pandas as pd
import json
import csv
from adres_kordinate import get_coordinates

# Open and read the JSON file
with open('evler.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Define the keys to extract
keys_to_extract = [
    "url",
    "İlan Güncelleme Tarihi",
    "İlan Oluşturma Tarihi",
    "Kategorisi",
    "Net Metrekare",
    "Oda Sayısı",
    "Bulunduğu Kat",
    "Isıtma Tipi",
    "Banyo Sayısı",
    "Tipi",
    "Brüt Metrekare",
    "Binanın Yaşı",
    "Binanın Kat Sayısı",
    "Kullanım Durumu",
    "Eşya Durumu",
    "Balkon Durumu",
    "Site İçerisinde",
    "address",
    "price"
]

keys_to_extract_model = [
    # "İlan Güncelleme Tarihi",
    "Net Metrekare",
    "Oda Sayısı",
    "Bulunduğu Kat",
    "Banyo Sayısı",
    "Binanın Yaşı",
    "Binanın Kat Sayısı",
    "Site İçerisinde",
    "address",
    "price",

]

# Extract the specified data from each object
extracted_data = []
for obj in data:
    extracted_obj = {}
    for key in keys_to_extract:
        extracted_obj[key] = obj.get(key, "bilinmiyor")
    extracted_data.append(extracted_obj)

# Write the extracted data to a new JSON file
with open('evler_benzer_ozellikler.json', 'w', encoding='utf-8') as output_file:
    json.dump(extracted_data, output_file, ensure_ascii=False, indent=2)


# Extract the specified data for model from each object
# Clean and preprocess the data
cleaned_data = []
for obj in data:
    cleaned_obj = {}
    for key in keys_to_extract_model:
        value = obj.get(key, "Unknown")
        if key == "Net Metrekare":
            # Remove non-numeric characters
            value = float(value.replace(' M2', ''))
            
        elif key == "price":
            # Remove non-numeric characters and convert to integer
            value = int(''.join(filter(str.isdigit, value)))
        elif key == "address":
            latitude, longitude = get_coordinates(value)
            cleaned_obj['latitude'] = latitude
            cleaned_obj['longitude'] = longitude
            print(value, latitude, longitude)
        # You can add more preprocessing steps here based on your specific needs
        cleaned_obj[key] = value
    cleaned_data.append(cleaned_obj)


keys_to_extract_model.append('latitude')
keys_to_extract_model.append('longitude')

# Write the cleaned data to a CSV file
csv_file_path = 'evler_benzer_ozellikler.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=keys_to_extract_model)
    writer.writeheader()
    writer.writerows(cleaned_data)




# Define a function to clean the data and convert categories into numbers
def clean_data(df):
    # Replace "Unknown" values with NaN
    df = df.replace("Unknown", float("NaN"))

    # Convert "Bulunduğu Kat" column to string
    df["Bulunduğu Kat"] = df["Bulunduğu Kat"].astype(str)

    df['Bulunduğu Kat'].replace('Unknown', '3.Kat')

    # Extract the floor number from "Bulunduğu Kat" column
    df["Bulunduğu Kat"] = df["Bulunduğu Kat"].str.extract('(\\d+)', expand=False)

    # Convert "Bulunduğu Kat" column to numeric
    df["Bulunduğu Kat"] = pd.to_numeric(df["Bulunduğu Kat"])

    # Convert "Binanın Yaşı" column to string
    df["Binanın Yaşı"] = df["Binanın Yaşı"].astype(str)

    # Extract the building age from "Binanın Yaşı" column
    df["Binanın Yaşı"] = df["Binanın Yaşı"].str.extract('(\\d+)', expand=False)

    # Convert "Binanın Yaşı" column to numeric
    df["Binanın Yaşı"] = pd.to_numeric(df["Binanın Yaşı"])

    # Convert "Site İçerisinde" column to binary
    df["Site İçerisinde"] = df["Site İçerisinde"].map({"Evet": 1, "Hayır": 0})

    # Convert "Oda Sayısı" column to string
    df["Oda Sayısı"] = df["Oda Sayısı"].astype(str)

    # Extract the number of rooms from "Oda Sayısı" column
    df["Oda Sayısı"] = df["Oda Sayısı"].str.extract('(\\d+)', expand=False)

    # Convert "Oda Sayısı" column to numeric
    df["Oda Sayısı"] = pd.to_numeric(df["Oda Sayısı"])

    # Replace "Yok" with 0 and "6+" with 6 in "Banyo Sayısı" column
    df["Banyo Sayısı"] = df["Banyo Sayısı"].replace({"Yok": 0, "6+": 6})

    # Drop addrress column
    df = df.drop("address", axis=1)

    # Fill NaN values with median of each column
    df = df.fillna(df.median())

    return df

# Load the data
data = pd.read_csv("evler_benzer_ozellikler.csv")

# Clean the data
cleaned_data = clean_data(data)

cleaned_data['price'] /= 1000000

# make price column the last column
cols = list(cleaned_data.columns)
cols.remove('price')
cols.append('price')
cleaned_data = cleaned_data[cols]

cleaned_data.to_csv('temiz_veri.csv', index=False)
print(f"Veri temizleme yapildi temiz_veri.csv")
