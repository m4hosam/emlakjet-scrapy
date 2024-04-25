# python -m venv venv
# .\venv\Scripts\activate
# source ./venv/Scripts/activate
scrapy runspider emlak_scrapy.py
python veri_analizi.py
python veri_temizleme.py
python train_model.py