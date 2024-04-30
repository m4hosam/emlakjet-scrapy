import json
import csv

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
with open('evler_analizi.json', 'w', encoding='utf-8') as output_file:
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
        # You can add more preprocessing steps here based on your specific needs
        cleaned_obj[key] = value
    cleaned_data.append(cleaned_obj)

# Write the cleaned data to a CSV file
csv_file_path = 'evler_analizi_model.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=keys_to_extract_model)
    writer.writeheader()
    writer.writerows(cleaned_data)


print(f"Data saved to {csv_file_path}")