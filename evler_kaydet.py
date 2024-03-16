import mysql.connector
import json

# Connect to MySQL database
db_connection = mysql.connector.connect(
    host='localhost',
    user='admin',
    password='password',
    database='emlakjet'
)

# Create a cursor object to interact with the database
cursor = db_connection.cursor()

# Open the JSON file and load data
with open("extracted_data.json", "r", encoding="utf-8") as file:
    extracted_data = json.load(file)

# Iterate through each object in the JSON array and insert into the database
for data in extracted_data:
    query = """
    INSERT INTO Evler (
        url,
        Ilan_Guncelleme_Tarihi,
        Ilan_Olusturma_Tarihi,
        Kategorisi,
        Net_Metrekare,
        Oda_Sayisi,
        Bulundugu_Kat,
        Isitma_Tipi,
        Banyo_Sayisi,
        Tipi,
        Brut_Metrekare,
        Binanin_Yasi,
        Binanin_Kat_Sayisi,
        Kullanim_Durumu,
        Eşya_Durumu,
        Balkon_Durumu,
        Site_Icerisinde,
        price
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        data["url"],
        data["İlan Güncelleme Tarihi"],
        data["İlan Oluşturma Tarihi"],
        data["Kategorisi"],
        data["Net Metrekare"],
        data["Oda Sayısı"],
        data["Bulunduğu Kat"],
        data["Isıtma Tipi"],
        data["Banyo Sayısı"],
        data["Tipi"],
        data["Brüt Metrekare"],
        data["Binanın Yaşı"],
        data["Binanın Kat Sayısı"],
        data["Kullanım Durumu"],
        data["Eşya Durumu"],
        data["Balkon Durumu"],
        data["Site İçerisinde"],
        data["price"]
    )

    cursor.execute(query, values)

# Commit changes and close connections
db_connection.commit()
cursor.close()
db_connection.close()
