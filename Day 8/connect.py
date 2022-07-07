from distutils import errors
import requests
import pprint
import pandas as pd

import configparser
config = configparser.ConfigParser()
config.read('/Users/ruby/Desktop/VS-Code-Basics/credentials.ini') #PATH TO MY config file on my local device

cred = config["MOVIEDB"]
api_key = cred["MOVIE_API_KEY"]
api_key_v4 = cred["MOVIE_API_KEY_V4"]



#HTTP REQUESTS- Internet connection request
#what's our endpoint or url?. get # -> Grab data. POST -> add/update data
#whats the hhtp method that we need? rest APIs usually have a url that you'll call to get or do something
#params = {"api_key": "your_api_key"}
#r = requests.get(endpoint, params=params)
#API Read Access Token (v4 auth) = eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxOTQ2ZWU2OTI2Y2M2NDA4NjdlNDBhNWQwYTVkNzFjNCIsInN1YiI6IjYyNmFkODYxMmQ1MzFhMDliZmQxNjIxOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.npC0Exhp7BQct8sdQvLjJj7CRZ5udf5Qpv9EAn1mKLc

"""
Endpoint
/movie/{movie_id} #somewhat formatted path
https://api.themoviedb.org/3/movie/550?api_key=api_key
"""

#HTTP Requests methods. GET, POST, PATCH, PUT, DELETE.
movie_id = 500
api_version = 3
api_base_url = f'https://api.themoviedb.org/{api_version}'
endpoint_path = f'/movie/{movie_id}'
endpoint = f'{api_base_url}{endpoint_path}?api_key={api_key}&page=1'
#print(endpoint)
#r = requests.get(endpoint) #json={'api_key': api_key})
#print (r.status_code)
#print (r.text)


#using version v4
movie_id = 501
api_version = 4
api_base_url = f'https://api.themoviedb.org/{api_version}'
endpoint_path = f'/movie/{movie_id}'
endpoint = f'{api_base_url}{endpoint_path}'
#print(endpoint)
headers = {
    'Authorization': f'Bearer {api_key_v4}',
    'Content-Type': 'application/json;charset=utf-8'
} #headers are arguements that you pass into the request that you are doing
#r = requests.get(endpoint, headers = headers) #json={'api_key': api_key})
#print (r.status_code)
#print (r.text)
#curl-> is another way to run a request, pretty similar to a python request, except that you only call it in a terminal.

#search movies of a specific name
api_base_url = f'https://api.themoviedb.org/{api_version}'
endpoint_path = f'/search/movie' #resource path where, resource is any of these endpoints
search_query = 'The Matrix' #or any movie you want to find
endpoint = f'{api_base_url}{endpoint_path}?api_key={api_key}&query={search_query}'
#print(endpoint)
r = requests.get(endpoint)
#pprint.pprint(r.json()) #java script object notation
if r.status_code in range (200, 299):
    data = r.json()
    results = data['results']
    if len(results) > 0:
        print(results[0].keys())
        movie_ids = set() #set ensures that everything in a list is unique, not how many but what numbers
        for result in results:
            _id = result['id'] #we use underscore because typically 'id' is normally used in a program , and sometimes comes along with a language documentation, so to prevent 'syntax' errors
            #print (result['title'], _id) #to grab the id
            movie_ids.add (_id)
        #print (list(movie_ids))

output = 'movies.csv'
movie_data = []
for movie_ids in movie_ids:
    api_version = 3
    api_base_url = f'https://api.themoviedb.org/{api_version}'
    endpoint_path = f'/movie/{movie_id}'
    endpoint = f'{api_base_url}{endpoint_path}?api_key={api_key}'
    r = requests.get(endpoint)
    if r.status_code in range (200,299):
        data = r.json()
        movie_data.append (data)


df = pd.DataFrame (movie_data)
print (df.head())
df.to_csv(output, index = False)