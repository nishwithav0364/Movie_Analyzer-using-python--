import pandas as pd
import matplotlib.pyplot as plt

top_movies = pd.read_csv("output/top_movies.csv")
genre_ratings = pd.read_csv("output/genre_ratings.csv")
most_rated = pd.read_csv("output/most_rated_movies.csv")
cleaned_data = pd.read_csv("output/cleaned_movie_data.csv")

#Bar Chart
plt.figure(figsize=(10,6))

plt.bar(top_movies["title"], top_movies["rating"])

plt.title("Top 10 Highest Rated Movies")
plt.xlabel("Movie")
plt.ylabel("Average Rating")

plt.xticks(rotation=90)

plt.tight_layout()

plt.savefig("graphs/top_movies.png")

plt.show()

#Line Chart
ratings_year = cleaned_data.groupby("year")["rating"].mean()
plt.figure(figsize=(10,6))

plt.plot(
    ratings_year.index,
    ratings_year.values,
    marker="o"
)

plt.title("Average Rating by Year")
plt.xlabel("Year")
plt.ylabel("Average Rating")

plt.grid(True)

plt.savefig("graphs/rating_by_year.png")

plt.show()

#Pie Chart
genre_data = cleaned_data.copy()

genre_data["genres"] = genre_data["genres"].str.split("|")

genre_data = genre_data.explode("genres")

genre_count = genre_data["genres"].value_counts()

plt.figure(figsize=(8,8))

plt.pie(
    genre_count.head(8),
    labels=genre_count.head(8).index,
    autopct="%1.1f%%"
)

plt.title("Genre Distribution")

plt.savefig("graphs/genre_distribution.png")

plt.show()
 

#Histogram
plt.figure(figsize=(8,6))

plt.hist(
    cleaned_data["rating"],
    bins=10
)

plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Frequency")

plt.savefig("graphs/rating_distribution.png")

plt.show()

#Scatter Plot
movie_stats = cleaned_data.groupby("title").agg(
    average_rating=("rating", "mean"),
    rating_count=("rating", "count")
)
plt.figure(figsize=(10,6))

plt.scatter(
    movie_stats["rating_count"],
    movie_stats["average_rating"]
)

plt.title("Ratings Count vs Average Rating")
plt.xlabel("Number of Ratings")
plt.ylabel("Average Rating")

plt.savefig("graphs/scatter_plot.png")

plt.show()