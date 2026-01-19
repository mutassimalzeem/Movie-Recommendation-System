from fastapi import FastAPI, Request, Form, Query
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import pickle, requests, json
import pandas as pd

app = FastAPI()

templates = Jinja2Templates(directory='templates')

movies = pickle.load(open('movie_list.pkl', 'rb'))
similarities = pickle.load(open('similarity.pkl', 'rb'))

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    return "https://via.placeholder.com/500x750?text=No+Poster"

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "movie_list": movies['title'].values,
        "recommendations": []
    })

@app.post("/recommend")
async def get_recommendation(request: Request):
    data = await request.json()
    movie_name = data.get('movie_name')
    
    try:
        index = movies[movies['title'] == movie_name].index[0]
        distances = sorted(list(enumerate(similarities[index])), reverse=True, key=lambda x: x[1])
        
        recommended_movies = []
        for i in distances[1:6]:
            movie_id = int(movies.iloc[i[0]].movie_id)
            recommended_movies.append({
                "id": movie_id,
                "title": movies.iloc[i[0]].title,
                "poster": fetch_poster(movie_id)
            })
        
        return JSONResponse({
            "success": True,
            "recommendations": recommended_movies,
            "movie_name": movie_name
        })
    except IndexError:
        return JSONResponse({
            "success": False,
            "message": "Movie not found"
        }, status_code=404)

@app.get("/movie/{movie_id}")
async def movie_details(request: Request, movie_id: int):
    api_key = "YOUR_API_KEY"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    response = requests.get(url).json()

    movie_info = {
        "title": response.get("title"),
        "overview": response.get('overview'),
        "release_date": response.get("release_date"),
        "rating": response.get("vote_average"),
        "poster": f"https://image.tmdb.org/t/p/w500{response.get('poster_path')}"
    }
    
    return templates.TemplateResponse("details.html", {"request": request, "movie": movie_info})

@app.get("/autocomplete")
async def autocomplete(q: str = Query(None)):
    if not q:
        return []
    
    suggestions = movies[movies['title'].str.contains(q, case=False, na=False)]
    return suggestions['title'].tolist()[:10]
