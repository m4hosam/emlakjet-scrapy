# Petlebi Scrapy Spider Documentation

### Overview

This Scrapy spider named `PetlebiSpider` is designed to crawl the website [petlebi.com](https://petlebi.com) and extract information about various products. The spider starts from the main page and follows links to individual product pages to collect details.

### How to Run

You need to install scrapy, sql-connector

```console
pip install scrapy mysql-connector-python
```

To execute the spider, use the following command:

```console
scrapy runspider emlak_scrapy.py
```

### Save Products to SQL

To save the scrapped products to SQL server you need to the SQL command lines in `petlebi_create.sql` to create the database and the table.
<br>
To Save the products from json file into the SQL you need to run `import_products.py`

```console
python evler_kaydet.py
```

Make sure to add the user and password correctly for your sql connection.

### Execution and Output

- Upon executing the spider, it will start crawling the website, following links to product pages, and extracting information.
- Once the crawling process is complete, the spider will save the collected data to a JSON file named `petlebi_products.json`.
