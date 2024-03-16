import json

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
    "price"
]

# Extract the specified data from each object
extracted_data = []
for obj in data:
    extracted_obj = {}
    for key in keys_to_extract:
        extracted_obj[key] = obj.get(key, "bilinmiyor")
    extracted_data.append(extracted_obj)

# Write the extracted data to a new JSON file
with open('extracted_data.json', 'w', encoding='utf-8') as output_file:
    json.dump(extracted_data, output_file, ensure_ascii=False, indent=2)
