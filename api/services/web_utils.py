import random
from math import radians, degrees, sin, cos, atan2, sqrt

import requests
from collections import defaultdict

from ..variables.overpass import url as overpass_url, attractions, query
from ..variables.mongo import mongo_url, mongo_headers, mongo_payload

def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    radius = 6371 
    return radius * c

def calculate_bounds(lat, lng, radius):
    R = 6371
    
    dlat = radius / R
    dlon = radius / (R * cos(radians(lat)))
    
    min_lat = lat - degrees(dlat)
    max_lat = lat + degrees(dlat)
    min_lng = lng - degrees(dlon)
    max_lng = lng + degrees(dlon)
    
    return min_lat, max_lat, min_lng, max_lng


def get_all_cities():
    body = {**mongo_payload, 'projection': {'city_ascii': 1, 'city': 1,
                                            'country': 1, 'lat': 1, 'lng': 1, 'id': 1}}
    response = requests.post(mongo_url, headers=mongo_headers, json=body)

    cities = response.json().get('documents', [])
    grouped_by_country = defaultdict(list)

    for city in cities:
        country = city.get('country')
        grouped_by_country[country].append({
            'name': city.get('city', city.get('city_ascii', '')), 'country': city['country'],
            'lat': city['lat'], 'lng': city['lng'], 'id': city['id']
        })

    return dict(grouped_by_country)


def get_nearby_cities(lat: float, lng: float, radius: float = 1000):
    min_lat, max_lat, min_lng, max_lng = calculate_bounds(lat, lng, radius)
    
    query = {
        'lat': {'$gte': min_lat, '$lte': max_lat},
        'lng': {'$gte': min_lng, '$lte': max_lng}
    }

    body = {**mongo_payload,
            'filter': query,
            'projection': {'city_ascii': 1, 'city': 1, 'country': 1,
                           'iso2': 1, 'lat': 1, 'lng': 1, 'id': 1}}
    
    cities = requests.post(mongo_url, headers=mongo_headers, json=body).json()['documents']

    for city in cities:
        city['distance'] = haversine(lat, lng, city['lat'], city['lng'])
        city['name'] = city.get('city', city.get('city_ascii', ''))
    
    cities_sorted = sorted(cities, key=lambda x: x['distance'])
    
    return cities_sorted[:20]

def get_coordinates(city: str):
    body = {**mongo_payload,
            'filter': {'city_ascii': city},
            'projection': {'lat': 1, 'lng': 1, '_id': 0}}
    response = requests.post(mongo_url, headers=mongo_headers, json=body)
    vals = response.json()['documents'][0]
    return [vals['lat'], vals['lng']]


def detail(item: dict):
    return {
        'lat': item.get('lat', item.get('center', {}).get('lat')),
        'lnt': item.get('lon', item.get('center', {}).get('lon')),
        'id': item['id'],
        'name': item['tags']['name:en'].split(',')[0],
        'type': item['tags'].get('tourism',
                                 item['tags'].get('historic',
                                                  item['tags'].get('amenity',
                                                                   item['tags'].get('leisure'))))
    }


def get_attractions(lat: float, lng: float, n: int = 10, radius: float = 10000):
    out = []
    for attr in attractions:
        response = requests.get(overpass_url, params={'data': query.format(
            attraction=attr, radius=radius, lat=lat, lng=lng)})
        data = response.json()['elements']
        val = [detail(point) for point in data]
        out.extend(val)

    return out if len(out) < n else random.choices(out, k=n)
