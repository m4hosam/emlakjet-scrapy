CREATE DATABASE emlakjet;
use emlakjet;
CREATE TABLE Evler (
    IlanNumarasi VARCHAR(255),
    IlanGuncellemeTarihi VARCHAR(255),
    Kategorisi VARCHAR(255),
    NetMetrekare VARCHAR(255),
    OdaSayisi VARCHAR(255),
    BulunduguKat VARCHAR(255),
    IsitmaTipi VARCHAR(255),
    KrediyeUygunluk VARCHAR(255),
    SiteIcerisinde VARCHAR(255),
    Takas VARCHAR(255),
    FiyatDurumu VARCHAR(255),
    IlanOlusturmaTarihi VARCHAR(255),
    Turu VARCHAR(255),
    Tipi VARCHAR(255),
    BrutMetrekare VARCHAR(255),
    BinaninYasi VARCHAR(255),
    BinaninKatSayisi VARCHAR(255),
    KullanimDurumu VARCHAR(255),
    YatirimaUygunluk VARCHAR(255),
    EsyaDurumu VARCHAR(255),
    BanyoSayisi VARCHAR(255),
    Url VARCHAR(255),
    Price VARCHAR(255)
);
select * from Evler; 