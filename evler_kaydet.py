
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
    INSERT INTO Evler (IlanNumarasi, IlanGuncellemeTarihi, Kategorisi, NetMetrekare, OdaSayisi, BulunduguKat, IsitmaTipi, 
                            KrediyeUygunluk, SiteIcerisinde, Takas, FiyatDurumu, IlanOlusturmaTarihi, Turu, Tipi, BrutMetrekare, 
                            BinaninYasi, BinaninKatSayisi, KullanimDurumu, YatirimaUygunluk, EsyaDurumu, BanyoSayisi, Url, Price)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    property_values = (
        ev["İlan Numarası"], ev["İlan Güncelleme Tarihi"], ev["Kategorisi"], ev["Net Metrekare"], ev["Oda Sayısı"],
        ev["Bulunduğu Kat"], ev["Isıtma Tipi"], ev["Krediye Uygunluk"], ev["Site İçerisinde"], ev["Takas"],
        ev["Fiyat Durumu"], ev["İlan Oluşturma Tarihi"], ev["Türü"], ev["Tipi"], ev["Brüt Metrekare"],
        ev["Binanın Yaşı"], ev["Binanın Kat Sayısı"], ev["Kullanım Durumu"], ev["Yatırıma Uygunluk"], ev["Eşya Durumu"],
        ev["Banyo Sayısı"], ev["url"], ev["price"]
    )
    print(property_values)  # Print the property values to check
    
    cursor.execute(insert_query, property_values)

# Commit changes and close the database connection
db_connection.commit()
db_connection.close()
