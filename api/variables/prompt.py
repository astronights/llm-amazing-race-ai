puzzle = '''
Please plan out an amazing race itinerary for {city} with upto {n} stops. 
This should be like a text based adventure. Provide a small riddle for
each stop. At each stop provide a small task to find that can be googled.
Here is the input JSON containing the sights: {sights}. Each record conists of 
the latitude and longitude, the name of the attraction and its type. Use these
only to build the itinerary. 
I want the output as a list of JSONs with one record for each stop. 
Each record should include the text based riddle for the stop, a one line hint,
the name of the place as the answer, as well as a small task. The task should
be a JSON record of its own with a small question the user will have to Google
about the place and the answer of the task. For each record, also add in an image
of the sight. Ensure the image is in the markdown format with only the URL and no
alt text. Make sure the task questions have objective answers. For each record, 
also add a message to congratulate the user when they guess the answer to the 
riddle correctly. This congratulatory message should be a one line message
describing the user reaching  the stop. Do not repeat stops. Along with the {n} stops, 
make sure the list of JSONs also has a record for the starting and the ending stop.
Please output the JSON output directly without any backticks so it can be parsed:
'''

description = '''
Please provide a small description about the city of {city} in country {country}.
Limit your description to 50 words to serve as an overview for a tourist visiting
the city for the first time. Provide the description immediately below: 
'''

evaluate = '''
Please evaluate whether the user input is correct according to the saved response.
I want you to check if the responses align with each other.
Saved answer: {answer}
User input: {response}
Only respond with a 1 or a 0 immediately below. If the answers are similar or if
the mean the same thing, return a 1, otherwise return a 0.
Do not respond with more than 1 character.
Enter your response below: 
'''

routing = '''
Based on the following message and body, determine which function should handle the request.
Choose from: get_description, make_puzzle or eval_response.
Only respond with the function name, nothing else.

Message: {message}

Function:
'''