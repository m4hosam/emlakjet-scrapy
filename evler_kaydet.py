
# python evler_kaydet.py 

import mysql.connector
import json

# Connect to MySQL database
db_connection = mysql.connector.connect(
    host='localhost',
    user='admin',
    password='password',
    database='emlakjet'
)
{
    "url": "https://www.emlakjet.com/ilan/attichouse-tan-panoromik-manzarali-satilik-31-dubleks-14820820/",
    "İlan Güncelleme Tarihi": "08 Mart 2024",
    "İlan Oluşturma Tarihi": "08 Mart 2024",
    "Kategorisi": "Satılık",
    "Net Metrekare": "138 M2",
    "Oda Sayısı": "3+1",
    "Bulunduğu Kat": "Çatı Dubleks",
    "Isıtma Tipi": "Yerden Isıtma",
    "Banyo Sayısı": "3",
    "Tipi": "Daire",
    "Brüt Metrekare": "165 M2",
    "Binanın Yaşı": "0 (Yeni)",
    "Binanın Kat Sayısı": "3",
    "Kullanım Durumu": "Boş",
    "Eşya Durumu": "Boş",
    "Balkon Durumu": "Var",
    "Site İçerisinde": "Evet",
    "price": "4,990,000"
  }
# Create a cursor object to interact with the database
cursor = db_connection.cursor()

# Open the JSON file and load data
with open("evler.json", "r", encoding="utf-8") as file:
    evler = json.load(file)

# Define a function to check if a property is missing and set its value to "bilinmiyor"
def check_missing_property(property_value):
    return property_value if property_value else "bilinmiyor"

for ev in evler:
    # Check and update missing properties
    ev["Krediye Uygunluk"] = check_missing_property(ev.get("Krediye Uygunluk"))
    ev["Site İçerisinde"] = check_missing_property(ev.get("Site İçerisinde"))
    ev["Takas"] = check_missing_property(ev.get("Takas"))
    ev["Yatırıma Uygunluk"] = check_missing_property(ev.get("Yatırıma Uygunluk"))
    ev["Eşya Durumu"] = check_missing_property(ev.get("Eşya Durumu"))
    # Assuming all other properties can't be missing, adjust this line if needed
    
    # Print the current object to check its values
    print(ev)
    
    # Insert the object into the database
    insert_query = """
    INSERT INTO RealEstateListing (
        Ilan_Numarasi, 
        Ilan_Guncelleme_Tarihi, 
        Kategorisi, 
        Net_Metrekare, 
        Oda_Sayisi, 
        Bulundugu_Kat, 
        Isitma_Tipi, 
        Krediye_Uygunluk, 
        Banyo_Sayisi, 
        Ilan_Olusturma_Tarihi, 
        Turu, 
        Tipi, 
        Brut_Metrekare, 
        Binanin_Yasi, 
        Binanin_Kat_Sayisi, 
        Kullanim_Durumu, 
        Site_Icerisinde, 
        Fiyat_Durumu, 
        url, 
        price
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    property_values = (
        ev["İlan Numarası"],
        ev["İlan Güncelleme Tarihi"],
        ev["Kategorisi"],
        ev["Net Metrekare"],
        ev["Oda Sayısı"],
        ev["Bulunduğu Kat"],
        ev["Isıtma Tipi"],
        ev["Krediye Uygunluk"],
        int(ev["Banyo Sayısı"]),
        ev["İlan Oluşturma Tarihi"],
        ev["Türü"],
        ev["Tipi"],
        ev["Brüt Metrekare"],
        ev["Binanın Yaşı"],
        int(ev["Binanın Kat Sayısı"]),
        ev["Kullanım Durumu"],
        ev["Site İçerisinde"],
        ev["Fiyat Durumu"],
        ev["url"],
        float(ev["price"].replace(',', ''))  # Removing commas from price and converting to float
    )
    # print(property_values)  # Print the property values to check
    
    cursor.execute(insert_query, property_values)

# Commit changes and close the database connection
db_connection.commit()
db_connection.close()
