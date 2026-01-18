#  Movie Recommender System (Content-Based)

A **Content-Based Movie Recommendation System** that suggests movies by analyzing their “content DNA” — **genres, keywords, cast, and director**.  
Unlike collaborative filtering (which depends on other users’ ratings), this model recommends movies that are **most similar to your selected movie** based on its metadata.

---

##  Key Features

-  Content-based recommendations using **Bag of Words**
-  Similarity search using **Cosine Similarity**
-  Clean UI using **HTML/CSS + Jinja2 templates**
-  Real-time posters fetched via **TMDB API**
-  Backend powered by **FastAPI**

---

## Tech Stack

- **Language:** Python  
- **Data Analysis:** Pandas, NumPy  
- **Machine Learning:** Scikit-learn (`CountVectorizer`, `cosine_similarity`)  
- **NLP:** NLTK (`PorterStemmer`)  
- **Backend:** FastAPI  
- **Frontend:** HTML/CSS + Jinja2 Templates  
- **API:** TMDB API (poster fetching)

---

##  How It Works

### 1) Data Preprocessing
This model is trained using the **TMDB 5000 Movie Dataset**.

**Steps:**
- **Merging:** Combine `movies` and `credits` datasets (on movie title)
- **Cleaning:** Extract important metadata from JSON-like fields
  - genres
  - keywords
  - top cast (lead actors)
  - director
- **Entity Resolution:** Remove spaces in names to keep tags unique  
  Example: `Sam Worthington → SamWorthington`

---

### 2) Vectorization Engine (Bag of Words)
To compare movies mathematically, the system converts text metadata into vectors.

**Pipeline:**
- **Tag creation:** Combine genres + keywords + cast + director into a single “tags” field
- **Stemming:** Reduce words to root form  
  Example: `action`, `actions` → `action`
- **CountVectorizer:**
  - Builds a sparse matrix of the **top 5,000 most frequent words**
- **Cosine Similarity:**
  - Computes similarity between movies using vector angles  
  - Smaller angle → more similar movies

---

### 3) FastAPI Deployment
The backend serves recommendations via FastAPI with two main routes:

- `GET /`  
  Serves the homepage with a movie dropdown.

- `POST /recommend`  
  Accepts a selected movie → returns **Top 5 recommendations** + posters fetched from TMDB.

---

##  Install Dependencies
```bash
pip install fastapi uvicorn pandas scikit-learn nltk requests
```

##  Installation & Setup

### 1) Clone the Repository
```bash
git clone https://github.com/mutassimalzeem/movie-recommendation-system.git
cd movie-recommendation-system
```

###  Generate the Model Files

Run the Jupyter Notebook to generate:

movie_list.pkl

similarity.pkl

- Make sure both files are placed in the root directory.

### Set Up TMDB API Key

Create an account on The Movie Database (TMDB)

Generate an API key

Paste the key inside the fetch_poster() function in app.py


Run the App
```bash
uvicorn app2:app --reload
```

Open in your browser:

http://127.0.0.1:8000

Future Improvements

🔍 Add a search bar with auto-complete

⭐ Add user ratings for a Hybrid Recommendation System

🐳 Dockerize and deploy the app using Docker

📌 Disclaimer

This project was built as part of a learning journey guided by the CampusX Machine Learning series.
