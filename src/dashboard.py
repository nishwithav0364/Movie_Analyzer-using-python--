import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#css
def load_css():

    with open("assets/style.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

st.success(
    "Welcome! Use the sidebar to explore charts, search movies and get recommendations."
)
# Page Configuration


st.set_page_config(
    page_title="Movie Ratings Dashboard",
    page_icon="🎬",
    layout="wide"
)


# Load Dataset


data = pd.read_csv("output/cleaned_movie_data.csv")


# Sidebar Logo


st.sidebar.image(
    "assets/logo.png",
    width=130
)

st.sidebar.title("Movie Dashboard")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📊 Charts",
        "⭐ Recommendation",
        "ℹ️ About"
    ]
)

st.sidebar.markdown("---")


# Filters


movie_search = st.sidebar.text_input(
    "🔍 Search Movie"
)

genres = sorted(data["genres"].unique())

selected_genre = st.sidebar.selectbox(
    "🎭 Select Genre",
    ["All"] + genres
)

year = st.sidebar.slider(
    "📅 Select Year",
    int(data["year"].min()),
    int(data["year"].max()),
    int(data["year"].max())
)


# Apply Filters


filtered = data.copy()

if movie_search:
    filtered = filtered[
        filtered["title"].str.contains(
            movie_search,
            case=False
        )
    ]

if selected_genre != "All":
    filtered = filtered[
        filtered["genres"] == selected_genre
    ]

filtered = filtered[
    filtered["year"] == year
]


# HOME PAGE


if page == "🏠 Home":

    st.image(
        "assets/banner.png",
        use_container_width=True
    )

    st.title("🎬 Movie Ratings Dashboard")

    st.markdown("Discover insights from thousands of movie ratings through interactive analysis and visualizations.")

    total_movies = data["title"].nunique()

    total_users = data["userId"].nunique()

    total_ratings = len(data)

    average_rating = round(
        data["rating"].mean(),
        2
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "🎬 Movies",
        total_movies
    )

    col2.metric(
        "👤 Users",
        total_users
    )

    col3.metric(
        "⭐ Ratings",
        total_ratings
    )

    col4.metric(
        "⭐ Avg Rating",
        average_rating
    )

    st.markdown("---")

    
    st.subheader("📊 Dashboard Overview")

    st.dataframe(
        filtered,
        use_container_width=True
    )

    st.info(
        f"Showing {len(filtered)} matching records."
    )


# Placeholder Pages


elif page == "📊 Charts":

    st.title("📊 Movie Analytics")

    chart = st.selectbox(
        "Select Chart",
        (
            "Top 10 Highest Rated Movies",
            "Top 10 Most Rated Movies",
            "Average Rating by Year",
            "Genre Distribution",
            "Rating Distribution",
            "Popularity vs Rating"
        )
    )

    # Chart 1
   

    if chart == "Top 10 Highest Rated Movies":

        top_movies = (
            data.groupby("title")["rating"]
            .mean()
            .sort_values(ascending=False)
            .head(10)
        )

        fig, ax = plt.subplots(figsize=(10,6))

        ax.barh(
            top_movies.index,
            top_movies.values
        )

        ax.set_title("Top 10 Highest Rated Movies")
        ax.set_xlabel("Average Rating")

        st.pyplot(fig)

    
    # Chart 2


    elif chart == "Top 10 Most Rated Movies":

        most_rated = (
            data.groupby("title")["rating"]
            .count()
            .sort_values(ascending=False)
            .head(10)
        )

        fig, ax = plt.subplots(figsize=(10,6))

        ax.barh(
            most_rated.index,
            most_rated.values
        )

        ax.set_title("Top 10 Most Rated Movies")
        ax.set_xlabel("Number of Ratings")

        st.pyplot(fig)

    
    # Chart 3
    

    elif chart == "Average Rating by Year":

        ratings_year = (
            data.groupby("year")["rating"]
            .mean()
        )

        fig, ax = plt.subplots(figsize=(10,6))

        ax.plot(
            ratings_year.index,
            ratings_year.values,
            marker="o"
        )

        ax.set_title("Average Rating by Year")

        ax.set_xlabel("Year")

        ax.set_ylabel("Average Rating")

        ax.grid(True)

        st.pyplot(fig)

   
    # Chart 4
   
    elif chart == "Genre Distribution":

        genre_data = data.copy()

        genre_data["genres"] = genre_data["genres"].str.split("|")

        genre_data = genre_data.explode("genres")

        genre_count = genre_data["genres"].value_counts()

        fig, ax = plt.subplots(figsize=(8,8))

        ax.pie(
            genre_count.head(8),
            labels=genre_count.head(8).index,
            autopct="%1.1f%%"
        )

        ax.set_title("Top Genres")

        st.pyplot(fig)

    # Chart 5
   

    elif chart == "Rating Distribution":

        fig, ax = plt.subplots(figsize=(10,6))

        ax.hist(
            data["rating"],
            bins=10
        )

        ax.set_title("Rating Distribution")

        ax.set_xlabel("Rating")

        ax.set_ylabel("Frequency")

        st.pyplot(fig)

  
    # Chart 6
   

    elif chart == "Popularity vs Rating":

        movie_stats = (
            data.groupby("title")
            .agg(
                average_rating=("rating","mean"),
                rating_count=("rating","count")
            )
        )

        fig, ax = plt.subplots(figsize=(10,6))

        ax.scatter(
            movie_stats["rating_count"],
            movie_stats["average_rating"]
        )

        ax.set_title("Popularity vs Average Rating")

        ax.set_xlabel("Number of Ratings")

        ax.set_ylabel("Average Rating")

        st.pyplot(fig)

elif page == "⭐ Recommendation":

    st.title("⭐ Movie Recommendation System")

    st.write(
        "Select a movie to discover other highly rated movies from similar genres."
    )

    st.markdown("---")

    # Movie Selection

    movie = st.selectbox(
        "🎬 Select a Movie",
        sorted(data["title"].unique())
    )

    selected_movie = data[
        data["title"] == movie
    ]

    genre = selected_movie["genres"].iloc[0]

    average_rating = round(
        selected_movie["rating"].mean(),
        2
    )

    total_ratings = selected_movie["rating"].count()

    # Movie Details

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Genre",
        genre
    )

    col2.metric(
        "Average Rating",
        average_rating
    )

    col3.metric(
        "Total Ratings",
        total_ratings
    )

    st.markdown("---")

    st.subheader("Recommended Movies")

    recommendation = (

        data[
            (data["genres"] == genre) &
            (data["title"] != movie)
        ]

        .groupby("title")

        .agg(
            Average_Rating=("rating","mean"),
            Ratings=("rating","count")
        )

        .sort_values(
            by=["Average_Rating","Ratings"],
            ascending=False
        )

        .head(10)

        .reset_index()

    )

    if len(recommendation) > 0:

        st.dataframe(
            recommendation,
            use_container_width=True
        )

    else:

        st.warning(
            "No similar movies found."
        )

elif page == "ℹ️ About":

    st.title("ℹ️ About")

    st.write("""
This dashboard analyzes movie ratings using the MovieLens dataset.

### Technologies Used

- Python
- Pandas
- Matplotlib
- Streamlit

### Features

- Search movies
- Filter by genre
- Filter by year
- Interactive charts
- Movie recommendations
""")