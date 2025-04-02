import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import TruncatedSVD

# Helper function to compute cosine similarity
def calculate_cosine_similarity(matrix):
    return cosine_similarity(matrix.fillna(0))

# User-User Collaborative Filtering
def user_user_collab_filtering(user_item_matrix, target_user_id, top_n_neighbors=5):
    similarity_matrix = calculate_cosine_similarity(user_item_matrix)

    # Find target user index
    target_user_index = user_item_matrix.index.get_loc(target_user_id)
    
    # Get similarity scores and exclude self
    user_similarities = similarity_matrix[target_user_index]
    similar_users = user_similarities.argsort()[-(top_n_neighbors+1):-1][::-1]  

    recommendations = {}
    for user in similar_users:
        similar_user_id = user_item_matrix.index[user]
        similar_user_ratings = user_item_matrix.loc[similar_user_id]

        for movie_id, rating in similar_user_ratings.items():
            if pd.isnull(user_item_matrix.loc[target_user_id, movie_id]):  # Only recommend unseen movies
                recommendations[movie_id] = recommendations.get(movie_id, 0) + rating

    return sorted(recommendations, key=recommendations.get, reverse=True)[:top_n_neighbors]

# Item-Item Collaborative Filtering
from sklearn.metrics.pairwise import cosine_similarity

def item_item_collab_filtering(user_item_matrix, movie_id):
    # Ensure movie_id is in the matrix columns
    if movie_id not in user_item_matrix.columns:
        raise ValueError(f"Movie ID {movie_id} not found in the user-item matrix")

    # Transpose the matrix so movies become rows, users are columns
    movie_item_matrix = user_item_matrix.T

    # Calculate cosine similarity between the selected movie and all other movies
    similarity_matrix = cosine_similarity(movie_item_matrix.fillna(0))

    # Create a mapping of movie index to movie ID
    movie_indices = {movie_id: idx for idx, movie_id in enumerate(user_item_matrix.columns)}

    # Get the index of the selected movie
    selected_movie_idx = movie_indices[movie_id]

    # Get similarities of the selected movie with all other movies
    movie_similarities = similarity_matrix[selected_movie_idx]

    # Get indices of the most similar movies (excluding the selected movie itself)
    similar_movie_indices = movie_similarities.argsort()[-6:-1][::-1]  # Top 5 similar movies

    # Get movie IDs for the most similar movies
    similar_movie_ids = [user_item_matrix.columns[i] for i in similar_movie_indices]

    return similar_movie_ids

# Matrix Factorization (SVD)
def svd_recommendation(user_item_matrix, movie_id, n_components=20):
    # Ensure movie_id is in the columns of the user-item matrix
    if movie_id not in user_item_matrix.columns:
        raise ValueError(f"Movie ID {movie_id} not found in the user-item matrix")
    
    # Perform SVD on the user-item matrix
    svd = TruncatedSVD(n_components=n_components)
    matrix_svd = svd.fit_transform(user_item_matrix.fillna(0))  # Handle missing values by filling with 0
    
    # Get the index of the selected movie (column in the user-item matrix)
    movie_idx = user_item_matrix.columns.get_loc(movie_id)
    
    # Get the latent features of the selected movie (from the SVD matrix, column corresponding to movie_idx)
    movie_latent_features = svd.components_[:, movie_idx]  # This will get the correct movie's latent features
    
    # Compute the similarity between the selected movie and all other movies (dot product)
    similarity_scores = np.dot(svd.components_.T, movie_latent_features)
    
    # Sort the movies based on similarity (ignoring the selected movie itself)
    similar_movie_indices = similarity_scores.argsort()[-6:-1][::-1]  # Top 5 similar movies
    
    # Get movie IDs for the most similar movies
    similar_movie_ids = [user_item_matrix.columns[i] for i in similar_movie_indices]
    
    return similar_movie_ids