import os

from flask_cors import CORS
from flask import Flask, request

from .services.llm import route_request
from .services.web_utils import get_all_cities, get_nearby_cities, get_coordinates, get_attractions

def get_allowed_origins():
    environment = os.getenv('FLASK_ENV', 'development')
    if environment == 'production':
        return ["https://llm-amazing-race.vercel.app"]
    elif environment == 'development':
        return ["http://localhost:3000", "https://llm-amazing-race.vercel.app"]
    return []  # No origins allowed by default

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": get_allowed_origins()}})


@app.route('/')
def root_hello():
    return '<p>Hello, World!</p>'

@app.get('/api/city/all')
def all_cities():
    return get_all_cities()

@app.post('/api/city/nearby')
def city_coords():
    return get_nearby_cities(**request.json)

@app.get('/api/city/<city>/attr')
def city_attrs(city: str):
    coords = get_coordinates(city)
    ats = get_attractions(*coords)
    return ats

@app.post('/api/llm/chat')
def chat():
    body = request.json
    response = route_request(body['message'], body['data'])
    return response