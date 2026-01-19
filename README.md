#  Movie Recommendation System (Content-Based)

This is a full-stack, **content-based movie recommendation engine.** It suggests movies similar to a user's choice by analyzing metadata such as genres, keywords, cast, and directors. While originally inspired by the CampusX Streamlit project, this version has been upgraded to a **decoupled FastAPI architecture** for better performance and scalability.

<img width="1416" height="614" alt="image" src="https://github.com/user-attachments/assets/9e227d97-5d2f-407f-bd76-ad8e7ffeece8" />


##  Key Features

-  Content-based recommendations using **Bag of Words**
-  Similarity search using **Cosine Similarity**
-  Clean UI using **HTML/CSS + Jinja2 templates**
-  Real-time posters fetched via **TMDB API**
-  Backend powered by **FastAPI**

##  New Upgrades

-  Decoupled Architecture: Separation of a high-performance Python backend (FastAPI) and a dynamic frontend (HTML/JS).
-  Autocomplete Search: Real-time title suggestions as you type, reducing server load and improving UX.
-  Dynamic Poster Fetching: Integrated TMDB API to fetch high-resolution posters in real-time.
-  AJAX Updates: The page updates results dynamically without reloading, providing a smooth, app-like experience.

## Tech Stack

- **Language:** Python  
- **Data Analysis:** Pandas, NumPy (with NumPy-to-JSON serialization fixes)  
- **Machine Learning:** Scikit-learn (`CountVectorizer`, `cosine_similarity`)    
- **Backend:** FastAPI, Uvicorn (ASGI)
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

#  Configuration:
To use the poster fetching feature, obtain an API Key from The Movie Database (TMDB) and replace the placeholder in app.py:
```bash
api_key = "your_tmdb_api_key_here"
```

Author: Mutassim Al Zeem
Project Context: Upgraded from CampusX Machine Learning series to a modern API-first approach.
