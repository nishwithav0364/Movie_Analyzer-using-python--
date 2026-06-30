import pandas as pd

# Load datasets
movies = pd.read_csv("dataset/movies.csv")
ratings = pd.read_csv("dataset/ratings.csv")

print("Datasets Loaded Successfully!")

print("Duplicate Movies:", movies.duplicated().sum())
print("Duplicate Ratings:", ratings.duplicated().sum())

movies = movies.drop_duplicates()
ratings = ratings.drop_duplicates()

print("Duplicates Removed!")

print("\nMissing Values in Movies")
print(movies.isnull().sum())

print("\nMissing Values in Ratings")
print(ratings.isnull().sum())

movies = movies.dropna()
ratings = ratings.dropna()

ratings["date"] = pd.to_datetime(
    ratings["timestamp"],
    unit="s"
)

print(ratings[["timestamp", "date"]].head())

ratings["year"] = ratings["date"].dt.year
print(ratings[["date", "year"]].head())

merged_data = pd.merge(
    ratings,
    movies,
    on="movieId"
)
print(merged_data.head())

merged_data.to_csv(
    "output/cleaned_movie_data.csv",
    index=False
)