from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pickle, requests
import pandas as pd


app = FastAPI()

templates = Jinja2Templates(directory= 'templates')

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
        "recommendations": None  # Initially, there are no recommendations
    })


@app.post("/recommend")

async def get_recommendation(request: Request, movie_name: str = Form(...)):
    index = movies[movies['title'] == movie_name].index[0]
    distances = sorted(list(enumerate(similarities[index])), reverse=True, key=lambda x: x[1])
    
    recommended_movies = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append({
            "title": movies.iloc[i[0]].title,
            "poster": fetch_poster(movie_id)
        })
        
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "recommendations": recommended_movies,
        "movie_list": movies['title'].values
    })