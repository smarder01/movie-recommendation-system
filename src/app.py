import streamlit as st
import collaborative_filtering as cf
import data_preprocessing as dp

# load dataset
movies_df, ratings_df, tags_df = dp.load_data()

# clean it
movies_df, ratings_df, tags_df = dp.clean_data(movies_df, ratings_df, tags_df)

# create user-item matrix
user_item_matrix = dp.create_user_item_matrix(ratings_df, movies_df)

dp.save_preprocessed_data(user_item_matrix)

# create a dictionary to map movie IDs to titles
movie_titles = dict(zip(movies_df["movieId"], movies_df["title"]))

# Create a reverse dictionary to map movie titles to movie IDs for easy lookup
title_to_movieId = dict(zip(movies_df["title"], movies_df["movieId"]))

# Cache top movies for faster dropdown loading
@st.cache_data
def get_top_movies():
    top_movies = ratings_df["movieId"].value_counts().head(500).index.tolist()
    return sorted([movie_titles[movie_id] for movie_id in top_movies if movie_id in movie_titles])

top_movie_titles = get_top_movies()

# Streamlit UI
st.title("🍿 PopcornPicks - Movie Recommendation System")
st.write("Discover personalized movie recommendations!")

# Instructions Section
st.markdown("""
## How It Works:
1. **Enter a Movie Title** in the sidebar to receive recommendations based on that movie.
2. **Choose a Recommendation Method**:
   - **Item-Based Filtering**: Finds movies similar to your selected movie based on user ratings.
   - **SVD (Singular Value Decomposition)**: Uses matrix factorization to predict movies you might like based on hidden patterns in the rating data.
3. **Surprise Me Button**: Choose a genre (or **Any Genre**) and let us surprise you with a random movie recommendation from that genre!
4. Click **"Get Recommendations"** to see your personalized suggestions!
""")

# User Input Section
st.sidebar.header("Find Movie Recommendations")
movie_name = st.sidebar.selectbox("Select a Movie", options=[""] + movies_df["title"].tolist())

if movie_name:
    movie_id = title_to_movieId[movie_name]

# Convert selected movie name to movie ID
if movie_name and movie_name in title_to_movieId:
    movie_id = title_to_movieId[movie_name]

    # Recommendation Type Selection
    option = st.sidebar.selectbox("📌 Choose a recommendation type", ["Item-Based", "SVD"], index=0)

    # Recommendation Button
    if st.sidebar.button("🎬 Get Recommendations"):
        if option == "Item-Based":
            if movie_id not in user_item_matrix.columns:
                st.error("❌ Movie not found in the ratings dataset!")
            else:
                recommendations = cf.item_item_collab_filtering(user_item_matrix, movie_id)
        else:
            recommendations = cf.svd_recommendation(user_item_matrix, movie_id)

        # Display Recommendations with Genres and Ratings (Nicer Format)
        st.write(f"## 🎞️ Recommended Movies Based on: **{movie_name}**")
        for rec_id in recommendations:
            movie_data = movies_df[movies_df["movieId"] == rec_id].iloc[0]
            title = movie_data["title"]
            genres = movie_data["genres"]
            avg_rating = ratings_df[ratings_df["movieId"] == rec_id]["rating"].mean()
            
            # Formatting and styling
            st.markdown(f"### 🎬 **{title}**")
            st.markdown(f"**Genres:** _{genres}_")
            st.markdown(f"**Average Rating:** ⭐ {avg_rating:.2f}")
            st.markdown("---")

# Surprise Me Button and Genre Selection
st.sidebar.header("Surprise Me!")
genre_list = movies_df["genres"].unique().tolist()
genre_list = sorted([genre for genre in genre_list if genre != "(no genres listed)"])  # Exclude empty genres

# Add 'Any Genre' to the genre list
genre_list = ["Any Genre"] + genre_list

genre_choice = st.sidebar.selectbox("Select Genre", options=genre_list)

if st.sidebar.button("🎉 Surprise Me!"):
    if genre_choice == "Any Genre":
        # If "Any Genre" is selected, pick a random movie from all available movies
        random_movie = movies_df.sample(n=1)
        movie_name = random_movie["title"].values[0]
        genres = random_movie["genres"].values[0]
        avg_rating = ratings_df[ratings_df["movieId"] == random_movie["movieId"].values[0]]["rating"].mean()
        st.write(f"**Surprise Movie:** {movie_name} 🎬\n  - Genres: _{genres}_\n  - Average Rating: ⭐ {avg_rating:.2f}")
    else:
        # Filter movies based on selected genre
        filtered_movies = movies_df[movies_df["genres"].str.contains(genre_choice)]
        
        if not filtered_movies.empty:
            random_movie = filtered_movies.sample(n=1)
            movie_name = random_movie["title"].values[0]
            genres = random_movie["genres"].values[0]
            avg_rating = ratings_df[ratings_df["movieId"] == random_movie["movieId"].values[0]]["rating"].mean()
            st.write(f"**Surprise Movie:** {movie_name} 🎬\n  - Genres: _{genres}_\n  - Average Rating: ⭐ {avg_rating:.2f}")
        else:
            st.error(f"No movies found in the {genre_choice} genre.")