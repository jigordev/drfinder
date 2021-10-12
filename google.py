import requests
import random

SERPAPI_KEYS = ["YOUR SERPAPI KEYS"]

def get_api_key():
	return random.choice(SERPAPI_KEYS)

def get_doctors_by_local(query, location="", country="br", lang="pt"):
	try:
		url = f"https://serpapi.com/search.json?q={query}&location={location}&gl={country}&hl={lang}&tbm=lcl&api_key={get_api_key()}"
		response = requests.get(url).json()
		return response.get("local_results")
	except:
		return None