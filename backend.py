import requests
import wikipedia

# Set API Keys
JSEARCH_API_KEY = "fa1b1a3250msh76cb65b21c97956p1bb67fjsn512fa71fd7b1"

def get_career_advice(question):
    """Fetch career advice using Wikipedia summaries"""
    try:
        summary = wikipedia.summary(question, sentences=2)
        return summary
    except wikipedia.exceptions.PageError:
        return "⚠️ No relevant Wikipedia page found."
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

def search_jobs(query, location=""):
    """Fetch job listings from JSearch API"""
    url = "https://jsearch.p.rapidapi.com/search"
    headers = {
        "X-RapidAPI-Key": JSEARCH_API_KEY,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }
    params = {"query": query, "location": location, "page": 1}
    
    response = requests.get(url, headers=headers, params=params)
    jobs = response.json().get("data", [])
    
    return jobs[:5]  # Return top 5 job listings
