# PopcornPicks  

A simple **Movie Recommendation System** built using Collaborative Filtering and Matrix Factorization (SVD). This project demonstrates the use of user-based & item-based filtering to provide personalized movie recommendations.  

![Python](https://img.shields.io/badge/Python-3.8+-blue)  
![License](https://img.shields.io/badge/License-MIT-green)  

---

## Features  
- **User-Based Collaborative Filtering** – Recommends movies based on similar users.  
- **Item-Based Collaborative Filtering** – Recommends movies similar to a given movie.  
- **Matrix Factorization (SVD)** – Uses dimensionality reduction to predict ratings.  
- **Evaluation with RMSE** – Measures model accuracy.  
- **Command-Line Interface** – Users can input a movie or user ID to get recommendations.  

---

## Dataset: MovieLens 100K  
This project uses the **MovieLens 100K dataset** provided by [GroupLens](https://grouplens.org/datasets/movielens/100k/). It contains **100,000 ratings** from **943 users** on **1,682 movies**, with ratings ranging from **1 to 5 stars**.  

### Dataset Files & Structure  
After extraction, the dataset files are located in the `ml-100k/` directory:  

| File           | Description |
|---------------|------------|
| `movies.csv`  | Contains **movieId**, **title**, and **genres**. |
| `ratings.csv` | Contains **userId**, **movieId**, **rating**, and **timestamp** for **100,000 ratings**. |
| `tags.csv`    | Contains user-generated **tags** for movies (e.g., "Action", "Drama"). |
| `README`      | Dataset information provided by GroupLens. |

---

## Project Structure  
```plaintext
movie-recommendation-system/
│
├── data/                           # Folder where the MovieLens dataset will be placed
│   ├── ml-latest-small/            # Unzipped dataset folder
│   │   ├── movies.csv              # Movie details (title, genres)
│   │   ├── ratings.csv             # Ratings data (userId, movieId, rating, timestamp)
│   │   ├── tags.csv       	    # User-generated tags
│   │   ├── README.txt     	    # Dataset info         
│
├── src/                   	    # Source code for the recommendation system
│   ├── recommend.py       	    # Main script to generate movie recommendations
│   ├── data_preprocessing.py 	    # Preprocessing script (loading, cleaning data)
│   ├── collaborative_filtering.py  # User/Item-based CF implementations
│   ├── svd_model.py       	    # SVD matrix factorization implementation
│   └── evaluation.py               # RMSE evaluation and results
│
├── requirements.txt                # Required Python libraries
├── README.md              	    # Project details and instructions (this file)
└── LICENSE                	    # MIT License
```

---

## Future Enhancements
- Hybrid Model – Combine collaborative and content-based filtering.
- Deep Learning – Use Autoencoders or Transformers for better recommendations.
- Web Interface – Deploy a Streamlit app for a better user experience.
- API Deployment – Use Flask/FastAPI for REST API integration.

___

## Installation & Setup
1. Clone the Repository
  git clone https://github.com/your-username/movie-recommendation-system.git  
  cd movie-recommendation-system
2. Install Dependencies
  Ensure you have Python 3.8+ installed. Then, run:
  pip install -r requirements.txt
3. Run the Reccomendation System
  python recommend.py
4. Then, enter a movie name or user ID to recieve recommendations.

### Example Usage (Command-Line Interface)
$ python recommend.py  
Enter a movie name: Inception  
Recommended movies: Interstellar, The Dark Knight, Memento  

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

## 📖 Citation  

F. Maxwell Harper and Joseph A. Konstan. 2015. The MovieLens Datasets: History and Context. ACM Transactions on Interactive Intelligent Systems (TiiS) 5, 4: 19:1–19:19. <https://doi.org/10.1145/2827872>
