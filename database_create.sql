CREATE DATABASE emlakjet;
use emlakjet;

CREATE TABLE  Evler(
	id INT AUTO_INCREMENT PRIMARY KEY,
    url VARCHAR(255),
    Ilan_Guncelleme_Tarihi VARCHAR(50),
    Ilan_Olusturma_Tarihi VARCHAR(50),
    Kategorisi VARCHAR(50),
    Net_Metrekare VARCHAR(50),
    Oda_Sayisi VARCHAR(50),
    Bulundugu_Kat VARCHAR(50),
    Isitma_Tipi VARCHAR(50),
    Banyo_Sayisi  VARCHAR(50),
    Tipi VARCHAR(50),
    Brut_Metrekare VARCHAR(50),
    Binanin_Yasi VARCHAR(50),
    Binanin_Kat_Sayisi  VARCHAR(50),
    Kullanim_Durumu VARCHAR(50),
    Eşya_Durumu VARCHAR(50),
    Balkon_Durumu VARCHAR(50),
    Site_Icerisinde VARCHAR(50),
    price VARCHAR(50)
);

select * from Evler; 

DROP table Evler;