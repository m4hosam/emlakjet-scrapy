import pandas as pd

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

    # Fill NaN values with median of each column
    df = df.fillna(df.median())

    return df

# Load the data
data = pd.read_csv("evler_analizi_model.csv")

# Clean the data
cleaned_data = clean_data(data)

cleaned_data['price'] /= 1000000

cleaned_data.to_csv('cleaned_data.csv', index=False)
# cleaned_data[:10]
data = cleaned_data