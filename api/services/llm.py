import os
from ast import literal_eval

import google.generativeai as genai
from ..variables.prompt import puzzle, description, evaluate, routing

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

def get_description(city: str, country: str):
    response = model.generate_content(description.format(city=city, country=country)).text
    print(response)
    return {'description': response}

def make_puzzle(city: str, sights: list, n=10):
    response = model.generate_content(puzzle.format(city=city, n=n, sights=sights)).text
    return literal_eval(response)

def eval_response(answer: str, response: str):
    response = model.generate_content(evaluate.format(answer=answer, response=response)).text
    return {'check': int(response)}

function_map = {
    'get_description': get_description,
    'make_puzzle': make_puzzle,
    'eval_response': eval_response
}

def route_request(message: str, data: dict):
    str_func = model.generate_content(routing.format(message=message)).text.strip()
    func = function_map[str_func]

    return func(**data)