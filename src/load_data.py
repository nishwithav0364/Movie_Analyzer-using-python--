import pandas as pd

# Load datasets
movies = pd.read_csv("dataset/movies.csv")
ratings = pd.read_csv("dataset/ratings.csv")

# Display first 5 rows
print("Movies Dataset")
print(movies.head())

print("\nRatings Dataset")
print(ratings.head())

print("\nMovies Shape")
print(movies.shape)

print("\nRatings Shape")
print(ratings.shape)

print("\nMovies Columns")
print(movies.columns)

print("\nRatings Columns")
print(ratings.columns)

print("\nMissing Values in Movies")
print(movies.isnull().sum())

print("\nMissing Values in Ratings")
print(ratings.isnull().sum())

print("\nMovies Information")
movies.info()

print("\nRatings Information")
ratings.info()

print("\nRatings Statistics")
print(ratings.describe())
