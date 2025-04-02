# PopcornPicks  

A **Movie Recommendation System** built using Collaborative Filtering and Matrix Factorization (SVD). This project provides personalized movie recommendations using **item-based filtering**, **SVD-based filtering**, and a **"Surprise Me" feature** for movie discovery. The system is deployed as an interactive **Streamlit app**.  

![Python](https://img.shields.io/badge/Python-3.8+-blue)  
![License](https://img.shields.io/badge/License-MIT-green)  

---

## ✨ Features  
- **Item-Based Collaborative Filtering** – Recommends movies similar to a selected movie based on user preferences.  
- **SVD (Singular Value Decomposition)** – Uses matrix factorization to predict movies you might enjoy.  
- **"Surprise Me" Feature** – Pick a random movie from any genre or a specific genre.  
- **Streamlit Web App** – A user-friendly UI for discovering new movies.  
- **Movie Details** – Recommendations include genres and average ratings for better decision-making.  

---

## Dataset: MovieLens 100K  
This project uses the **MovieLens 100K dataset** from [GroupLens](https://grouplens.org/datasets/movielens/100k/). It contains:  
- **100,000 ratings** from **943 users**  
- **1,682 movies** with **genre labels**  
- Ratings range from **1 to 5 stars**  

---

### Dataset Files & Structure  
| File           | Description |
|---------------|------------|
| `movies.csv`  | Movie metadata (ID, title, genres). |
| `ratings.csv` | User-movie ratings (userId, movieId, rating). |
| `tags.csv`    | User-generated tags (e.g., "Action", "Drama"). |
| `README`      | Dataset information. |

---

## Project Structure  
```plaintext
movie-recommendation-system/
│
├── data/                           # Folder where the dataset is stored
│   ├── ml-latest-small/            # Unzipped dataset folder
│   │   ├── movies.csv              # Movie details (title, genres)
│   │   ├── ratings.csv             # Ratings data (userId, movieId, rating, timestamp)
│   │   ├── tags.csv                # User-generated tags
│   │   ├── README.txt              # Dataset info         
│
├── src/                            # Source code for the recommendation system
│   ├── app.py                      # Streamlit App script
│   ├── data_preprocessing.py        # Preprocessing script (loading, cleaning data)
│   ├── collaborative_filtering.py   # Item-based CF implementation
│   ├── evaluation.py                # Evaluation metrics (RMSE, MAE)
│
├── requirements.txt                 # Required Python libraries
├── README.md                        # Project details and instructions (this file)
└── LICENSE                          # MIT License
```

---

## Future Enhancements
- Hybrid Model – Combine collaborative and content-based filtering for improved accuracy.
- Deep Learning – Implement neural networks (Autoencoders, Transformers) for enhanced recommendations.
- API Deployment – Serve recommendations via a REST API using Flask/FastAPI.
- Movie Posters & Trailers – Integrate metadata for a richer user experience.

___

## Installation & Setup
1. Clone the Repository:
    git clone https://github.com/smarder01/movie-recommendation-system.git
    cd movie-recommendation-system
2. Install Dependencies:
    pip install -r requirements.txt
3. Run the Streamlit App:
    streamlit run src/app.py

### Example Usage (Streamlit App)
	1.	Select a movie from the dropdown menu.
	2.	Choose a recommendation method (Item-Based or SVD).
	3.	Click “Get Recommendations” to see personalized suggestions.
	4.	Try the “Surprise Me” button for random movie suggestions!

---

## Contributing
Contributions are welcome! If you'd like to contribute
	1.	Fork the repository
	2.	Create a feature branch (git checkout -b feature-name)
	3.	Commit your changes (git commit -m "Added a new feature")
	4.	Push to your branch (git push origin feature-name)
	5.	Submit a pull request

This project is open-source and licensed under the MIT License.

---

## Citation  

F. Maxwell Harper and Joseph A. Konstan. 2015. The MovieLens Datasets: History and Context. ACM Transactions on Interactive Intelligent Systems (TiiS) 5, 4: 19:1–19:19. <https://doi.org/10.1145/2827872>
