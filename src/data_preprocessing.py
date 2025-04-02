import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re

def load_data():
    # load the datasets (movies, ratings, and tags)
    movies_df = pd.read_csv('data/ml-latest-small/movies.csv')
    ratings_df = pd.read_csv('data/ml-latest-small/ratings.csv')
    tags_df = pd.read_csv('data/ml-latest-small/tags.csv')

    return movies_df, ratings_df, tags_df

def clean_data(movies_df, ratings_df, tags_df):
    # clean data by checking for missing values and duplicates
    
    # drop duplicates
    movies_df.drop_duplicates(inplace = True)
    movies_df.drop_duplicates(inplace = True)
    movies_df.drop_duplicates(inplace = True)

    # check for missing values in each dataframe
    print(f"Missing values in movies: {movies_df.isnull().sum()}")
    print(f"Missing values in ratings: {ratings_df.isnull().sum()}")
    print(f"Missing values in tags: {tags_df.isnull().sum()}")

    # remove rowns with missing values in ratings and movies
    movies_df.dropna(subset=['movieId', 'title', 'genres'], inplace=True)
    ratings_df.dropna(subset = ['userId', 'movieId', 'rating'], inplace = True)

    # ensure the correct data types
    ratings_df["rating"] = ratings_df["rating"].astype(float)

    # Remove the year from movie titles using regex
    movies_df["title"] = movies_df["title"].apply(lambda x: re.sub(r'\(.*\)', '', x).strip())

    return movies_df, ratings_df, tags_df

def visualize_data(ratings_df):
    # visualize key data distributions:
    # rating distribution and number of ratings per movie/user

    # distribution of rattings
    sns.histplot(ratings_df["rating"], bins = 5, kde = True)
    plt.title("Rating Distribution")
    plt.xlabel("Rating")
    plt.ylabel("Count")
    plt.show()

    # plot the number of ratings per movie
    movie_ratings_counts = ratings_df.groupby("movieId").size()
    sns.histplot(movie_ratings_counts, bins = 50, kde = False)
    plt.title("Number of Ratings Per Movie")
    plt.xlabel("Number of Ratings")
    plt.ylabel("Count")
    plt.show()

    # plot the number of ratings per user
    user_ratings_counts = ratings_df.groupby("userId").size()
    sns.histplot(user_ratings_counts, bins = 50, kde = False)
    plt.title("Number of Ratings Per User")
    plt.xlabel("Number of Ratings")
    plt.ylabel("Count")
    plt.show()

def create_user_item_matrix(ratings_df, movies_df):
    # create a user-item matrix from ratings data

    # merge ratings with movie titles to associate movie titles with ratings
    merged_df = pd.merge(ratings_df, movies_df[["movieId", "title"]], on = "movieId", how = "left")

    # Create the user-item matrix where rows are users, columns are movieIds, and values are ratings
    user_item_matrix = merged_df.pivot_table(index='userId', columns='movieId', values='rating')
    
    # Fill missing values (NaN) with 0 (indicating that the user hasn't rated the movie)
    user_item_matrix = user_item_matrix.fillna(0)
    
    return user_item_matrix

def save_preprocessed_data(user_item_matrix):
    # save preprocessed user-item matrix to a CSV file for future use
    user_item_matrix.to_csv("data/user_item_matrix.csv")
    print("Preprocessed user-item matrix saved to 'data/user_item_matrix.csv'.")

def main():

    # load datasets
    movies_df, ratings_df, tags_df = load_data()

    # clean data
    movies_df, ratings_df, tags_df = clean_data(movies_df, ratings_df, tags_df)

    # visualize data
    visualize_data(ratings_df)

    # create_user_matrix
    user_item_matrix = create_user_item_matrix(ratings_df, movies_df)

    # save preprocessed data
    save_preprocessed_data(user_item_matrix)

if __name__ == "__main__":
    main()