import os

from flask_cors import CORS
from flask import Flask, request, jsonify

from .services.llm import chat
from .services.web_utils import get_all_cities, get_coordinates, get_attractions


def get_allowed_origins():
    environment = os.getenv('FLASK_ENV', 'development')
    if environment == 'production':
        return ["https://llm-amazing-race.vercel.app"]
    elif environment == 'development':
        return ["http://localhost:3000", "https://llm-amazing-race.vercel.app"]
    return []  # No origins allowed by default

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": get_allowed_origins()}})

@app.before_request
def restrict_cors():
    if 'FLASK_ENV' in os.environ and os.environ['FLASK_ENV'] == 'production':
        origin = request.headers.get('Origin')
        if origin not in get_allowed_origins():
            return jsonify({"error": "Forbidden"}), 403


@app.route('/')
def root_hello():
    return '<p>Hello, World!</p>'

@app.get('/api/city/all')
def all_cities():
    return get_all_cities()

@app.get('/api/city/<city>')
def city_coords(city: str):
    coords = get_coordinates(city)
    return {'city': city, 'lat': coords[0], 'lng': coords[1]}

@app.get('/api/city/<city>/attr')
def city_attrs(city: str):
    coords = get_coordinates(city)
    ats = get_attractions(*coords)
    return ats

@app.post('/api/llm/chat')
def try_chat():
    city = request.json['city']
    coords = get_coordinates(city)
    sights = get_attractions(*coords)
    ans = chat(city, sights)
    return ans