#!/usr/bin/python3
"""
Module containing the top_ten function that queries the Reddit API.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    
    If the subreddit is invalid or an error occurs, prints None.
    """
    # Base URL for the hot posts of a subreddit, limited to 10 results
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    # A custom User-Agent is mandatory to avoid 429 Too Many Requests errors
    headers = {
        "User-Agent": "linux:reddit.api.project:v1.0.0 (by /u/wintermancer)"
    }

    try:
        # allow_redirects=False prevents following 302 redirects to search pages
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the subreddit exists and the request was successful
        if response.status_code == 200:
            results = response.json()
            posts = results.get("data", {}).get("children", [])
            
            if not posts:
                print(None)
                return

            for post in posts:
                print(post.get("data", {}).get("title"))
        else:
            print(None)
            
    except Exception:
        print(None)
