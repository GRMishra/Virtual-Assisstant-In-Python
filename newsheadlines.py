import requests

# Your NewsAPI key
newsapi = "your api key here"  # can get the api-key from https://newsapi.org

# Define the categories or segments
segments = {
    "business": "business",
    "sports": "sports",
    "politics": "politics",
    "stock market": "stock market"
}

# Base URL for NewsAPI
base_url = "https://newsapi.org/v2/top-headlines?"

# Function to fetch top headlines for a given category or keyword
def fetch_top_headlines(segment, query=None):
    if query:
        url = f"{base_url}q={query}&apiKey={newsapi_key}&pageSize=5"
    else:
        url = f"{base_url}category={segment}&country=us&apiKey={newsapi_key}&pageSize=5"
    
    r = requests.get(url)
    
    if r.status_code == 200:
        data = r.json()
        articles = data.get('articles', [])
        
        if articles:
            print(f"\nTop 5 {segment.capitalize()} News:")
            for i, article in enumerate(articles, start=1):
                print(f"{i}. {article['title']}")
        else:
            print(f"No articles found for {segment}.")
    else:
        print(f"Failed to fetch news for {segment}. Status code: {r.status_code}")

# Fetch top headlines for each segment
def fetch_all_segments():
    for segment, query in segments.items():
        fetch_top_headlines(segment, query=query)
