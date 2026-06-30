import pandas as pd

# Load cleaned dataset
data = pd.read_csv("output/cleaned_movie_data.csv")

print("Dataset Loaded Successfully!")

print(data.head())

top_movies = (
    data.groupby("title")["rating"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
)

print("\nTop 10 Highest Rated Movies")
print(top_movies)
 
most_rated = (
    data.groupby("title")["rating"]
        .count()
        .sort_values(ascending=False)
        .head(10)
)

print("\nTop 10 Most Rated Movies")
print(most_rated)

genre_data = data.copy()

genre_data["genres"] = genre_data["genres"].str.split("|")

genre_data = genre_data.explode("genres")

avg_genre = (
    genre_data.groupby("genres")["rating"]
              .mean()
              .sort_values(ascending=False)
)

print("\nAverage Rating by Genre")
print(avg_genre)

genre_count = (
    genre_data.groupby("genres")["title"]
              .count()
              .sort_values(ascending=False)
)

print("\nMovies in Each Genre")
print(genre_count)

ratings_year = (
    data.groupby("year")["rating"]
        .mean()
)

print("\nAverage Rating by Year")
print(ratings_year)

print("\nTop 5 Genres")

print(avg_genre.head())

top_movies.to_csv("output/top_movies.csv")
avg_genre.to_csv("output/genre_ratings.csv")
most_rated.to_csv("output/most_rated_movies.csv")